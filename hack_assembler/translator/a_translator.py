import re
from .. import symbol_table as symbol_table_module


def translate(line, symbol_table={}):
    addr = _extract_addr(line)
    if _is_var(addr):
        addr = symbol_table_module.get_var(addr, symbol_table)
    return _addr(addr)


def _extract_addr(line):
    return line[1:]


def _is_var(ref):
    return re.compile('\D+').match(ref)


def _addr(addr):
    return '{:016b}'.format(int(addr))
