import sys

input = sys.stdin.readline

from collections import Counter


def main():
    N = int(input())
    string = input().rstrip()

    cnt_dict = Counter(string)

    hiarc = [cnt_dict["H"], cnt_dict["I"], cnt_dict["A"], cnt_dict["R"], cnt_dict["C"]]
    print(min(hiarc))


main()
