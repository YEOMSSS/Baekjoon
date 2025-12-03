import sys

input = sys.stdin.readline


def func(n: int, cipher: str, rome_dict: set) -> bool:
    string = ""
    for ch in cipher:
        temp = ord(ch) + n
        if temp > ord("z"):
            temp -= 26
        string += chr(temp)

    for rome in rome_dict:
        if rome in string:
            print(string)
            return True

    return False


def main() -> None:
    cipher = input().rstrip()

    rome_dict = set()
    for _ in range(int(input())):
        rome_dict.add(input().rstrip())

    for i in range(0, 26):
        if func(i, cipher, rome_dict):
            return


main()
