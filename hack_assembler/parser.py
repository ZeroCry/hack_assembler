import os
import re
from . import symbol_table as symbol_table_module


def parse(asm_input, symbol_table=symbol_table_module.init()):
    instructions = []

    for line in asm_input.split(os.linesep):

        line = _remove_comments(line)
        line = _remove_spaces(line)

        # empty line produces no instruction to the machine.
        if not line:
            continue

        # label is a pseudo-command, it also produces no instruction to the
        # machine, just an entry on the symbol table.
        elif _is_label(line):
            _extract_label(len(instructions), line, symbol_table)

        else:
            instructions.append(line)

    return instructions


def _remove_comments(line):
    comment_index = line.find('//')
    return line[:comment_index] if comment_index > -1 else line


def _remove_spaces(line):
    return line.replace(' ', '').strip()


def _is_label(line):
    return re.compile('^\(').match(line)


def _extract_label(index, line, symbol_table):
    label = line[1:-1]  # removing parentheses around the label.
    symbol_table_module.add(label, index, symbol_table)
