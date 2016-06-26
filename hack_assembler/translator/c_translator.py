def translate(line):
    comp, dest, jump = _extract_line_parts(line)
    return '111' + _comp(comp) + _dest(dest) + _jump(jump)


def _extract_line_parts(line):
    if '=' in line:
        dest, comp = line.split('=')
        return (comp, dest, None)
    else:
        comp, jump = line.split(';')
        return (comp, None, jump)


def _comp(comp):
    return {
        '0':  '0101010', '-D':  '0001111', 'D-A': '0010011', 'M+1': '1110111',
        '1':  '0111111', '-A':  '0110011', 'A-D': '0000111', 'M-1': '1110010',
        '-1': '0111010', 'D+1': '0011111', 'D&A': '0000000', 'D+M': '1000010',
        'D':  '0001100', 'A+1': '0110111', 'D|A': '0010101', 'D-M': '1010011',
        'A':  '0110000', 'D-1': '0001110', 'M':   '1110000', 'M-D': '1000111',
        '!D': '0001101', 'A-1': '0110010', '!M':  '1110001', 'D&M': '1000000',
        '!A': '0110001', 'D+A': '0000010', '-M':  '1110011', 'D|M': '1010101',
    }[comp]


def _dest(dest):
    return {
        None: '000', 'A':   '100',
        'M':  '001', 'AM':  '101',
        'D':  '010', 'AD':  '110',
        'MD': '011', 'AMD': '111',
    }[dest]


def _jump(jump):
    return {
        None:  '000', 'JLT': '100',
        'JGT': '001', 'JNE': '101',
        'JEQ': '010', 'JLE': '110',
        'JGE': '011', 'JMP': '111',
    }[jump]
