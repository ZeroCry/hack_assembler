import re
from . import a_translator, c_translator


def translate(lines, symbol_table):
    machine_code = []
    for line in lines:
        if _instruction_type(line) == 'a':
            code = a_translator.translate(line, symbol_table)
        else:
            code = c_translator.translate(line)
        machine_code.append(code)
    return machine_code


def _instruction_type(line):
    return 'a' if re.compile('^@').match(line) else 'c'
