# 큰수연산은 역시 이썬이형

import sys

input = sys.stdin.readline

MAX_INT = 10**100

dp = [1, 2]
ptr = 0

while True:
    next = dp[ptr] + dp[ptr + 1]
    if next > MAX_INT:
        break
    dp.append(next)
    ptr += 1


def main():
    while True:
        a, b = map(int, input().split())
        if a == b == 0:
            return

        result = 0
        for i, num in enumerate(dp):
            if num < a:
                continue
            elif num > b:
                break
            result += 1

        print(result)


main()
