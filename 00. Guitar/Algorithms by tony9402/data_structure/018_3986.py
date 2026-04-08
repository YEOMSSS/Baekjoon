# 참 쉽죠잉~~~

import sys

input = sys.stdin.readline


def main() -> None:
    N = int(input())

    result = 0
    for _ in range(N):
        string = input().rstrip()

        stack = []

        for ch in string:

            if not stack:
                stack.append(ch)
                continue

            if stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)

        if not stack:
            result += 1

    print(result)


main()
