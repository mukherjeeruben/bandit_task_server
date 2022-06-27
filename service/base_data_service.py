from flask_restx import Resource
from model.base_data_model import api
from dal.base_data_dal import record_consent_data
from flask import jsonify
import random, string


@api.route("/createuserid")
class CreateUserId(Resource):
    @api.doc(response={200: 'Success', 400: 'Validation Error'})
    @api.response('default', 'Error')
    def get(self):
        '''Get random session user id'''
        user_id = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        return user_id


@api.route("/record_consent_data")
class InsertUserConsentData(Resource):
    @api.doc(response={200: 'Success', 400: 'Validation Error'})
    @api.response('default', 'Error')
    def post(self):
        '''Insert User Consent data to database'''
        user_consent_data = list()
        user_consent_data.append(api.payload)
        result = record_consent_data(user_consent_data)
        return jsonify(result)
