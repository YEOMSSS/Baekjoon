# Authored by : marigold2003
# Date : 2026-03-03
# Link : https://www.acmicpc.net/problem/00000000000000000000000000


import sys

input = sys.stdin.readline


# [Summary] 큰 수 계산

# 임의의 수식이 입력될 때 수식을 계산하시오.
# 소수점이 나올 경우 내린다.


def main() -> None:

    # [Ideas]

    # 연산자 우선순위도 있는데 이게 브론즈 2라고? 스택 써야하는데?
    # eval때문에 그러는거임?

    # 소수점 내림이면 //정수나눗셈 조지면되고...

    ##########

    N = int(input())

    stack = [input().rstrip()]

    for _ in range(2 * N - 2):

        curr = input().rstrip()

        if stack[-1] == "*":
            stack.pop()
            stack.append(int(stack.pop()) * int(curr))

        elif stack[-1] == "/":
            stack.pop()
            stack.append(int(stack.pop()) // int(curr))
        else:
            stack.append(curr)

    answer = [0]
    for s in stack:
        if answer[-1] == "+":
            answer.pop()
            answer.append(int(answer.pop()) + int(s))
        elif answer[-1] == "-":
            answer.pop()
            answer.append(int(answer.pop()) - int(s))
        else:
            answer.append(s)

    print(answer[-1])

    ##########

    return


# [Review]

# 더 쉬운 방법이 있어서 브론즈겠지?;;;
# 진짜 eval때문이었네........................


if __name__ == "__main__":
    main()
