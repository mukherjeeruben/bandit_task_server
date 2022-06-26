from flask_restx import Resource
from flask import jsonify
from model.static_templates_model import api, FILE_UPLOAD
from dal.templates_dal import get_template_data, create_template_data
from bl.template_bl import preprocess_template_file
from interface.JSON_Encoder import JSONEncoder
import json


# @api.route("/create") # TODO Keep commented during check-in
class CreateStaticData(Resource):
    @api.expect(FILE_UPLOAD)
    @api.doc(response={200: 'Success', 400: 'Validation Error'})
    @api.response('default', 'Error')
    def post(self):
        args = FILE_UPLOAD.parse_args()
        uploaded_file = args['file']
        dataset = preprocess_template_file(uploaded_file)
        response = create_template_data(dataset)
        return jsonify(response)


@api.route("/getTemplate/<templatetype>")
class GetStaticData(Resource):
    @api.doc(response={200: 'Success', 400: 'Validation Error'})
    @api.response('default', 'Error')
    def get(self, templatetype):
        '''Get game template for bandit task'''
        template = get_template_data(templatetype=templatetype)
        result = JSONEncoder().encode(template)
        return json.loads(result)