# Authored by : marigold2003
# Date : 2026-03-29
# Link : https://www.acmicpc.net/problem/29790


import sys

input = sys.stdin.readline


# [Summary] 임스의 메이플컵

# N, U, L이 입력된다.
# N이 1K 이상이면 Good을 출력한다.
# 동시에 U가 8K 이상이고나 L이 260 이상이면 Very Good을 출력한다.
# 만족하지 못하면 Bad를 출력한다.


def main() -> None:

    # [Ideas]

    # 있는 그대로 구현하자.

    ##########

    N, U, L = map(int, input().split())

    if N < 1000:
        print("Bad")
        return

    if U >= 8000 or L >= 260:
        print("Very Good")
    else:
        print("Good")

    ##########

    return


# [Review]

# 이기적인 놈😠, 메이플이 망해도 좋다. 이거냐❓❗️


if __name__ == "__main__":
    main()
