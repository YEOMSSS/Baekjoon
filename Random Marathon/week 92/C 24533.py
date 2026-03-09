# Authored by : marigold2003
# Date : 2026-03-05
# Link : https://www.acmicpc.net/problem/24533


import sys

input = sys.stdin.readline


# [Summary] 결합

# 물질이 N(30K)개 있다.
# 각 물질은 특성을 두개 가지며, 두 물질을 결합시킬 수 있다.
# (a,b)와 (c,d)를 결합시키면 ad+bc 에너지가 발생하고 a+c, b+d인 물질이 생긴다.
# 물질을 합치는 과정에서 얻을 수 있는 에너지의 양의 합의 최대치를 출력하시오.


def main() -> None:

    # [Ideas]

    # 뭐 그리딘가, 했는데
    # 순서가 상관없어보인다.
    # 이런 문제 특이지 뭐.

    ##########

    N = int(input())
    answer = 0

    a, b = map(int, input().split())
    for _ in range(N - 1):
        c, d = map(int, input().split())
        answer += a * d + b * c
        a, b = a + c, b + d

    print(answer)

    ##########

    return


# [Review]

# 알면 쉬움. 알기가 어려움.
# 노트에 식을 써보니 알 수 있었다.
# 분배법칙으로 풀어놓으니까 다 똑같이 생김.


if __name__ == "__main__":
    main()
