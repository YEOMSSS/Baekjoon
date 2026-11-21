# Authored by : marigold2003
# Date : 2026-11-21
# Link : https://www.acmicpc.net/problem/15439


import sys

input = sys.stdin.readline


# [Summary] 베라의 패션

# 상의 N벌과 하의 N벌이 있다.
# i번째 상의와 i번째 하의의 색은 같다.
# N개의 색상은 모두 다르다.
# 상하의가 서로 다른 색상인 조합의 개수는?


def main() -> None:

    # [Ideas]

    # 조합이다.
    # 대충 생각해 보면 N*N에서 겹치는거만 빼주면 된다.
    # 겹치는 건 N개잖아? 그럼 N*(N-1) 아니냐?

    ##########

    N = int(input())
    print(N * (N - 1))

    ##########

    return


# [Review]

# 이건 정말 쉬운데


if __name__ == "__main__":
    main()
