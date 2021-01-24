import requests
from http.client import BAD_REQUEST
from flask import Flask, request, abort, logging
from pydantic import ValidationError
from settings import get_settings
from models import AddressDetailRequest

app = Flask(__name__)
app.config["DEBUG"] = True
logger = logging.create_logger(app)

settings = get_settings()


@app.route('/', methods=['GET'])
def home():
    return "<h1>this is working</h1>"


@app.route('/getAddressDetails', methods=['POST'])
def get_address_details():
    """
    this API returns coordinates for the provides human readable address using googles geocode api service
    :return: json or xml containing coordinate data
    """

    try:
        body = AddressDetailRequest.validate(request.get_json())
        response = requests.get(url=f'{settings.GEOCODE_API_ENDPOINT}/{body.output_format}',
                                params={"address": body.address, 'key': settings.GEO_CODE_API_KEY})
        return response.content
    except ValidationError as err:
        abort(BAD_REQUEST, err)


app.run(port=8000)
