from flask_restx import Resource
from flask import jsonify
from model.data_record_model import api
from dal.record_game_data_dal import record_user_data
from model.data_record_model import user_game_data_field


@api.route("/insert_user_game_data")
class InsertUserGameData(Resource):
    @api.doc(response={200: 'Success', 400: 'Validation Error'})
    @api.response('default', 'Error')
    @api.expect(user_game_data_field)
    def post(self):
        '''Insert User game data to database'''
        user_game_data_set = list()
        user_game_data_set.append(api.payload)
        result = record_user_data(user_game_data_set)
        return jsonify(result)

