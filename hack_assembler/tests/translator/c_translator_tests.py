from nose.tools import assert_equal
from ...translator.c_translator import translate


def test_compute():
    assert_equal(translate('D=M'),   '1111110000010000')
    assert_equal(translate('D=D-M'), '1111010011010000')
    assert_equal(translate('D;JGT'), '1110001100000001')
    assert_equal(translate('0;JMP'), '1110101010000111')
