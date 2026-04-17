# Authored by : marigold2003
# Date : 2026-04-15
# Link : https://www.acmicpc.net/problem/34813


import sys

input = sys.stdin.readline


# [Summary] 공통교육과정

# 주어진 교양 과목이 학문의 토대에 속해 있으면 Foundation,
# 지성의 열쇠에 속해 있으면 Claves,
# 베리타스에 속해 있으면 Veritas,
# 지성의 확장에 속해 있으면 Exploration을 출력한다.


def main() -> None:

    # [Ideas]

    # 뭘로 시작하는건지만 보면 되지 뭐.

    ##########

    data = input().rstrip()

    match data[0]:
        case "F":
            print("Foundation")
        case "C":
            print("Claves")
        case "V":
            print("Veritas")
        case "E":
            print("Exploration")

    ##########

    return


# [Review]

# 가지마 백준


if __name__ == "__main__":
    main()
