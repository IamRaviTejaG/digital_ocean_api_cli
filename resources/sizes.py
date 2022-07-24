import json

import requests
from config.constants import (DIGITAL_OCEAN_API_BASE_URL,
                              DIGITAL_OCEAN_API_HEADERS, DIGITAL_OCEAN_SIZES_URL,
                              SIZE_SLUGS_FIELD_NAMES)
from utils.printer import print_table


def get_sizes():
    sizes_url = f"{DIGITAL_OCEAN_SIZES_URL}?page=1&per_page=1000"
    response = requests.request("GET", sizes_url, headers=DIGITAL_OCEAN_API_HEADERS)
    sizes_data = json.loads(response.text)
    return sizes_data['sizes']

def view_size_slugs():
    sizes = get_sizes()

    rows = []

    for size in sizes:
        row = []
        row.append(size['slug'])
        row.append(size['description'])
        row.append(size['memory'])
        row.append(size['vcpus'])
        row.append(size['disk'])
        row.append(size['transfer'])
        row.append(size['price_hourly'])
        row.append(size['price_monthly'] if int(size['price_monthly']) != float(size['price_monthly']) else int(size['price_monthly']))
        row.append(size['available'])
        row.append(','.join(size['regions']))
        rows.append(row)
    
    print_table(SIZE_SLUGS_FIELD_NAMES, rows)
