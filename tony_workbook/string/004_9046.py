import sys

input = sys.stdin.readline

from collections import Counter


def main():
    T = int(input())

    for _ in range(T):
        string = input().rstrip()

        count = Counter(string)
        top = count.most_common(3)

        if len(top) < 2:
            print(top[0][0])
            continue

        for i in range(2):
            if top[i][0] == " ":
                top.pop(i)
                break

        if top[0][1] == top[1][1]:
            print("?")
            continue
        else:
            print(top[0][0])


main()
