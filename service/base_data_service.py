from flask_restx import Resource
from model.base_data_model import api
import random, string


@api.route("/createuserid")
class CreateUserId(Resource):
    @api.doc(response={200: 'Success', 400: 'Validation Error'})
    @api.response('default', 'Error')
    def get(self):
        user_id = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        return user_id
