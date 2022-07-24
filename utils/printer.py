# Printing utility methods reside here

from typing import Any, List

from prettytable import PrettyTable


def print_table(field_names: List[str], rows: List[List[Any]]) -> None:
    x = PrettyTable()
    x.field_names = field_names
    for row in rows:
        x.add_row(row)

    print(x)
