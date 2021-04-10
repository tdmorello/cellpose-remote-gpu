
# Remote GPU Cellpose (Google Colab)
## Notes
- Work in root level directory of Google Drive
- Delete Temp folders when done

# Python Scripts and arguments

## ./run_upload_folder.py
### CLI args
`--source (local folder: Path)`  
`--destination (google drive folder: str)`

## ./run_remote_cellpose.py
### CLI args
`--server` (ssh server address: str)  
`--script` (cellpose script location: Path)  
`--output` (output directory: Path)  
`--[cellpose params]`
```
# functions

upload_script(source, server, destination)
run_script(server, script, **params)
```

## ./run_download_folder.py
`--source` (google drive folder: str)  
`--destination` (local folder: Path)

## ./run_clean.py
`--folders` List\[str\]  
*remove Temp folders*

## ./utils.py
```
# Pydrive helper functions
authenticate()
get_folder_id()

# Subprocess function
run_command()
```
# Setup
## Virtual environment
```
pip install -r requirements.txt
```

## pydrive
- client_secrets.json
## colab-ssh
- passwordless login
- Github personal token
