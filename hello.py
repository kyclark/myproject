#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2024-11-15
Purpose: Rock the Casbah
"""

import argparse
from typing import NamedTuple


class Args(NamedTuple):
    """ Command-line arguments """
    name: str


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('name',
                        metavar='NAME',
                        help='Your name')

    args = parser.parse_args()

    return Args(args.name)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()
    print(f'Hello, {args.name}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
