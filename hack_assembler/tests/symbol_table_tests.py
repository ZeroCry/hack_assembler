from nose.tools import assert_equal
from .. import symbol_table


def test_predefined_symbols():
    expected_predefined_symbols = [
        ('R0', 0), ('R5', 5), ('R10', 10), ('R15',  15), ('THAT',   4),
        ('R1', 1), ('R6', 6), ('R11', 11), ('SP',   0),  ('SCREEN', 16384),
        ('R2', 2), ('R7', 7), ('R12', 12), ('LCL',  1),  ('KBD',    24576),
        ('R3', 3), ('R8', 8), ('R13', 13), ('ARG',  2),
        ('R4', 4), ('R9', 9), ('R14', 14), ('THIS', 3),
    ]
    for entry in expected_predefined_symbols:
        yield _check_entry, entry[0], entry[1]


def _check_entry(key, value):
    assert_equal(symbol_table.get(key, symbol_table.init()), value)


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
