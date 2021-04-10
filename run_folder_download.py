'''
'''
from utils import authenticate
from utils import get_folder_id
from pathlib import Path

# https://gist.github.com/jmlrt/f524e1a45205a0b9f169eb713a223330

# Import Google libraries
# from pydrive.auth import GoogleAuth
# from pydrive.drive import GoogleDrive

# Import general libraries
from argparse import ArgumentParser
from os import chdir, listdir


parser = ArgumentParser(
    description="Download Google Drive folder to local")
parser.add_argument('-s', '--source', type=str,
                    help='Folder name to download')
parser.add_argument('-d', '--destination', type=str,
                    help='Local destination Folder')
parser.add_argument('-p', '--parent', type=str,
                    help='Parent Folder in Google Drive')

args = parser.parse_args()
src_folder_name = args.source
dst_folder = args.destination
parent_folder_name = args.parent

chdir('/Users/tim/Research/Data-Analysis/remote-gpu-cellpose')

drive = authenticate()
gparent_id = get_folder_id(drive, 'root', 'image-processing')
gfolder_id = get_folder_id(drive, gparent_id, src_folder_name)

gfile_obj = drive.CreateFile({'id': gfolder_id})
print(gfile_obj["title"], gfile_obj["mimeType"])
# gfile_obj.GetContentFile(gfile_obj['title'])

if not Path(dst_folder).exists():
    Path(dst_folder).mkdir()

# # Enter the source folder
try:
    chdir(dst_folder)
# Print error if source folder doesn't exist
except OSError:
    print(src_folder_name + ' is missing')

# # To list asll files in a particular folder. (***)
file_list = drive.ListFile(
    {'q': f"'{gfolder_id}' in parents and trashed=false"}
    ).GetList()

for file_ in file_list:
    print('title: %s, id: %s' % (file_['title'], file_['id']))
    file_.GetContentFile(file_['title'])
