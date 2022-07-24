

import json

import requests
from config.constants import (DIGITAL_OCEAN_API_BASE_URL,
                              DIGITAL_OCEAN_API_HEADERS)


def get_user_ssh_keys():
    ssh_url = f"{DIGITAL_OCEAN_API_BASE_URL}/account/keys"
    response = requests.request("GET", ssh_url, headers=DIGITAL_OCEAN_API_HEADERS)
    ssh_keys_data = json.loads(response.text)

    return ssh_keys_data['ssh_keys']



def ssh_selector():
    ssh_url = f"{DIGITAL_OCEAN_API_BASE_URL}/account/keys"
    response = requests.request("GET", ssh_url, headers=DIGITAL_OCEAN_API_HEADERS)
    ssh_keys_data = json.loads(response.text)
    print(ssh_keys_data)

    ssh_key_id_map = {}

    ssh_ids = []
    count = 0

    for ssh_key in ssh_keys_data['ssh_keys']:
        ssh_ids.append(f'ID: {ssh_key["id"]}, Key Name: {ssh_key["name"]}')
        ssh_key_id_map[count] = ssh_key
        count += 1
    
    terminal_menu = TerminalMenu(
        ssh_ids,
        multi_select=True,
        show_multi_select_hint=True,
    )

    choice = terminal_menu.show()
    print(choice)
