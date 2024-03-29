# Driver to handle the Digital Ocean API -> CLI utility

from config.constants import MENU_OPTIONS
from droplet.create import create_droplets_selector
from droplet.delete import delete_droplet_selector
from droplet.view import view_droplets
from resources.images import view_image_slugs
from resources.regions import view_region_slugs
from resources.sizes import view_size_slugs
from utils.menu_generator import generate_menu


def main():
    method_choice_map = {
        0: create_droplets_selector,
        1: delete_droplet_selector,
        2: view_droplets,
        3: view_image_slugs,
        4: view_region_slugs,
        5: view_size_slugs
    }

    choice = generate_menu(MENU_OPTIONS, title="Select option", multi=False)

    if (choice == 6):
        exit()
    else:
        method_choice_map[choice]()
        print('\n\n')
        main()


if __name__ == '__main__':
    main()
