import re


def init():
    """
    Initializes a symbol table with all predefined symbols.
    Page 110 of http://nand2tetris.org/chapters/chapter%2006.pdf
    """
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


def get_var(var, symbol_table):
    if var not in symbol_table:
        add_var(var, symbol_table)
    return get(var, symbol_table)


def add_var(var, table):
    return add(var, _use_free_addr_for_var(table), table)


def _use_free_addr_for_var(table):
    """
    free_addr_for_var is used to keep track of which memory address can be
    used by a variable. This key is a tuple instead of a string to prevent
    a possible override.
    """
    if ('free_addr_for_var') in table:
        table[('free_addr_for_var')] = table[('free_addr_for_var')] + 1
    else:
        table[('free_addr_for_var')] = 16  # vars should start at addr 16

    return table[('free_addr_for_var')]
