from app import app
from app.libraries.random_string import RandomString
from app.libraries.token_handler import TokenHandler
from app.models.model_payment import ModelPayment
from app.models.model_payment_session import ModelPaymentSession
from datetime import datetime
import requests

class PaymentService(object):
    config = {}
    base_result = {
        'data': None,
        'total_data': 0
    }
    PAYMENT_CODE_LENGTH = 11
    PAYMENT_TOKEN_LENGTH = 118
    MOUNTAIN_HOST = app.environment.get('APP_MOUNTAIN_HOST')
    
    def __init__(self, config = None):
        super(PaymentService, self).__init__()

        if config:
            self.config = config

    def generate_payment_list(self, data_model = None):
        data_sql = getattr(ModelPayment(data_model), 'get_list')()

        raw_data = data_sql.get('data')

        if raw_data:
            for item_raw_data in raw_data:
                # Get payment session value
                payment_token = item_raw_data.get('payment_token')

                content_data_session = getattr(ModelPaymentSession(), 'get_detail_by')('token', payment_token)
                content_data_session = content_data_session.get('data')

                item_raw_data['is_expired'] = self.check_payment_expired(content_data_session.get('expired'))

        self.base_result['data'] = data_sql.get('data')
        self.base_result['total_data'] = data_sql.get('total_rows')

        return self.base_result

    def generate_payment_detail(self, columns = None, payment_code = None):
        data_sql = getattr(ModelPayment(), 'get_detail_by')(columns, payment_code)

        raw_data = data_sql.get('data')

        if raw_data:
            # Get payment session value
            payment_token = raw_data.get('payment_token')

            content_data_session = getattr(ModelPaymentSession(), 'get_detail_by')('token', payment_token)
            content_data_session = content_data_session.get('data')
            
            raw_data['is_expired'] = self.check_payment_expired(content_data_session.get('expired'))

        self.base_result['data'] = data_sql.get('data')
        self.base_result['total_data'] = data_sql.get('total_rows')

        return self.base_result

    def create_payment(self, data_model = None):
        # To Do :: Create validation here
        payment_token = self.generate_payment_token()
        data_model['payment_token'] = payment_token

        getattr(ModelPaymentSession(), 'create_data')({
            'token': payment_token
        })

        payment_session_id = app.mysql_lastrowid

        payment_session_detail = getattr(ModelPaymentSession(), 'get_detail_by')('id', payment_session_id)
        payment_session_created = payment_session_detail['data']['created_at']
        
        payment_expired = TokenHandler({
            'time_by': 'minute',
            'time_by_value': 30,
            'session_time': payment_session_created
        }).create_expired_time()

        queries = "expired='{}'".format(payment_expired)
        
        data_model_session = {
            'id': payment_session_id,
            'data': queries
        }

        getattr(ModelPaymentSession(), 'update_data')(data_model_session)

        getattr(ModelPayment(), 'create_data')(data_model)

    def update_payment(self, data_model = None):
        # To Do :: Create validation here
        getattr(ModelPayment(), 'update_data')(data_model)

        # Get detail payment 
        payment_code = data_model.get('code')
        raw_payment_detail = self.generate_payment_detail('code', payment_code.upper())
        data_payment_detail = raw_payment_detail.get('data')

        if data_payment_detail:
            # Update booking status in mountain apps
            booking_code = data_payment_detail.get('booking_code')
            transaction_status = data_payment_detail.get('transaction_status')

            if booking_code:
                data_update_booking = {
                    'payment_status': transaction_status
                }
                res_update_booking = requests.put('{}/booking/{}'.format(self.MOUNTAIN_HOST, booking_code), json = data_update_booking)
                res_update_booking = res_update_booking.json()

    def generate_payment_code(self):
        result = RandomString({
            'key_length': self.PAYMENT_CODE_LENGTH
        }).run()

        result = '{}{}'.format('PAY', result.upper())

        return result

    def generate_payment_token(self):
        result = RandomString({
            'key_length': self.PAYMENT_TOKEN_LENGTH
        }).run()

        return result.upper()

    def check_availability_payment_code(self, payment_code = None):
        availability_result = {
            'status': 0,
            'message': 'Available',
            'payment_code': payment_code
        }

        # Check availability payment code
        data_sql = getattr(ModelPayment(), 'get_detail_by')('code', payment_code)

        if data_sql.get('data'):
            availability_result['status'] = 1
            availability_result['message'] = 'Not Available'

        self.base_result['data'] = availability_result
        self.base_result['total_data'] = data_sql.get('total_rows')

        return self.base_result

    def check_payment_expired(self, expired_time = None):
        return TokenHandler().check_expired_time(expired_time)