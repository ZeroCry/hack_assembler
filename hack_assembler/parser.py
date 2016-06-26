import os
import re
from . import symbol_table as symbol_table_module


def parse(lines, symbol_table=symbol_table_module.init()):
    parsed_lines = []

    for line in lines.split(os.linesep):

        line = _remove_comments(line)
        line = _remove_spaces(line)

        # empty lines produce no machine code.
        if not line:
            continue

        # labels are pseudo-commands, they also produce no machine code,
        # just an entry on the symbol table.
        elif _is_label(line):
            _extract_label(len(parsed_lines), line, symbol_table)

        else:
            parsed_lines.append(line)

    return parsed_lines


def _remove_comments(line):
    comment_index = line.find('//')
    return line[:comment_index] if comment_index > -1 else line


def _remove_spaces(line):
    return line.replace(' ', '').strip()


def _is_label(line):
    return re.compile('^\(').match(line)


def _extract_label(index, line, symbol_table):
    label = line[1:-1]
    symbol_table_module.add(label, index, symbol_table)
