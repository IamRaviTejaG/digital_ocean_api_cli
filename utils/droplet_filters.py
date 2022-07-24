# Contains custom filters for filtering droplets based on a specific condition

def get_network_ipv4_public(network):
    """
    Expects an object similar to this. Would break otherwise, please exercise
    caution while changing this.

    {
        "v4": [
            {
                "ip_address": "143.110.186.175",
                "netmask": "255.255.240.0",
                "gateway": "143.110.176.1",
                "type": "public"
            },
            {
                "ip_address": "10.122.0.2",
                "netmask": "255.255.240.0",
                "gateway": "10.122.0.1",
                "type": "private"
            }
        ],
        "v6": []
    }
    """

    ipv4 = 'NA'

    if 'v4' in network:
        public_ipv4 = list(filter(__get_public_ipv4, network['v4']))
        ipv4 = public_ipv4[0]['ip_address']
    
    return ipv4

def __get_public_ipv4(ipv4_network_object):
    return ipv4_network_object['type'] == 'public'
