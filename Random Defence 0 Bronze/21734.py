# Authored by : marigold2003
# Date : 2026-02-10
# Link : https://www.acmicpc.net/problem/21734


import sys

input = sys.stdin.readline


# [Summary] SMUPC의 등장

# input된 string의 각 char에 대하여
# ASCII값을 10진법으로 나타내서 각 자릿수를 더한 만큼 출력하시오.


def main() -> None:

    # [Ideas]

    # ord 쓰면 되겠다.

    ##########

    # for ch in input().rstrip():
    # print(ch * sum(map(int, str(ord(ch)))))

    print("\n".join(ch * sum(map(int, str(ord(ch)))) for ch in input().rstrip()))

    ##########

    return


# [Review]

# ord가 짱이에요


if __name__ == "__main__":
    main()
