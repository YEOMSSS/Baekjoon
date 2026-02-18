# Authored by : marigold2003
# Date : 2026-02-12
# Link : https://www.acmicpc.net/problem/26267


import sys

input = sys.stdin.readline


# [Summary] 은?행 털!자 1

# 직선 경로에 은행이 있고, 이 은행은 정확히 T시각에만 털 수 있다.
# 시간은 0으로 시작하며, 좌표가 1이 증가할 때 시간이 1 증가한다.
# 좌표는 증가하기만 할 수 있으며, 시작점은 상관없다.
# 털 수 있는 최대 금액을 구하시오.


def main() -> None:

    # [Ideas]

    # 은행이 있는 좌표에서만 시작해서, 하나 털고 시작하면 된다.
    # 모든 은행에 대해서 다 해보면 된다.

    # 이동한 좌표만큼 시간이 늘어난다.
    # 은행은 최대 30만개다. 브루트포스로 할만할듯.

    # 대체 뭔 개소리야? 45000150000번을 어떻게하냐. 이걸 왜 시뮬레이션해 멍청하게.
    # (시각 - 좌표) 가 같은 애들끼리 묶어서 금액의 합을 구하면 된다.
    # 좌표의 시작점은 음수여도 된다. 안된다는 말이 없으니까

    ##########

    N = int(input())

    # (시각 - 좌표) 가 같은것들의 금액이 합쳐질 딕셔너리
    money_dict = dict()

    for _ in range(N):
        # 좌표 시각 금액
        x, t, c = map(int, input().split())
        if t - x not in money_dict:
            money_dict[t - x] = c
        else:
            money_dict[t - x] += c

    print(max(money_dict.values()))

    ##########

    return


# [Review]

# dict 쓰는 문제였네. 그러니까 HashMap
# 시간복잡도 구하는 습관이 생기니 좋다.


if __name__ == "__main__":
    main()
