from typing import Any, List

from .droplet_filters import get_network_ipv4_public


def get_views_table_rows(droplets: List[dict]) -> List[List[Any]]:
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

        # Special case for `vpc_uuid`, missing in newly created droplets
        if 'vpc_uuid' in droplet:
            row.append(droplet['vpc_uuid'])
        else:
            row.append('NA')

        rows.append(row)
    
    return rows
