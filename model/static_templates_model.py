from flask_restx import Namespace, reqparse, fields
from werkzeug.datastructures import FileStorage

api = Namespace('StaticGameTemplate', description='Static Template Scores for Two Arm Bandit Task')

# For File Upload
FILE_UPLOAD = reqparse.RequestParser(bundle_errors=True)
FILE_UPLOAD.add_argument('file', location='files', type=FileStorage, required=True)

