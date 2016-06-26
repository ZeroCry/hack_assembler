from nose.tools import assert_equal
from ...translator.a_translator import translate


def test_constant():
    actual = translate('@1024', {})
    expected = '0000010000000000'
    assert_equal(actual, expected)


def test_symbol():
    actual = translate('@a_symbol', {'a_symbol': 16})
    expected = '0000000000010000'
    assert_equal(actual, expected)
