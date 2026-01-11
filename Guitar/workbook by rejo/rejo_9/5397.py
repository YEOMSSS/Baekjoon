import sys

input = sys.stdin.readline

from collections import deque


def main():
    for _ in range(int(input())):
        string = input().rstrip()

        left = []
        right = deque()

        for ch in string:
            match ch:
                case "<":
                    if not left:
                        continue
                    right.appendleft(left.pop())
                case ">":
                    if not right:
                        continue
                    left.append(right.popleft())
                case "-":
                    if not left:
                        continue
                    left.pop()
                case _:
                    left.append(ch)

        print("".join(left + list(right)))


main()


# 시간초과 코드
def wrong1():
    for _ in range(int(input())):
        cursor = 0
        string = []

        key_log = input().rstrip()

        for ch in key_log:
            match ch:
                case "<":
                    if cursor == 0:
                        continue
                    cursor -= 1
                case ">":
                    if cursor == len(string):
                        continue
                    cursor += 1
                case "-":
                    if cursor == 0:
                        continue
                    cursor -= 1
                    string.pop(cursor)
                case _:
                    if cursor == len(string):
                        string.append(ch)
                        cursor += 1
                    else:
                        string.insert(cursor, ch)
                        cursor += 1

        print("".join(string))
