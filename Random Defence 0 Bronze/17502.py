# Authored by : marigold2003
# Date : 2026-03-19
# Link : https://www.acmicpc.net/problem/17502


import sys

input = sys.stdin.readline


# [Summary] 클레어와 팰린드롬

# string이 입력된다. (<= 100)
# ?를 채워서 팰린드롬으로 만드시오.


def main() -> None:

    # [Ideas]

    # 투포인터로 확인하자.
    # 아니면, 뒤집은 걸 하나 더 만들까?

    # 원래거가 차있으면 넣고
    # 원래거가 ?면 뒤집은거 넣자.

    # 마지막에 한번 더 확인해서 ?를 a로 바꾸자.
    # 이렇게 절반만 만들어서 뒤집어 붙이자.

    # 아니면 뭐.. 그냥 투포인터로 하던가.

    # N이 작으니까 그냥 뒤집어 붙이지도 말자. 귀찮다.

    ##########

    N = int(input())
    string = input().rstrip()
    string_rev = string[::-1]

    for i in range(N):
        if string[i] != "?":
            print(string[i], end="")
            continue
        if string_rev[i] != "?":
            print(string_rev[i], end="")
            continue
        print("a", end="")

    print()

    ##########

    return


# [Review]

# 이름을 비슷하게 하니까 버그를 못찾겠네
# 그냥 집중력 부족인거같기도 하고.


if __name__ == "__main__":
    main()
