from flask_restx import Namespace, fields

api = Namespace('UserGameRecordData', description='Record User Game Data from Two Arm Bandit Task')

record_data = api.model('game_set_data', {
    'selection': fields.String(attribute='Leprechaun Selection'),
    'reward': fields.Integer(attribute='reward'),
    'total_score': fields.Integer(attribute='Total Score')
})

user_game_data_field = api.model('user_game_data_set', {
    'iteration_number': fields.Nested(record_data)})

