import random
import argparse

parser = argparse.ArgumentParser(description='')
parser.add_argument('filename')
parser.add_argument('-s', '--show', action="store_true", default=False)
parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.0')
args = parser.parse_args()


if __name__ == '__main__':
    print args 
    f = open(args.filename)
    line = f.readline()
    if args.show:
        while line:
            print line
            line = f.readline()
    else:

        while line:
            print '   ' + line
            raw_input('>  ')
            line = f.readline()
            print '-----------------------------------------------------------------------------------'
        f.close

