from app import app
from app.core.models import Models
import json

class ModelPayment(Models):
    def __init__(self, params = None):
        super(ModelPayment, self).__init__(params)

        self.table_name = 'payment'

    def get_list(self):
        sql_rows = self.execute("SELECT \
        id, \
        code, \
        user_id, \
        amount, \
        unique_code, \
        booking_code, \
        type, \
        transaction_id, \
        {}, \
        transaction_status, \
        payment_token, \
        {}, {} from `{}`".format(self.convert_time_zone('transaction_time'), self.convert_time_zone('created_at'), self.convert_time_zone('updated_at'), self.table_name))

        convert_attribute_list = [
            'transaction_time',
            'created_at',
            'updated_at'
        ]

        sql_rows = self.convert_to_normal_date(sql_rows, convert_attribute_list)

        return sql_rows

    def get_detail_by(self, columns = None, value = None):
        if columns == "name":
            value = value.replace('-', ' ')

        sql_rows = self.execute("SELECT \
        id, \
        code, \
        user_id, \
        amount, \
        unique_code, \
        booking_code, \
        type, \
        transaction_id, \
        {}, \
        transaction_status, \
        payment_token, \
        {}, {} from `{}` WHERE `{}` = '{}'".format(self.convert_time_zone('transaction_time'), self.convert_time_zone('created_at'), self.convert_time_zone('updated_at'), self.table_name, columns, value))

        convert_attribute_list = [
            'transaction_time',
            'created_at',
            'updated_at'
        ]

        sql_rows = self.convert_to_normal_date(sql_rows, convert_attribute_list)

        return sql_rows

    def create_data(self, value = None):
        action = {}

        action['{}'.format(self.table_name)] = {
            'action': self.action_type.get('insert'),
            'command': (
                "INSERT INTO `{}` (\
                `code`, \
                `user_id`, \
                `amount`, \
                `unique_code`, \
                `booking_code`, \
                `type`, \
                `payment_token`, \
                `created_at` \
                ) VALUES".format(self.table_name) +
                " (\
                '{}',\
                '{}',\
                '{}',\
                '{}',\
                '{}',\
                '{}',\
                '{}',\
                NOW())".format(
                    value.get('code'),
                    value.get('user_id'),
                    value.get('price_total'),
                    value.get('unique_code'),
                    value.get('booking_code'),
                    value.get('type'),
                    value.get('payment_token')
                )
            )
        }

        self.execute_command(
            action
        )

    def update_data(self, value):
        action = {}

        action['{}'.format(self.table_name)] = {
            'action': self.action_type.get('update'),
            'command': (
                "UPDATE `{}` SET {}, updated_at=NOW() WHERE code={}".format(self.table_name, value.get('data'), value.get('code'))
            )
        }

        self.execute_command(
            action
        )

    def delete_data(self, value):
        action = {}

        action['{}'.format(self.table_name)] = {
            'action': self.action_type.get('delete'),
            'command': (
                "DELETE FROM `{}` WHERE id={}".format(self.table_name, value)
            )
        }

        self.execute_command(
            action
        )