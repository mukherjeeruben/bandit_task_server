from flask_restx import Namespace, fields

api = Namespace('StaticTemplates', description= 'Static Template Scores for Two Arm Bandit Task')

static_entry_fields = api.model('Static Data', {
    'Name': fields.String(attribute='name')
    })