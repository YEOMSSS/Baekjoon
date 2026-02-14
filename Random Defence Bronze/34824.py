# Authored by : marigold2003
# Date : 2026-02-13
# Link : https://www.acmicpc.net/problem/34824


import sys

input = sys.stdin.readline


# [Summary] 연대 다음 고대

# 대학교의 이름이 순서대로 입력된다.
# yonsei가 korea보다 먼저 입력되면 승리한다.


def main() -> None:

    # [Ideas]

    # yonsei가 입력되면 종료
    # korea가 입력되면 종료
    # 굳이 전체를 입력받을 필요가 없음.

    ##########

    N = int(input())

    for _ in range(N):
        univ = input().rstrip()
        if univ == "yonsei":
            print("Yonsei Won!")
            return
        if univ == "korea":
            print("Yonsei Lost...")
            return

    ##########

    return


# [Review]

# 이런 브론즈도 필요해


if __name__ == "__main__":
    main()
