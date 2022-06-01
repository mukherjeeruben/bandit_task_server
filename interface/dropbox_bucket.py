from dropbox.files import WriteMode
from connection.dropbox_connect import create_bucket_connection


def upload_file(fileobject):
    try:
        '''File Upload to in Folder Apps/heroku_dev_app'''
        dbx_conn = create_bucket_connection()
        response = dbx_conn.files_upload(fileobject.read(), '/' + fileobject.filename, mode=WriteMode('overwrite'))
        if response:
            return 'File Uploaded to Bucket'
    except Exception as drp_err:
        return 'File Upload to Bucket Failed: '+str(drp_err)


def get_file_list():
    try:
        '''File List from Bucket'''
        dbx_conn = create_bucket_connection()
        file_list = list()
        for entry in dbx_conn.files_list_folder('').entries:
            file_list.append(entry.name)
        return file_list
    except Exception as drp_err:
        return 'Error while fetching file list from bucket: '+str(drp_err)