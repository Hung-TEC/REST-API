import requests
from requests.auth import HTTPBasicAuth
import json

HOST = '192.168.1.101'
USER = 'student'
PASS = 'Meilab123'
BASE_URL = 'http://{0}/restconf/api/running/'.format(HOST)

def set_interfaces(append_url, interface_name):
    url = BASE_URL + append_url + interface_name
    auth = HTTPBasicAuth(USER, PASS)
    headers = {
                'Accept': 'application/vnd.yang.data+json',
               'Content-Type': 'application/vnd.yang.data+json'
               }

    data = {
            "ietf-interfaces:interface": {
                "name": "GigabitEthernet3",
                "description": "to R1",
                "type": "iana-if-type:ethernetCsmacd",
                "enabled": 'true',
                "ietf-ip:ipv4": {
                    "address": [
                        {
                            "ip": "90.0.10.75",
                            "netmask": "255.255.255.0"
                        }
                    ]
                },
                "ietf-ip:ipv6": {}
            }
        }

    response = requests.put(url, auth=auth, headers=headers, data=json.dumps(data))
    if response.status_code == 204:
        return "success!"
    else:
        return response.text

print (set_interfaces("interfaces/interface/", "GigabitEthernet3"))

