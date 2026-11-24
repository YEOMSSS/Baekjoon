# Authored by : marigold2003
# Date : 2026-11-24
# Link : https://www.acmicpc.net/problem/7568


import sys

input = sys.stdin.readline


# [Summary] 덩치

# 키와 몸무게가 둘 다 상대보다 크면 상대보다 덩치가 크다.
# 순위는 자신보다 더 큰 덩치를 가진 사람의 수 + 1이다.
# 사람은 최대 50명 있다.


def main() -> None:

    # [Ideas]

    # 50명이니까 브루트포스로 충분할 것 같다는 생각은 든다.
    # 사람을 한 명 정하고, 나머지 49명과 전부 비교해도 될 듯.
    # 그냥 자신과도 비교하는 비용이 한 번쯤 있어도 뭐. 그냥 된다.
    # 최적화하기 귀찮으니까 그냥 하자.

    # 그래도 중복 정도는 없애줄까 싶기도 하고.
    # 근데 사실 똑같기는 한듯하면서도,,, 순회는 좀 덜 도네.

    ##########

    N = int(input())

    p_info = [tuple(map(int, input().split())) for _ in range(N)]
    result = [1 for _ in range(N)]

    for i in range(N):
        for j in range(i + 1, N):
            # j보다 큰 덩치가 존재
            if p_info[i][0] > p_info[j][0] and p_info[i][1] > p_info[j][1]:
                result[j] += 1
            # i보다 큰 덩치가 존재
            elif p_info[i][0] < p_info[j][0] and p_info[i][1] < p_info[j][1]:
                result[i] += 1

    print(*result)

    ##########

    return


# [Review]

# 문제를 보자마자 풀 수 있어야 한다.
# 재활을 하려면 실랜디를 다시 하는 편이 좋아보임.


if __name__ == "__main__":
    main()
