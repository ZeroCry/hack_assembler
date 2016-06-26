import os
from nose.tools import assert_equal
from .. import assemble


def test_multiple_lines():
    asm = [
        '@2',
        'D=A',
        '@3',
        'D=D+A',
        '@0',
        'M=D'
    ]
    hack = [
        '0000000000000010',
        '1110110000010000',
        '0000000000000011',
        '1110000010010000',
        '0000000000000000',
        '1110001100001000'
    ]
    actual = assemble(os.linesep.join(asm))
    expected = os.linesep.join(hack)
    assert_equal(actual, expected)
