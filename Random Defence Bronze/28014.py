# Authored by : marigold2003
# Date : 2026-02-19
# Link : https://www.acmicpc.net/problem/28014


import sys

input = sys.stdin.readline


# [Summary] 첨탑 밀어서 부수기

# 첨탑이 일렬로 놓여 있다.
# 밀려 넘어지는 첨탑의 높이가 그다음 첨탑보다 높으면 그다음 첨탑도 넘어진다.
# 앞에서부터 밀 때, 밀어야 하는 횟수를 구하시오.


def main() -> None:

    # [Ideas]

    # 높을 때만 넘어진다는 것은
    # 낮거나 같을 땐 밀어줘야 한다는 것이다.
    # 이게 브3이라고? 그런가?

    ##########

    N = int(input())
    it = map(int, input().split())

    prev = next(it)
    count = 1

    for h in it:
        if prev <= h:
            count += 1
        prev = h

    print(count)

    ##########

    return


# [Review]

# 묘하게 발상이 어려운데?
# iter로 푸니까 편하다.


if __name__ == "__main__":
    main()
