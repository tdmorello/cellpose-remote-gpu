from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# https://gist.github.com/jmlrt/f524e1a45205a0b9f169eb713a223330

# Import Google libraries
from pydrive.files import GoogleDriveFileList


def authenticate():
    # https://stackoverflow.com/questions/24419188/automating-pydrive-verification-process
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile("authcreds.txt")
    if gauth.credentials is None:
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        gauth.Refresh()
    else:
        gauth.LocalWebserverAuth()
    gauth.SaveCredentialsFile("authcreds.txt")
    drive = GoogleDrive(gauth)
    return drive


def get_folder_id(drive, parent_folder_id, folder_name):
    """
        Check if destination folder exists and return it's ID
    """
    # Auto-iterate through all files in the parent folder.
    file_list = GoogleDriveFileList()
    file_list = drive.ListFile(
        {'q': "'{0}' in parents and trashed=false".format(parent_folder_id)}  # noqa
    ).GetList()

    for file1 in file_list:
        if file1['title'] == folder_name:
            print('title: %s, id: %s' % (file1['title'], file1['id']))
            return file1['id']


def main():
    drive = authenticate()
    print(get_folder_id(drive, 'root', 'image-processing'))


if __name__ == '__main__':
    main()
