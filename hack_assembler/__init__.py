import os
from . import symbol_table as symbol_table_module
from .parser import parse
from .translator import translate


def assemble(asm_input):
    symbol_table = symbol_table_module.init()
    instructions = parse(asm_input, symbol_table)
    machine_code = translate(instructions, symbol_table)
    return os.linesep.join(machine_code)
