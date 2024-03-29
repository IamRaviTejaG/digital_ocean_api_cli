# Handles droplet creation

import json
from typing import Any, List

import requests
from config.constants import (DIGITAL_OCEAN_API_HEADERS,
                              DIGITAL_OCEAN_DROPLETS_URL,
                              DROPLET_VIEW_FIELD_NAMES)
from config.http_status import HttpStatus
from resources.images import get_images
from resources.regions import get_active_regions
from resources.sizes import get_sizes
from resources.ssh_keys import get_user_ssh_keys
from utils.menu_generator import generate_menu
from utils.printer import print_table
from utils.view_droplet_utils import get_views_table_rows


def create_droplets_selector():
    droplet_count = int(input("How many droplets do you want to create?\nEnter: "))

    names = []
    count = 1
    while (count <= droplet_count):
        name = str(input(f"Insert name for droplet #{count}: "))
        names.append(name)
        count += 1

    # Select image slug menu
    images = get_images()
    img_slugs_list = [img['slug'] for img in images]
    img_slug_idx = generate_menu(img_slugs_list, title="Select image slug", search_preview_text=True)
    image_slug = img_slugs_list[img_slug_idx]
    print(f'Selected image slug: {image_slug}')

    # Select region slug menu
    regions = get_active_regions()
    region_slugs = [region['slug'] for region in regions]
    region_slugs_list = [f"{region['slug']} ({region['name']})" for region in regions]
    region_slug_idx = generate_menu(region_slugs_list, title="Select region slug", search_preview_text=True)
    region_slug = region_slugs[region_slug_idx]
    print(f'Selected region slug: {region_slug}')

    # Select size slug menu
    sizes = get_sizes()
    size_slugs_list = [size['slug'] for size in sizes]
    size_slugs_idx = generate_menu(size_slugs_list, title="Select size slug", search_preview_text=True)
    size_slug = size_slugs_list[size_slugs_idx]
    print(f'Selected size slug: {size_slug}')

    # Select SSH key menu
    ssh_keys = get_user_ssh_keys()
    ssh_keys_list = [f'ID: {key["id"]}, Name: {key["name"]}' for key in ssh_keys]
    choices = generate_menu(
        ssh_keys_list,
        title="Select SSH keys to enable access to droplets",
        multi=True,
        search_key=False,
        search_preview_text=False)

    ssh_key_ids = [ssh_keys[choice]['id'] for choice in choices]
    ssh_key_ids_str = [str(x) for x in ssh_key_ids]
    print(f'Selected SSH keys with access to droplets: {", ".join(ssh_key_ids_str)}')

    # Proceed to create droplet
    __create_droplets(
        names,
        image_slug,
        region_slug,
        size_slug,
        ssh_key_ids
    )

def __create_droplets(names: List[str], image_slug: str, region_slug: str,
                      size_slug: str, ssh_keys: List[Any]) -> None:
    droplets = {
        "names": names,
        "region": region_slug,
        "size": size_slug,
        "image": image_slug,
        "ssh_keys": ssh_keys
    }

    response = requests.request("POST", DIGITAL_OCEAN_DROPLETS_URL, 
                                headers=DIGITAL_OCEAN_API_HEADERS,
                                json=droplets)

    if (response.status_code == HttpStatus.ACCEPTED):
        droplets_data = json.loads(response.text)
        print_table(DROPLET_VIEW_FIELD_NAMES, get_views_table_rows(droplets_data['droplets']))
    elif (response.status_code == HttpStatus.UNAUTHORIZED):
        print('Authorization error')
    elif (response.status_code == HttpStatus.TOO_MANY_REQUESTS):
        print('API Rate Limit exceeded')
    elif (response.status_code == HttpStatus.INTERNAL_SERVER_ERROR):
        print('Server side error')
    else:
        print(json.loads(response.text))
