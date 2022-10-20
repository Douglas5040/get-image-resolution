from cgitb import handler
from distutils.log import debug
import flask 
import base64
from flask import request
from controller import ImageResolutionController

import logging
import sys
import io

default_out = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

root = logging.getLogger()
root.setLevel(logging.DEBUG)

handler = logging.StreamHandler(default_out)
handler.setLevel(logging.DEBUG)
formater = logging.Formatter('%(message)s')
handler.setFormatter(formater)
fh = logging.FileHandler("api.log")
fh.setFormatter(formater)
root.addHandler(handler)
root.addHandler(fh)

app = flask.Flask(__name__)
app.config['DEBUG'] = True

img_resolution = ImageResolutionController()

@app.route('/', methods=['GET'])
def home():
    return "<h1>Get image resolution API</h1>" 


@app.route('/get-resolution', methods=['POST'])
def get_resolutions():
    if not request.json or 'image_data' not in request.json:
        return {}, 400

    data = request.json
    image_data = data['image_data']

    try:
        h, w = img_resolution.get_resolution(image_data)

        if not h or not w:
            return {"error": "invalid image"}, 200

        print("Resolution ---> ", f'{w}x{h}')
        return {'resolution': {'largura': w, 'altura': h}}, 200

    except Exception as e:
        logging.error(f'ERROR >> ', e)
        return {'error': str(e)}, 500


app.run("0.0.0.0", port=80, debug=True)