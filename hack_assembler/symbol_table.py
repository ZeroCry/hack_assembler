import re


def init():
    return {
        'R0': 0, 'R5': 5, 'R10': 10, 'R15':  15, 'THAT':   4,
        'R1': 1, 'R6': 6, 'R11': 11, 'SP':   0,  'SCREEN': 16384,
        'R2': 2, 'R7': 7, 'R12': 12, 'LCL':  1,  'KBD':    24576,
        'R3': 3, 'R8': 8, 'R13': 13, 'ARG':  2,
        'R4': 4, 'R9': 9, 'R14': 14, 'THIS': 3,
    }


def get(symbol, table):
    return table[symbol]


def add(symbol, address, table):
    table[symbol] = address
    return table


def add_var(var, table):
    _increment_var_counter(table)
    return add(var, table[None] + 16, table)


def _increment_var_counter(table):
    if None in table:
        table[None] = table[None] + 1
    else:
        table[None] = 0


def get_var(var, symbol_table):
    if var not in symbol_table:
        add_var(var, symbol_table)
    return get(var, symbol_table)
