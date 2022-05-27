from flask_restx import Resource
from flask import jsonify
from model.data_record_model import api
from dal.record_game_data_dal import record_user_data


@api.route("/insert_user_data")
class InsertUserGameData(Resource):
    def post(self):
        x = record_user_data()
        return jsonify(x)