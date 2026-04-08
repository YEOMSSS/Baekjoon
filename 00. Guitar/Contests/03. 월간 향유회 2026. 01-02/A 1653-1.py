# Authored by : marigold2003
# Date : 2026-02-22
# Link : https://www.acmicpc.net/contest/problem/1653/1


import sys

input = sys.stdin.readline


# [Summary] A번 - 월간 향유회 시즌 종료

# N(2000)명의 운영진이 있다.
# 각 운영진은 K(2000)개의 평가지표를 가진다.

# 수장은 다른 모든 운영진보다 높은 평가지표가 하나 이상 있어야 한다.
# 수장으로 임명 가능한 운영진의 수를 구하시오.


def main() -> None:

    # [Ideas]

    # max를 어떤 식으로 쓸까?
    # 아니면 입력받는 족족 갱신할까? << 이걸로 하자.

    # 모두보다 높아야 하니까, 동일하면 불가능.

    ##########

    N, K = map(int, input().split())
    best = [0] * K
    best_val = [0] * K

    for m in range(1, N + 1):
        info = map(int, input().split())
        for i, val in enumerate(info):
            if best_val[i] < val:
                best_val[i] = val
                best[i] = m
            elif best_val[i] == val:
                best[i] = 0

    result = set(best)

    if 0 in result:
        result.remove(0)

    print(len(result))

    ##########

    return


# [Review]

# 월간 향유회는 시즌 종료다, 에 혼또


if __name__ == "__main__":
    main()
