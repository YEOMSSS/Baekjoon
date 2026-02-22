# Authored by : marigold2003
# Date : 2026-02-22
# Link : https://www.acmicpc.net/problem/26906


import sys

input = sys.stdin.readline


# [Summary] Vikingahackare

# 바이킹은 생각보다 코딩에 능했다고 한다. (...)
# 길이가 4인 이진표현으로 그들은 char를 나타냈다.
# 바이킹의 이진표현으로 구성된 string을 번역하시오.


def main() -> None:

    # [Ideas]

    # 딕셔너리에 해독을 집어넣자.

    ##########

    N = int(input())
    # code_to_ch = {key: value for value, key in (list(input().split()) for _ in range(N))
    code_to_ch = dict(input().split()[::-1] for _ in range(N))

    string = input().rstrip()
    answer = []
    for i in range(0, len(string), 4):
        code = string[i : i + 4]
        if code not in code_to_ch:
            answer.append("?")
            continue
        ch = code_to_ch[code]
        answer.append(ch)

    print("".join(answer))

    ##########

    return


# [Review]

# 바이킹은 대체 어디까지 멋있을 셈인가


if __name__ == "__main__":
    main()
