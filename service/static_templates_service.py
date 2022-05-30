from flask_restx import Resource
from flask import jsonify
from model.static_templates_model import api
from dal.templates_dal import get_template_data, create_template_data
from interface.JSON_Encoder import JSONEncoder
import json


# @api.route("/create")
class CreateStaticData(Resource):
    def post(self):
        x = create_template_data()
        return jsonify(x)


@api.route("/get")
class GetStaticData(Resource):
    def get(self):
        template = get_template_data()
        result = JSONEncoder().encode(template)
        return json.loads(result)