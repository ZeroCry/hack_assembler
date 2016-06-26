import os
from nose.tools import assert_equal
from ..parser import parse
from .. import symbol_table as symbol_table_module


def test_removal_of_comments_entire_line():
    actual = parse('//nocode')
    expected = []
    assert_equal(actual, expected)


def test_removal_of_comments_mixed_with_valid_instructions():
    actual = parse('@2//address')
    expected = ['@2']
    assert_equal(actual, expected)


def test_removal_of_spaces():
    actual = parse('	D = D + A')
    expected = ['D=D+A']
    assert_equal(actual, expected)


def test_multiple_lines():
    actual = parse('@2' + os.linesep + 'D=A' + os.linesep + '@3')
    expected = ['@2', 'D=A', '@3']
    assert_equal(actual, expected)


def test_removal_of_empty_lines():
    actual = parse(os.linesep + os.linesep + os.linesep)
    expected = []
    assert_equal(actual, expected)


def test_extraction_of_labels():
    symbol_table = {}
    parsed_lines = parse('@R1' + os.linesep + '(LOOP)', symbol_table)

    actual = (parsed_lines, symbol_table)
    expected = (['@R1'], {'LOOP': 1})
    assert_equal(actual, expected)
