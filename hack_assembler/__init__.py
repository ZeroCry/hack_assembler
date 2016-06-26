import os
from . import symbol_table as symbol_table_module
from .parser import parse
from .translator import translate


def assemble(lines):
    symbol_table = symbol_table_module.init()
    parsed_lines = parse(lines, symbol_table)
    machine_code = translate(parsed_lines, symbol_table)
    return os.linesep.join(machine_code)
