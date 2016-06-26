import os
from nose.tools import assert_equal
from .. import assemble


def test_assemble():
    actual = assemble('@2' + os.linesep + 'D=M')
    expected = '0000000000000010' + os.linesep + '1111110000010000'
    assert_equal(actual, expected)
