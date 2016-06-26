import sys
import os
import hack_assembler


def main(args=sys.argv):
    inputfile = _get_inputfile(args)
    if inputfile:
        with open(inputfile, 'r') as f:
            print(hack_assembler.assemble(f.read()))


def _get_inputfile(args):
    if len(args) != 2:
        print('usage: hack-assembler inputfile')
        return False

    inputfile = args[1]
    if not os.path.isfile(inputfile):
        print('hack-assembler: '+inputfile+': No such file or directory')
        return False

    return inputfile


if __name__ == '__main__':
    main()
