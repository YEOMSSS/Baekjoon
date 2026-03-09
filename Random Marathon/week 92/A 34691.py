# Authored by : marigold2003
# Date : 2026-03-04
# Link : https://www.acmicpc.net/problem/34691


import sys

input = sys.stdin.readline


# [Summary] 대전과학고등학교를 사랑하십니까?

# animal이 입력되면 Panthera tigris를 출력한다.
# tree가 입력되면 Pinus densiflora를 출력한다.
# flower가 입력되면 Forsythia koreana를 출력한다.
# end가 입력되면 프로그램을 종료한다.


def main() -> None:

    # [Ideas]

    # 그냥 입력을 받고 출력하는 간단한 문제.

    ##########

    while True:
        string = input().rstrip()
        if string == "end":
            return

        match string:
            case "animal":
                print("Panthera tigris")
            case "tree":
                print("Pinus densiflora")
            case "flower":
                print("Forsythia koreana")

    ##########

    return


# [Review]

# 우리 학교 꽃은 뭘까?


if __name__ == "__main__":
    main()
