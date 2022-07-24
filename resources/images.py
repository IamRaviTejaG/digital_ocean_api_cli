import json

import requests
from config.constants import (DIGITAL_OCEAN_API_HEADERS,
                              DIGITAL_OCEAN_IMAGES_URL,
                              IMAGE_SLUGS_FIELD_NAMES)
from utils.printer import print_table


def get_images():
    images_url = f"{DIGITAL_OCEAN_IMAGES_URL}?page=1&per_page=1000"
    response = requests.request("GET", images_url, headers=DIGITAL_OCEAN_API_HEADERS)
    images_data = json.loads(response.text)
    return images_data['images']

def view_image_slugs():
    images = get_images()

    rows = []

    for image in images:
        row = []
        row.append(image['id'])
        row.append(image['name'])
        row.append(image['distribution'])
        row.append(image['slug'])
        row.append(image['type'])
        row.append(image['public'])
        row.append(image['status'])
        row.append(image['error_message'] or 'NA')
        rows.append(row)

    print_table(IMAGE_SLUGS_FIELD_NAMES, rows)
