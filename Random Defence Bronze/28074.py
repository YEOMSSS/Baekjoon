# Authored by : marigold2003
# Date : 2026-03-13
# Link : https://www.acmicpc.net/problem/28074


import sys

input = sys.stdin.readline


# [Summary] 모비스

# 주어진 string에 M, O, B, I, S가 들어있는지 확인하자.


def main() -> None:

    # [Ideas]

    # set으로 비교하자.

    ##########

    string = set(input().rstrip())
    mobis = set("MOBIS")

    print("YES" if string >= mobis else "NO")
    ##########

    return


# [Review]

# python에서 set은 부등호로 포함관계를 검사할 수 있다.


if __name__ == "__main__":
    main()
