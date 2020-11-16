from app.core.controllers import BaseControllers
from app.services.payment_service import PaymentService
import re
import json

class Payment(BaseControllers):
    request = None

    TABLES = {}

    def __init__(self, request = None):
        super(Payment, self).__init__()

        self.request = request

    def run(self):
        data = {
            'code': 200,
            'message': 'Success',
            'data': []
        }

        return self.create_response(data)

    def get_list(self):
        data = {
            'code': 200,
            'message': 'Success',
            'data': [],
            'total_data': 0
        }

        data_model = {
            'type': 'list',
            'pagination': True,
            'filter': self.request.args
        }

        data_sql = PaymentService().generate_payment_list(data_model)

        data['data'] = data_sql.get('data')
        data['total_data'] = data_sql.get('total_rows')

        return self.create_response(data)

    def get_detail(self, columns = None, value = None):
        if columns == "error":
            return self.create_response({
                'code': 400,
                'messages': 'Bad Request'
            })

        data = {
            'code': 200,
            'message': 'Success',
            'data': {},
            'total_data': 0
        }

        data_sql = PaymentService().generate_payment_detail(columns, value)

        data['data'] = data_sql.get('data')
        data['total_data'] = data_sql.get('total_rows')

        return self.create_response(data)

    def get_payment_code(self):
        data = {
            'code': 200,
            'message': 'Success',
            'data': {}
        }

        data['data'] = {
            'payment_code': PaymentService().generate_payment_code()
        }

        return self.create_response(data)

    def get_availability_code(self, value = None):
        if not value:
            return self.create_response({
                'code': 400,
                'messages': 'Bad Request'
            })

        data = {
            'code': 200,
            'message': 'Success',
            'data': {},
            'total_data': 0
        }
        
        # Check availability payment code
        availability = PaymentService().check_availability_payment_code(value)

        data['data'] = availability['data']
        data['total_data'] = availability['total_data']

        return self.create_response(data)

    def create_data(self):
        data = {
            'code': 200,
            'message': 'Success',
            'total_data': 0
        }

        request_data = self.request.json

        payment_type = request_data.get('type')
        payment_code = request_data.get('code')
        user_id = request_data.get('user_id')
        price_total = request_data.get('price_total')
        unique_code = request_data.get('unique_code')
        booking_id = request_data.get('booking_id')
        booking_code = request_data.get('booking_code')

        data_model = {
            'type': payment_type,
            'code': payment_code,
            'user_id': user_id,
            'booking_id': booking_id,
            'booking_code': booking_code,
            'price_total': price_total,
            'unique_code': unique_code
        }

        PaymentService().create_payment(data_model)

        return self.create_response(data)

    def update_data(self, payment_code = None):
        if not payment_code:
            return self.create_response({
                'code': 400,
                'messages': 'Bad Request'
            })

        data = {
            'code': 200,
            'message': 'Success',
            'total_data': 0
        }

        request_data = self.request.json

        transaction_id = request_data.get('transaction_id')
        transaction_time = request_data.get('transaction_time')
        transaction_status = request_data.get('transaction_status')

        queries = "transaction_id='{}',\
            transaction_time='{}',\
            transaction_status='{}'".format(transaction_id, transaction_time, transaction_status)
        
        data_model = {
            'code': payment_code,
            'data': queries
        }

        PaymentService().update_payment(data_model)

        return self.create_response(data)
        