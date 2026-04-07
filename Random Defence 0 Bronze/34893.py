# Authored by : marigold2003
# Date : 2026-03-06
# Link : https://www.acmicpc.net/problem/34893


import sys

input = sys.stdin.readline


# [Summary] 억지부리기

# U, O, S 의 개수가 주어진다.
# U 2개는 S 1개로 바꿀 수 있다.
# 만들 수 있는 UOS의 개수를 구하시오.


def main() -> None:

    # [Ideas]

    # U + S*2 해서 3으로 나누면 될듯?
    # 그거랑 O중에 작은 걸 찾으면 되겠다.

    # 어라, 이게 아닌가?
    # UUUUU S
    # UUU   SS
    # U     SSS
    # UUUUUUU

    # 전부 U로 변환한 후 처리한단 마인드였는데.
    # 음, S는 U로 바꿀 수가 없었지? 그럼 U도 min에 들어가야겠다.

    ##########

    U, O, S = map(int, input().split())

    print(min((U + S * 2) // 3, O, U))

    ##########

    return


# [Review]

# 가벼운 사칙연산


if __name__ == "__main__":
    main()
