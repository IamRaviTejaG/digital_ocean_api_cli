# Handles droplet creation

import json

import requests
from config.constants import (DIGITAL_OCEAN_API_BASE_URL,
                              DIGITAL_OCEAN_API_HEADERS)


def __create_droplets(names, region_slug, size_slug, image_slug):
    droplets = {
        "names": names,
        "region": region_slug,
        "size": size_slug,
        "image": image_slug,
    }

    droplets_url = f"{DIGITAL_OCEAN_API_BASE_URL}/droplets"
    response = requests.request("POST", droplets_url, headers=DIGITAL_OCEAN_API_HEADERS, json=droplets)

    if (response.status_code == 202):
        droplets_data = json.loads(response.text)
        print(droplets_data)
    elif (response.status_code == 401):
        print('Authorization error')
    elif (response.status_code == 429):
        print('API Rate Limit exceeded')
    elif (response.status_code == 500):
        print('Server side error')
    else:
        print(json.loads(response.text))

def create_droplets_selector():
    droplet_count = int(input("How many droplets do you want to create?\nEnter: "))
    names = []
    count = 1
    while (count <= droplet_count):
        name = str(input(f"Insert name for droplet #{count}: "))
        names.append(name)
        count += 1

    region_slug = str(input("Enter region slug: "))
    size_slug = str(input("Enter size slug: "))
    image_slug = str(input("Enter image slug: "))

    __create_droplets(names, region_slug, size_slug, image_slug)
