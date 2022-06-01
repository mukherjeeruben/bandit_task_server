from flask_restx import Resource
from model.storage_model import api, FILE_UPLOAD
from interface.dropbox_bucket import upload_file, get_file_list


@api.route('/uplaodfile')
class UplaodFileClass(Resource):
    @api.doc(response={200: 'Success', 400: 'Validation Error'})
    @api.expect(FILE_UPLOAD)
    @api.response('default', 'Error')
    def post(self):
        '''Upload File service to dropbox'''
        args = FILE_UPLOAD.parse_args()
        uploaded_file = args['file']
        response = upload_file(uploaded_file)
        return response


@api.route('/getfilelist')
class FetchFileListClass(Resource):
    @api.doc(response={200: 'Success', 400: 'Validation Error'})
    @api.response('default', 'Error')
    def get(self):
        '''Get File List from dropbox'''
        response = get_file_list()
        return response