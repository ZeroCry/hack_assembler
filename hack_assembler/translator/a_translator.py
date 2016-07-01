import re
from .. import symbol_table as symbol_table_module


def translate(instruction, symbol_table={}):
    addr = _extract_addr(instruction)
    if _is_var(addr):
        addr = symbol_table_module.get_var(addr, symbol_table)
    return _addr(addr)


def _extract_addr(instruction):
    return instruction[1:]  # removing the @ sign in front of it


def _is_var(addr):
    return re.compile('\D+').match(addr)


def _addr(addr):
    return '{:016b}'.format(int(addr))
