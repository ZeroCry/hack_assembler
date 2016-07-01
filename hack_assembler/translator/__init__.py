import re
from . import a_translator, c_translator


def translate(instructions, symbol_table):
    machine_code = []

    for instruction in instructions:
        if _instruction_type(instruction) == 'a':
            code = a_translator.translate(instruction, symbol_table)
        else:
            code = c_translator.translate(instruction)
        machine_code.append(code)

    return machine_code


def _instruction_type(line):
    """
    Addressing instructions start with an @ sign, everything else is a compute
    instruction.
    """
    return 'a' if re.compile('^@').match(line) else 'c'
