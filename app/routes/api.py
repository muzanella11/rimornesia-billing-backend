from flask import request, send_from_directory
from app import app
from app.libraries.slug_validate import SlugValidate
from app.controllers.health_indicator import HealthIndicator
from app.controllers.uploads import Uploads
from app.controllers.payment import Payment

@app.route('/api')
def helloapi():
    return "Hello World!"

## Health Check ##
@app.route('/health')
def health_indicator():
    return HealthIndicator().run()
##################

## Payment ##
@app.route('/payment/code')
def paymentcodeapi():
    return Payment(request).get_payment_code()

@app.route('/payment/code/<value>', methods=['POST'])
def paymentcodeavailabilityapi(value):
    return Payment(request).get_availability_code(value.upper())

@app.route('/payment')
def paymentlistapi():
    return Payment(request).get_list()

@app.route('/payment/<payment_code>')
def paymentdetailapi(payment_code):
    return Payment(request).get_detail('code', payment_code.upper())

@app.route('/payment', methods=['POST'])
def paymentcreateapi():
    return Payment(request).create_data()

@app.route('/payment/<payment_code>', methods=['PUT'])
def paymentupdateapi(payment_code):
    return Payment(request).update_data(payment_code.upper())
##################

## Uploads ##
@app.route('/uploads/<path:path>')
def uploadgetfile(path):
    return Uploads(request).get_detail(path)

@app.route('/uploads', methods=['POST'])
def uploadcreateapi():
    return Uploads(request).create_data()

@app.route('/uploads/delete/<path:path>', methods=['DELETE'])
def uploaddeletefile(path):
    return Uploads(request).delete_data(path)
##################