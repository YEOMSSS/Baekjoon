# Authored by : marigold2003
# Date : 2026-02-06
# Link : https://www.acmicpc.net/problem/14469

import sys

input = sys.stdin.readline


# [Summary]

# 소들이 농장으로 들어간다.
# 소들은 a초에 농장에 도착하고, b초만큼 검사를 진행한다.
# 만약 앞에 소가 검사중이면, 기다리다가 그 검사가 끝난 후 b초만큼 검사를 진행한다.
# 마지막 소의 검사가 끝나는 시각을 구하시오.


def main() -> None:

    # [Ideas]

    # 비슷한 문제를 풀었던 것 같다.

    # 어떤 소의 도착시점 vs 그 앞 소의 검문종료시간
    # 둘 중 큰 것에 검문시간을 더해주면 도착한 소의 검문종료시간이 나온다.

    ##########

    N = int(input())
    cows = list(tuple(map(int, input().split())) for _ in range(N))
    cows.sort()

    prev = 0
    for a, b in cows:
        prev = max(a, prev)
        prev += b

    print(prev)

    ##########

    return


# [Review]

# 코드가 생각보다 깔끔하게 나오네.

if __name__ == "__main__":
    main()
