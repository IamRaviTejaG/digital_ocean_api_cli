# Printing utility methods reside here

from prettytable import PrettyTable


def print_table(field_names, rows):
    x = PrettyTable()
    x.field_names = field_names
    for row in rows:
        x.add_row(row)

    print(x)
