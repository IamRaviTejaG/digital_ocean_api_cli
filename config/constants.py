# Contains all the constants required throughout the project.

DIGITAL_OCEAN_API_KEY = 'DIGITAL_OCEAN_API_KEY'

DIGITAL_OCEAN_API_BASE_URL = "https://api.digitalocean.com/v2"

DIGITAL_OCEAN_API_HEADERS = {
  'Content-Type': 'application/json',
  'Authorization': f'Bearer {DIGITAL_OCEAN_API_KEY}'
}

DIGITAL_OCEAN_DROPLETS_URL = f"{DIGITAL_OCEAN_API_BASE_URL}/droplets"
DIGITAL_OCEAN_IMAGES_URL = f"{DIGITAL_OCEAN_API_BASE_URL}/images"
DIGITAL_OCEAN_REGIONS_URL = f"{DIGITAL_OCEAN_API_BASE_URL}/regions"
DIGITAL_OCEAN_SIZES_URL = f"{DIGITAL_OCEAN_API_BASE_URL}/sizes"
DIGITAL_OCEAN_SSH_KEYS_URL = f"{DIGITAL_OCEAN_API_BASE_URL}/account/keys"

DROPLET_VIEW_FIELD_NAMES = ["ID", "IP", "Name", "Created", "Status", "ImgDist", "ImgID", "ImgSlug", "SizeSlug", "RegionSlug", "Tags", "VPC UUID"]
IMAGE_SLUGS_FIELD_NAMES = ["ID", "Name", "Distribution", "Slug", "Type", "Public", "Status", "Error Message"]
REGION_SLUGS_FIELD_NAMES = ["Name", "Slug", "Availability", "Features"]
SIZE_SLUGS_FIELD_NAMES = ["Slug", "Description", "Mem (MB)", "vCPUs", "Disk", "Network", "Price ($/Hour)", "Price ($/Month)", "Available", "Regions"]

MENU_OPTIONS = ["Create droplet(s)", "Delete droplet(s)", "View droplet(s)", "View image slugs", "View region slugs", "View size slugs", "Exit"]
