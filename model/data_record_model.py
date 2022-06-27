from flask_restx import Namespace, fields

api = Namespace('UserGameRecordData', description='Record User Game Data from Two Arm Bandit Task')

record_data = api.model('game_set_data', {
    'action': fields.String(attribute='Leprechaun Selection'),
    'reward': fields.Integer(attribute='reward'),
    'total_score': fields.Integer(attribute='Total Score')
})

user_game_data_field = api.model('user_game_data_set', {
    'interface_type': fields.String(attribute='interface_type'),
    'user_id': fields.String(attribute='user_id'),
    'game_data': fields.Nested(record_data),
    'creation_time': fields.String(attribute='creation_time')})


