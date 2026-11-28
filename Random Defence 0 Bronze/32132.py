# Authored by : marigold2003
# Date : 2026-11-28
# Link : https://www.acmicpc.net/problem/32132


import sys

input = sys.stdin.readline


# [Summary] PlayStation이 아니에요

# PS4나 PS5가 문자열에 포함되면 PS로 만들어야 한다.
# 변경을 완료한 문자열을 출력하시오.


def main() -> None:

    # [Ideas]

    # 스택으로 하자. 4나 5가 나왔는데 앞에 둘이 PS면 지나가기

    ##########

    N = int(input())
    string = input().rstrip()

    stack = []
    for i in range(N):
        ch = string[i]

        if i < 2:
            stack.append(ch)
            continue

        if stack[-2:] == list("PS"):
            if ch == "4" or ch == "5":
                continue

        stack.append(ch)

    print("".join(stack))

    ##########

    return


# [Review]

# 그냥 문자열로 굴려도 될 것 같다.


if __name__ == "__main__":
    main()
