from flask import request, send_from_directory
from app import app
from app.libraries.slug_validate import SlugValidate
from app.controllers.health_indicator import HealthIndicator
from app.controllers.uploads import Uploads

@app.route('/api')
def helloapi():
    return "Hello World!"

## Health Check ##
@app.route('/health')
def health_indicator():
    return HealthIndicator().run()
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