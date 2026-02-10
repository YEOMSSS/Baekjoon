# 이 얼마나 편하냐? sort가 이렇게 쉬운건데.
# 좆 같은 C언어.

import sys

input = sys.stdin.readline


def main():
    dict = {}

    for i in range(1, 9):
        dict[i] = int(input())

    dict_items = sorted(dict.items(), key=lambda x: x[1], reverse=True)

    total = 0
    answer = []
    for i in range(5):
        total += dict_items[i][1]
        answer.append(dict_items[i][0])

    print(total)
    answer.sort()
    print(*answer)


if __name__ == "__main__":
    main()
