import sys

input = sys.stdin.readline


def main():
    while True:
        string = input().rstrip()
        if string == "EOI":
            return

        string = string.upper()

        if "NEMO" in string:
            print("Found")
        else:
            print("Missing")


main()
