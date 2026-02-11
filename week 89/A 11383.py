# Authored by : marigold2003
# Date : 2026-02-11
# Link : https://www.acmicpc.net/problem/11383


import sys

input = sys.stdin.readline


# [Summary] 뚊

# original이 주어진다.
# 다음 input이 original의 각 ch를 2배로 늘려놓은 모습인지 확인하라.


def main() -> None:

    # [Ideas]

    # 한줄씩 비교하면 될듯

    ##########

    N, M = map(int, input().split())
    original = list(input().rstrip() for _ in range(N))
    for row in original:
        if "".join(ch * 2 for ch in row) == input().rstrip():
            continue
        print("Not Eyfa")
        return

    print("Eyfa")

    ##########

    return


# [Review]

# join으로 편하게 합쳤다.


if __name__ == "__main__":
    main()
