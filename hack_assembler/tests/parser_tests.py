import os
from nose.tools import assert_equal
from ..parser import parse
from .. import symbol_table as symbol_table_module


def test_removal_of_comments():
    actual = parse('//nocode'+os.linesep+'@2//address')
    expected = ['@2']
    assert_equal(actual, expected)


def test_removal_of_spaces():
    actual = parse('	D = D + A')
    expected = ['D=D+A']
    assert_equal(actual, expected)


def test_removal_of_empty_lines():
    actual = parse(os.linesep + os.linesep + os.linesep)
    expected = []
    assert_equal(actual, expected)


def test_extraction_of_labels():
    actual_symbol_table = {}
    actual_parsing = parse('@R1'+os.linesep+'(LOOP)', actual_symbol_table)

    expected_symbol_table = {'LOOP': 1}
    expected_parsing = ['@R1']

    assert_equal(actual_symbol_table, expected_symbol_table)
    assert_equal(actual_parsing, expected_parsing)
