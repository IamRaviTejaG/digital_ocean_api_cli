# Logic for listing droplets

import json

import requests
from config.constants import (DIGITAL_OCEAN_API_BASE_URL,
                              DIGITAL_OCEAN_API_HEADERS,
                              DROPLET_VIEW_FIELD_NAMES)
from utils.droplet_filters import get_network_ipv4_public
from utils.printer import print_table


def get_droplets():
    droplets_url = f"{DIGITAL_OCEAN_API_BASE_URL}/droplets"
    response = requests.request("GET", droplets_url, headers=DIGITAL_OCEAN_API_HEADERS)
    droplets_data = json.loads(response.text)
    return droplets_data['droplets']

def view_droplets():
    droplets = get_droplets()

    if (len(droplets) == 0):
        print("No droplets found!")
        return

    rows = []

    for droplet in droplets:
        row = []
        row.append(droplet['id'])
        row.append(get_network_ipv4_public(droplet['networks']))
        row.append(droplet['name'])
        row.append(droplet['created_at'])
        row.append(droplet['status'])
        row.append(droplet['image']['distribution'])
        row.append(droplet['image']['id'])
        row.append(droplet['image']['slug'])
        row.append(droplet['size']['slug'])
        row.append(droplet['region']['slug'])
        row.append(','.join(droplet['tags']))
        row.append(droplet['vpc_uuid'])
        rows.append(row)

    print_table(DROPLET_VIEW_FIELD_NAMES, rows)

def get_droplet_id_ip():
    droplets = get_droplets()
    ips = {}

    for droplet in droplets:
        droplet_details = get_droplet_fields(droplet, 'id', 'ip')
        ips[droplet_details['id']] = droplet_details['ip']

    return ips

def get_droplet_fields(droplet_object, *args):
    droplet_details = {}

    if 'id' in args:
        droplet_details['id'] = droplet_object['id']
    if 'ip' in args:
        droplet_details['ip'] = get_network_ipv4_public(droplet_object['networks'])
    if 'name' in args:
        droplet_details['name'] = droplet_object['name']
    if 'region' in args:
        droplet_details['region'] = droplet_object['region']['slug']
    if 'imgslug' in args:
        droplet_details['imgslug'] = droplet_object['image']['slug']
    if 'imgid' in args:
        droplet_details['imgid'] = droplet_object['image']['id']
    if 'dist' in args:
        droplet_details['distribution'] = droplet_object['image']['distribution']
    if 'sizeslug' in args:
        droplet_details['sizeslug'] = droplet_object['size']['slug']
    if 'status' in args:
        droplet_details['status'] = droplet_object['status']
    if 'created_at' in args:
        droplet_details['created_at'] = droplet_object['created_at']
    if 'tags' in args:
        droplet_details['tags'] = ','.join(droplet_object['tags'])
    if 'vpc' in args:
        droplet_details['vpc_uuid'] = droplet_object['vpc_uuid']
    
    return droplet_details
