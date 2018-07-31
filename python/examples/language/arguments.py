import argparse
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default=1.0, help='What is the first number?')
    parser.add_argument('--y', type=float, default=1.0, help='What is the second number?')
    parser.add_argument('--o', type=str, default='add', help='What operation? (add, sub, mul, or div)')
    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))


def calc(args):
    if args.o == 'add':
        return args.x + args.y
    elif args.o == 'sub':
        return args.x - args.y
    elif args.o == 'mul':
        return args.x * args.y
    elif args.o == 'div':
        return args.x / args.y


if __name__ == '__main__':
    main()
