from nose.tools import assert_equal
from .. import symbol_table


def test_predefined_symbols():
    my_table = symbol_table.init()
    assert_equal(symbol_table.get('R0',     my_table), 0)
    assert_equal(symbol_table.get('R1',     my_table), 1)
    assert_equal(symbol_table.get('R2',     my_table), 2)
    assert_equal(symbol_table.get('R3',     my_table), 3)
    assert_equal(symbol_table.get('R4',     my_table), 4)
    assert_equal(symbol_table.get('R5',     my_table), 5)
    assert_equal(symbol_table.get('R6',     my_table), 6)
    assert_equal(symbol_table.get('R7',     my_table), 7)
    assert_equal(symbol_table.get('R8',     my_table), 8)
    assert_equal(symbol_table.get('R9',     my_table), 9)
    assert_equal(symbol_table.get('R10',    my_table), 10)
    assert_equal(symbol_table.get('R11',    my_table), 11)
    assert_equal(symbol_table.get('R12',    my_table), 12)
    assert_equal(symbol_table.get('R13',    my_table), 13)
    assert_equal(symbol_table.get('R14',    my_table), 14)
    assert_equal(symbol_table.get('R15',    my_table), 15)
    assert_equal(symbol_table.get('SP',     my_table), 0)
    assert_equal(symbol_table.get('LCL',    my_table), 1)
    assert_equal(symbol_table.get('ARG',    my_table), 2)
    assert_equal(symbol_table.get('THIS',   my_table), 3)
    assert_equal(symbol_table.get('THAT',   my_table), 4)
    assert_equal(symbol_table.get('SCREEN', my_table), 16384)
    assert_equal(symbol_table.get('KBD',    my_table), 24576)


def test_add():
    actual = symbol_table.add('LOOP', 2, {})
    expected = {'LOOP': 2}
    assert_equal(actual, expected)


def test_add_var():
    my_table = {'LOOP': 23}
    symbol_table.add_var('foo', my_table)
    symbol_table.add_var('bar', my_table)
    symbol_table.add_var('baz', my_table)

    assert_equal(symbol_table.get('foo', my_table), 16)
    assert_equal(symbol_table.get('bar', my_table), 17)
    assert_equal(symbol_table.get('baz', my_table), 18)


def test_get_undeclared_var():
    actual = symbol_table.get_var('foo', {})
    expected = 16
    assert_equal(actual, expected)
