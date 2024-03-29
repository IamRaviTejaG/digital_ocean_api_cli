# Deletion logic for droplets

from typing import List

import requests
from config.constants import (DIGITAL_OCEAN_API_HEADERS,
                              DIGITAL_OCEAN_DROPLETS_URL)
from config.http_status import HttpStatus
from utils.menu_generator import generate_menu

from .view import get_droplet_fields, get_droplets


def delete_droplet_selector():
    droplets = get_droplets()

    if (len(droplets) == 0):
        print("No droplets found!")
        return

    option_droplet_id_map = {}

    droplets_list = []

    count = 0
    for droplet in droplets:
        droplet_details = get_droplet_fields(droplet, 'id', 'ip', 'name', 'region')
        details = f"ID: {droplet_details['id']}, IP: {droplet_details['ip']}, Name: {droplet_details['name']}, Region: {droplet_details['region']}"
        droplets_list.append(details)
        option_droplet_id_map[count] = droplet_details
        count += 1

    choices = generate_menu(droplets_list, title="Select droplets to delete", multi=True, search_key=False)
    droplets_to_delete = [option_droplet_id_map[choice] for choice in choices]
    __delete_droplets(droplets_to_delete)

def __delete_droplets(droplets_to_delete: List[dict]) -> None:
    for droplet in droplets_to_delete:
        s1 = "Do you want to delete droplet?"
        s2 = f"ID: {droplet['id']}, IP: {droplet['ip']}, Name: {droplet['name']}, Region: {droplet['region']}"
        s3 = "Enter Y/N: "
        res = str(input(f"{s1}\n\nDetails:\n{s2}\n\n{s3}"))

        if (res.lower() in ['y', 'yes']):
            delete_droplet_url = f"{DIGITAL_OCEAN_DROPLETS_URL}/{droplet['id']}"
            response = requests.request("DELETE", delete_droplet_url, headers=DIGITAL_OCEAN_API_HEADERS)
            if (response.status_code == HttpStatus.NO_CONTENT):
                print(f"Successfully deleted droplet. ID: {droplet['id']}\n")
            else:
                print(f"Failed to delete droplet. ID: {droplet['id']}\n")
        else:
            print(f"Skipped deleting data for ID: {droplet['id']}\n")
