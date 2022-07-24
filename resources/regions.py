import json

import requests
from config.constants import (DIGITAL_OCEAN_API_BASE_URL,
                              DIGITAL_OCEAN_API_HEADERS, DIGITAL_OCEAN_REGIONS_URL,
                              REGION_SLUGS_FIELD_NAMES)
from utils.printer import print_table


def get_regions():
    regions_url = f"{DIGITAL_OCEAN_REGIONS_URL}?page=1&per_page=1000"
    response = requests.request("GET", regions_url, headers=DIGITAL_OCEAN_API_HEADERS)
    regions_data = json.loads(response.text)
    return regions_data['regions']

def get_active_regions():
    all_regions = get_regions()
    active_regions = [region for region in all_regions if region['available'] == True]
    return active_regions

def view_region_slugs():
    regions = get_regions()

    rows = []

    for region in regions:
        row = []
        row.append(region['name'])
        row.append(region['slug'])
        row.append(region['available'])
        row.append(','.join(region['features']))
        rows.append(row)
    
    print_table(REGION_SLUGS_FIELD_NAMES, rows)
