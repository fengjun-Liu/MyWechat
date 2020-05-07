import requests
url = 'https://api.jsonbin.io/b'
headers = {
  'Content-Type': 'application/json',
  'secret-key': '<SECRET_KEY>'
}
data = {"Sample": "Hello World"}

req = requests.post(url, json=data, headers=headers)
print(req.text)

BIN_ID=json.loads(req.content)['id']


url = 'https://api.jsonbin.io/b/<BIN_ID>'
headers = {'secret-key': '<SECRET_KEY>'}

req = requests.put(url, json=nil, headers=headers)
print(req.text)


import requests
url = 'https://api.jsonbin.io/b/<BIN_ID>'
headers = {'Content-Type': 'application/json'}
data = {"Sample": "Hello World"}

req = requests.put(url, json=data, headers=headers)
print(req.text)


import requests
url = 'https://api.jsonbin.io/b/<BIN_ID>'
headers = {'secret-key': '<SECRET_KEY>'}

req = requests.delete(url, json=nil, headers=headers)
print(req.text)
