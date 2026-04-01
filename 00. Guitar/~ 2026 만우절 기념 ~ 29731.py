# Authored by : marigold2003
# Date : 2026-04-01
# Link : https://www.acmicpc.net/problem/29731


import sys

input = sys.stdin.readline


# [Summary] 2033년 밈 투표

# Never gonna give you up
# Never gonna let you down
# Never gonna run around and desert you
# Never gonna make you cry
# Never gonna say goodbye
# Never gonna tell a lie and hurt you
# Never gonna stop

# 위 문장이 아닌 다른 문장이 들어오면 Yes를 출력한다.
# 입력된 모든 문장이 위 문장에 속한다면 No를 출력한다.


def main() -> None:

    # [Ideas]

    # 등호로 쉽게 구분이 가능하다.

    ##########

    Memes = {
        "Never gonna give you up",
        "Never gonna let you down",
        "Never gonna run around and desert you",
        "Never gonna make you cry",
        "Never gonna say goodbye",
        "Never gonna tell a lie and hurt you",
        "Never gonna stop",
    }

    N = int(input())
    for _ in range(N):
        data = input().rstrip()
        if data not in Memes:
            print("Yes")
            return

    print("No")

    ##########

    return


# [Review]

# The domain Solved.ac may be for sale. Click here to inquire about this domain.
# 그래그래 2026 만우절 축하한다


if __name__ == "__main__":
    main()
