import io
import os
from contextlib import redirect_stdout
from nose.tools import assert_equal
from .. import cli


def test_no_arguments():
    actual = _run_cli([]).strip()
    expected = 'usage: hack-assembler inputfile'
    assert_equal(actual, expected)


def test_invalid_inputfile():
    actual = _run_cli(['', './invalid_file.asm']).strip()
    expected = 'hack-assembler: ./invalid_file.asm: No such file or directory'
    assert_equal(actual, expected)


def test_valid_inputfiles():
    for program in ['Add', 'MaxL', 'RectL', 'PongL', 'Max', 'Rect', 'Pong']:
        yield _check_output, program


def _check_output(program):
    actual = _run_cli(['', _get_examples_path(program + '.asm')])

    with open(_get_examples_path(program + '.hack')) as f:
        expected = f.read()

    assert_equal(actual, expected)


def _run_cli(args):
    my_stdout = io.StringIO()
    with redirect_stdout(my_stdout):
        cli.main(args)
    return my_stdout.getvalue()


def _get_examples_path(program):
    dirname = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(dirname, 'examples', program)
