from flask_restx import Namespace, fields

api = Namespace('GameRecordData', description='Record User Game Data from Two Arm Bandit Task')

user_game_data_fields = api.model('Game Data', {
    'Selections': fields.String(attribute='selections')
    })