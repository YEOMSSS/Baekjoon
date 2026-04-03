# Authored by : marigold2003
# Date : 2026-04-03
# Link : https://www.acmicpc.net/problem/34034


import sys

input = sys.stdin.readline


# [Summary] 스트릭 채우기

# 문제 N개와 스트릭 M개를 준비했다.
# 각 문제를 푸는 데 걸리는 일수가 주어진다.
# 문제를 동시에 푸는 것은 불가능하다.
# K일동안 스트릭을 유지하는 방법을 출력하시오.
# N, M, K <= 200K


def main() -> None:

    # [Ideas]

    # 문제 푸는 동안 스트릭으로 버티다가 문제 내는거지.
    # 마지막 날에 스트릭 내도 상관없는거고.
    # 그럼 쉬운거부터 풀어야할거아니냐. 스트릭은 부족해.
    # 빨리끝나는문제부터 처리하면 된다.

    ##########

    N, M, K = map(int, input().split())
    Problems = list(zip(map(int, input().split()), range(1, N + 1)))
    Problems.sort()

    answer = []

    day = 0

    for p, i in Problems:

        while p > 1:
            day += 1
            answer.append(0)
            M -= 1

            if day == K:
                if M < 0:
                    print(-1)
                    return
                print(*answer)
                return
            p -= 1

        day += 1
        answer.append(i)

        if day == K:
            if M < 0:
                print(-1)
                return
            print(*answer)
            return

    while day < K:
        day += 1
        answer.append(0)
        M -= 1

        if day == K:
            if M < 0:
                print(-1)
                return
            print(*answer)
            return

    print(-1)

    ##########

    return


# [Review]

# 너무 막짜긴 했는데, 돌아가긴 하지 않을까요?


if __name__ == "__main__":
    main()
