# Authored by : marigold2003
# Date : 2026-03-15
# Link : https://www.acmicpc.net/problem/1284


import sys

input = sys.stdin.readline


# [Summary] 집 주소

# 각 숫자 사이에는 1의 여백이 들어간다.
# 1은 2의 너비를 가지고, 0은 4의 너비를 가진다.
# 나머지 숫자는 3의 너비를 가진다.
# 시작과 끝에는 1의 여백이 들어간다.

# 주어진 수 N의 범위를 구하시오.


def main() -> None:

    # [Ideas]

    # 앞뒤로 1씩 붙이니까 +2
    # 사이사이에 1씩 들어가니까 +len(N)-1
    # 그리고 1일때랑 0일때만 따로 처리.

    ##########

    while True:
        N = input().rstrip()
        if N == "0":
            return

        answer = 2 + len(N) - 1

        for n in N:
            if n == "0":
                answer += 4
            elif n == "1":
                answer += 2
            else:
                answer += 3

        print(answer)

    ##########

    return


# [Review]

# 쉽고 빠른 구현


if __name__ == "__main__":
    main()
