import tempfile

import werkzeug
import darknet

import config
import load_model_object

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource


class ObjectDetection(Resource):
    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')
        args = parse.parse_args()

        img_file = args['file']

        if not img_file:
            return {'no file'}, 417

        with tempfile.NamedTemporaryFile() as f:
            img_data = args['file'].read()
            f.write(img_data)
            detect_result = darknet.detect(load_model_object.get.model['net'], 
                                           load_model_object.get.model['meta'], 
                                           f.name.encode("utf-8"))

        return detect_result, 201


def serve():
    load_model_object.get()

    app = Flask(__name__)
    api = Api(app)

    api.add_resource(ObjectDetection, '/object_detection')

    app.run(host=config.server_address, port=config.server_port, debug=False)


