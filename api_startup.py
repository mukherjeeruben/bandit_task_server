from flask import Flask
from flask_restx import Api
import config
from flask_cors import CORS


##############Import service###############
from service.static_templates_service import api as statictemplates
from service.data_record_service import api as usergamedata
from service.storage_service import api as app_storage
###########################################


flask_app = Flask(__name__)
CORS(flask_app)
API = Api(flask_app, title=config.API_TITLE, version=config.API_VERSION, description=config.API_DESCRIPTION + config.API_STYLE)

############Append Namespace##############
API.add_namespace(statictemplates)
API.add_namespace(usergamedata)
API.add_namespace(app_storage)
###########################################

if __name__ == '__main__':
    flask_app.run(debug=config.DEBUG)
