# Authored by : marigold2003
# Date : 2026-02-18
# Link : https://www.acmicpc.net/problem/32748


import sys

input = sys.stdin.readline


# [Summary]  $f(A + B)$

# 숫자를 바꾸는 대응표와 두 수가 입력된다.
# 각 자릿수를 대응표에 역으로 바꾼 후, 바뀐 두 수를 더한다.
# 더한 결과를 다시 대응표에 맞춰 바꾼다.


def main() -> None:

    # [Ideas]

    # 설명하기가 뭔가 애매해서 그렇지
    # 엄청 쉬운 문제다.

    # arr과 index로 처리하면 매우 쉬운 문제

    ##########

    arr = tuple(map(int, input().split()))
    a, b = map(
        lambda x: int("".join(map(str, (arr.index(n) for n in (map(int, x)))))),
        input().split(),
    )

    print("".join(map(lambda x: str(arr[int(x)]), (n for n in (str(a + b))))))

    ##########

    return


# [Review]

# 어우 보기안좋아


if __name__ == "__main__":
    main()
