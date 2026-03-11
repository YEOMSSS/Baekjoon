# Authored by : marigold2003
# Date : 2026-03-11
# Link : https://www.acmicpc.net/problem/25635


import sys

input = sys.stdin.readline


# [Summary] 자유 이용권

# 놀이기구별로 이용횟수 제한이 있다.
# 연속으로 같은 놀이기구를 타지 않을 것이다.
# 놀이기구를 이용할 수 있는 최대 횟수를 구하시오.
# 아, 나에게는 자유이용권이 있다.


def main() -> None:

    # [Ideas]

    # 힙이다. 최대힙이다.
    # 다 때려넣고 하나씩 꺼내면서 가자.
    # 20311이네 이거.
    # 엥, 10만이구나. 절대안되겠네

    ##########

    import sys

    input = sys.stdin.readline

    def main():
        N = int(input())
        arr = list(map(int, input().split()))

        if N == 1:
            print(1)
            return

        S = sum(arr)
        M = max(arr)
        R = S - M

        # 다른 놀이기구가 충분할 때
        if M <= R + 1:
            print(S)
        # 최댓값이 너무 클 때
        else:
            print(2 * R + 1)

    if __name__ == "__main__":
        main()

    ##########

    return


# [Review]

# 그냥 그리디였네
# 시뮬레이션이 안되는 문제였구나.


if __name__ == "__main__":
    main()
