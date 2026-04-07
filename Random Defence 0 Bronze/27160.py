# Authored by : marigold2003
# Date : 2026-02-22
# Link : https://www.acmicpc.net/problem/27160


import sys

input = sys.stdin.readline


# [Summary] 할리갈리

# 펼쳐진 카드들의 목록이 주어진다.
# 정확히 5개인 과일이 있으면 종을 쳐야 한다.

# 종을 쳐야 할지 말아야 할지 판단하시오.


def main() -> None:

    # [Ideas]

    # 딕셔너리로 인덱스변환하자.
    # 그냥 딕셔너리로 셀까?
    # 아, 딕셔너리 써야되냐??

    ##########

    arr = [0] * 4
    fruit_to_index = {"STRAWBERRY": 0, "BANANA": 1, "LIME": 2, "PLUM": 3}

    N = int(input())
    for _ in range(N):
        fruit, count = input().split()
        arr[fruit_to_index[fruit]] += int(count)

    print("YES" if 5 in arr else "NO")

    ##########

    return


# [Review]

# 오랜만에 할리갈리가 하고 싶은걸...


if __name__ == "__main__":
    main()
