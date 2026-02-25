# Authored by : marigold2003
# Date : 2026-02-25
# Link : https://www.acmicpc.net/problem/5766


import sys

input = sys.stdin.readline


# [Summary] 할아버지는 유명해!

# N(500)주 동안의 매주 상위 M(500)명의 랭킹정보가 주어진다.
# 랭킹정보에 이름이 오를 때마다 선수의 포인트가 1 오른다.
# 2등이 누구인지 알아내시오.


def main() -> None:

    # [Ideas]

    # 10000까지 선수번호가 식별되니까, 그냥 10000짜리 arr 만들자.
    # dict를 짤까? 그게 더 효율적이긴 하지. 아닌가?
    # dict로 짜야 정렬하기 편할 거 같다.

    ##########

    while True:
        N, M = map(int, input().split())
        if not N:
            return

        count = dict()

        for _ in range(N):
            rank_info = map(int, input().split())
            for n in rank_info:

                if n in count:
                    count[n] += 1
                else:
                    count[n] = 1

        rank = sorted(count.items(), key=lambda x: (-x[1], x[0]))
        rank_len = len(rank)

        i = 0
        first = rank[i][1]

        while i < rank_len and rank[i][1] == first:
            i += 1

        second = rank[i][1]

        answer = []
        while i < rank_len and rank[i][1] == second:
            answer.append(rank[i][0])
            i += 1

        print(*answer)

    ##########

    return


# [Review]

# 좀 더 최적화가 될 것 같은데.
# while 안에 굳이 if가 또 들어갈 필요가 없었다.


if __name__ == "__main__":
    main()
