# Generates terminal menu based on the given inputs

from typing import Any, List, Optional
from simple_term_menu import TerminalMenu

def generate_menu(menu_options: List[str],
                  title: Optional[Any] = None,
                  multi: Optional[Any] = False,
                  search_key: Optional[Any] = None,
                  search_preview_text: Optional[Any] = False) -> Any:
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
