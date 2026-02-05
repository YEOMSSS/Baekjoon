# Authored by : marigold2003
# Date : 2026-02-05
# Link : https://www.acmicpc.net/problem/14468

import sys

input = sys.stdin.readline


# [Summary]

# 소가 26마리 있다.
# 원에는 출입구가 52개 있다.
# 모든 소는 다른 입구로 들어가서 다른 출구로 나온다.
# 원 안에서 경로가 무조건 겹치는 소쌍은 몇개일까?


def main() -> None:

    # [Ideas]

    # 입력이 ABCAD... 이런식으로 들어오니까 인덱스는 확인하기 쉽다.
    # A와 A 사이에 알파벳이 몇개 있을텐데, 같은개 두개 있지 않은 모든 알파벳은 A와 겹친다.
    # 이런식으로 전부 확인해서 더하고 2로 나누면 되지 않을까?

    ##########

    from collections import defaultdict, Counter

    route = input().rstrip()

    cow_information = defaultdict(list)
    for i, ch in enumerate(route):
        cow_information[ch].append(i)

    answer = 0
    for start, end in cow_information.values():
        # 같은 소 사이에 있는 애들 세기
        counts = Counter(route[start + 1 : end])
        # 사이에 있는 애들이 홀수면 무조건 걔랑은 겹침
        answer += sum(count % 2 for count in counts.values())

    # answer는 AB와 BA가 다 들어있으니 //2
    print(answer // 2)

    ##########

    return


# [Review]

# defaultdict란 무엇인가

if __name__ == "__main__":
    main()
