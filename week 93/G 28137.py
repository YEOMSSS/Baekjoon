# Authored by : marigold2003
# Date : 2026-03-14
# Link : https://www.acmicpc.net/problem/28137


import sys

input = sys.stdin.readline


# [Summary] 뭐라고? 안들려

# 좌표가 N(<= 200K)개 주어진다.
# 두 점의 기울기가 K(정수)인 경우의 수를 구하시오.


def main() -> None:

    # [Ideas]

    # 두 점을 고르려면 전부 비교해봐야 하는 거 아닌가?
    # K가 정수인 걸 이용하면 뭐가 될 것 같기도 한데.

    # 일단 모든 점에 대해서 검사를 해보긴 해야한다.
    # 어떤 점을 지나면서 기울기가 K인 직선을 긋고
    # 그 위에 있는 다른 점들의 개수를 세야 한다.

    # 근데 점이 200K개인데, 각 점마다 200K번의 비교를 할 순 없다.

    # 일단 기울기는 yb-y / xb-x = K
    # yb-Kxb = -kx+y = y-kx
    # y-kx만 저장하면 되는 문제였네?
    # 그리고 그게 동일한 애들끼리 조합으로 2경우 구하면 된다.

    ##########

    from collections import Counter

    N, K = map(int, input().split())

    y_minus_Kx = Counter()
    for _ in range(N):
        x, y = map(int, input().split())
        y_minus_Kx[y - K * x] += 1

    answer = 0
    for cnt in y_minus_Kx.values():
        if cnt < 2:
            continue

        answer += cnt * (cnt - 1)

    print(answer)

    ##########

    return


# [Review]

# 예외가 없으려나?
# 없네! 역시 수학은 하고 볼 일이구만.


if __name__ == "__main__":
    main()
