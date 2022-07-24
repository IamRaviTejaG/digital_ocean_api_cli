# Gets user SSH keys

import json

import requests
from config.constants import (DIGITAL_OCEAN_API_HEADERS,
                              DIGITAL_OCEAN_SSH_KEYS_URL)


def get_user_ssh_keys():
    response = requests.request("GET", DIGITAL_OCEAN_SSH_KEYS_URL, headers=DIGITAL_OCEAN_API_HEADERS)
    ssh_keys_data = json.loads(response.text)

    return ssh_keys_data['ssh_keys']
