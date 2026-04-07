# Authored by : marigold2003
# Date : 2026-02-10
# Link : https://www.acmicpc.net/problem/5704


import sys

input = sys.stdin.readline


# [Summary] 팬그램

# 소문자로만 이루어진 문장에 모든 알파벳이 들어있는지 확인하시오.


def main() -> None:

    # [Ideas]

    # set에 넣어서 길이가 26이면 되는거 아닌가?

    ##########

    while True:
        string = input().rstrip()
        if string == "*":
            return

        # 공백 처리하기 귀찮으니 그냥 공백을 더하고 27로 설정한다.
        print("Y" if len(set(string + " ")) == 27 else "N")

    ##########

    return


# [Review]

# 귀찮음이 사람을 효율적으로 만들어


if __name__ == "__main__":
    main()
