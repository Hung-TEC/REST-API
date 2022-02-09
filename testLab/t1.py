import requests
from requests.auth import HTTPBasicAuth
import json

HOST = '192.168.1.101'
USER = 'student'
PASS = 'Meilab123'
BASE_URL = 'http://{0}/restconf/api/running/'.format(HOST)


def get_interfaces(append_url):
    url = BASE_URL + append_url
    auth = HTTPBasicAuth(USER, PASS)
    headers = {'Accept': 'application/vnd.yang.data+json'}

    response = requests.get(url, auth=auth, headers=headers)
    if response.status_code == 200:
        return json.dumps(response.json(), sort_keys=True, indent=4 )
    else:
        return response.text
a = get_interfaces('interfaces')
print(a)
