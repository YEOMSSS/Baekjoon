# Authored by : marigold2003
# Date : 2026-03-30
# Link : https://www.acmicpc.net/problem/34021


import sys

input = sys.stdin.readline


# [Summary] [T] 스코어보드가 121분 남은 시점에서 프리즈되었습니다.

# M분이 주어진다. 참가자는 N(1K)명이다.
# 끝날 때까지 L분이 남으면 프리즈된다.
# 1문제 제외 전부 해결한 참가자가 등장해도 프리즈된다.

# 각 참가자가 1문제 제외 전부 해결하기까지의 시간이 주어진다.
# 프리즈 문구를 출력하시오.


def main() -> None:

    # [Ideas]

    # 아니 예측으로 공지를 쓰고앉았네.
    # -1을 제외한 입력에서 최솟값을 찾으면 된다.
    # 그걸로 찾은 남은시간이 L보다 작으면 L로 출력하면 된다.

    ##########

    T = int(input())

    for _ in range(T):
        N, M, L = map(int, input().split())

        answer = 1440
        for t in map(int, input().split()):
            if t == -1:
                continue
            answer = min(answer, t)

        result = max(M - answer, L)
        if result == 1:
            print(f"The scoreboard has been frozen with {result} minute remaining.")
        else:
            print(f"The scoreboard has been frozen with {result} minutes remaining.")

    ##########

    return


# [Review]

# 묘하게 귀찮네.

# 프리즈 공지 멘트를 자동으로 써서 뭐함 도대체?
# 참가자가 문제해결에 걸리는 시간이 예상인데 프로그램이 의미있는거임?
# 차라리 문제를 해결하고 걸린 시간이 S분이라고 할 때 프리즈공지가 어떻게 출력되어야 하는지를
# 쓰라고 했으면 좀 더 속편하게 풀었겠다.

# 물론 문제 푸는데에는 상관없습니다.


if __name__ == "__main__":
    main()
