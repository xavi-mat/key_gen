#! /usr/bin/python3

"""
Key generator.

Generates secure formated keys. Can be used to unlock elements in apps and
games, like 'External Keys' on itch.io. Uses a sequence of numbers and letters
without confusing characters: 1,I,i,0,O,o.
"""


__version__ = "1.1"
__author__ = "Xavimat"
__date__ = "2023-06-26"


import argparse
import secrets


# CONSTANTS AND FUNCTIONS:

# 32 characters:
# seq32 = "23456789ABCDEFGHJKLMNPQRSTUVWXYZ"
# 56 characters:
SEQ = "23456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghjklmnpqrstuvwxyz"


def gen_a_key(blocks=3, chars=5, length=32):
    """
    Generate a key with given values.

    - blocks: int, number of hyphen-separated blocks.
    - chars: int, number of characters per block.
    - length: int, number of elegible characters.
    """

    if length <= 56:
        seq = SEQ[:length]
    else:
        raise ValueError("Sequence too large (max 56).")

    r = ""

    for i1 in range(blocks):

        for i2 in range(chars):

            r += secrets.choice(seq)

        r += "-"

    return r[:-1]


def key_gen(blocks=3, chars=5, length=32, keys=1000, filename="keys.txt"):
    """
    Output a text file with the given number of keys.

    - blocks: int, number of hyphen-separated blocks per key.
    - chars: int, number of characters per block per key.
    - length: int, number of elegible characters.
    - keys: int, total of generated keys.
    - filename: str, name of file with one key per line.
    """

    # Generate, avoiding repetition
    keys_set = set([gen_a_key(blocks, chars, length) for _ in range(keys)])

    while len(keys_set) < keys:

        keys_set.add(gen_a_key(blocks, chars, length))

    with open(filename, "w") as t:

        for k in keys_set:

            t.write(k + "\n")


# PARSING ARGUMENTS:

_parser = argparse.ArgumentParser()

_parser.add_argument("-b", type=int,
    help="number of character-blocks per key (default 3)", default=3)
_parser.add_argument("-c", type=int,
    help="number of characters per block (default 5)", default=5)
_parser.add_argument("-f",
    help="filename to output (default keys.txt)", default="keys.txt")
_parser.add_argument("-k", type=int,
    help="number of generated keys (default 1000)", default=1000)
_parser.add_argument("-l", type=int,
    help="number of random characters (recomended 32, max 56)", default=32)


# EXECUTE:
if __name__ == '__main__':

    args = _parser.parse_args()

    blocks = args.b
    chars = args.c
    filename = args.f
    keys = args.k
    length = args.l

    key_gen(blocks, chars, length, keys, filename)
