# Authored by : marigold2003
# Date : 2026-02-08
# Link : https://www.acmicpc.net/problem/10205


import sys

input = sys.stdin.readline


# [Summary] 헤라클레스와 히드라

# 히드라의 목을 자르면 2개가 돋아난다.
# 목을 자름과 동시에 불로 지지면 돋아나지 않는다.
# 각 행동을 c, b 라고 할 때 입력된 대로 행동하여 히드라를 죽일 수 있는지 확인하라.


def main() -> None:

    # [Ideas]

    # 그대로 시뮬레이션을 돌려보자.
    # c행동을 하면 머리가 하나 늘어나고,
    # b행동을 하면 머리가 하나 줄어든다.

    ##########

    T = int(input())

    for i in range(T):
        h = int(input())
        commands = input().rstrip()

        for command in commands:
            if command == "c":
                h += 1
            else:  # command == "b"
                h -= 1

        print(f"Data Set {i + 1}:\n{h}\n")

    ##########

    return


# [Review]

# 젠장 헤라클라스, 그 정도 지능으로는 헤라의 인정을 받을 수 없다고

if __name__ == "__main__":
    main()
