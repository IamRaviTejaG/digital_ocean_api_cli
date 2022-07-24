from simple_term_menu import TerminalMenu

def generate_menu(menu_options, title=None, multi=False, search_key=None, search_preview_text=False):
    menu = TerminalMenu(
        menu_options,
        title=title,
        multi_select=multi,
        show_multi_select_hint=True,
        search_key=search_key,
        show_search_hint=search_preview_text
    )

    choice = menu.show()

    return choice
