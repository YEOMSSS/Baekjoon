"""
import sys

input = sys.stdin.readline

import binascii


def main():
    while True:
        hex_string = input().rstrip()
        if not hex_string:
            return
        bytes_data = binascii.unhexlify(hex_string)
        string_data = bytes_data.decode("utf-8")

        print(string_data)


main()
"""

import sys

input = sys.stdin.readline


def main():
    while True:
        string = input().rstrip()
        if not string:
            return

        for i in range(0, len(string), 2):
            print(chr(int(string[i : i + 2], 16)), end="")
        print()


main()
