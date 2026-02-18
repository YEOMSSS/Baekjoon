# Authored by : marigold2003
# Date : 2026-02-12
# Link : https://www.acmicpc.net/problem/3495


import sys

input = sys.stdin.readline


# [Summary] 아스키 도형

# /, \ 으로 이루어진 다각형이 하나 주어진다.
# 도형의 넓이를 구하여라.


def main() -> None:

    # [Ideas]

    # 한줄씩 읽으면 된다.
    # /가 됐든 \가 됐든 홀수번 이후부터는 도형 내부고
    # 짝수번 이후부터는 도형 외부다.

    # 줄 돌돌 말아놓고 막대기 하나 꽂아서 안에있게 밖에있게 하는 그거같네.

    # /, \는 0.5, 내부 .은 1이다.

    ##########

    H, W = map(int, input().split())

    answer = 0
    for _ in range(H):
        row = input().rstrip()

        # /나 \를 만날 때마다 토글한다.
        inside_flag = False
        for ch in row:
            if ch == ".":
                if inside_flag:
                    answer += 1
            else:
                answer += 0.5
                inside_flag = not inside_flag

    print(int(answer))

    ##########

    return


# [Review]

# 마음이 편안해지는 문제
# 너무 재밌다


if __name__ == "__main__":
    main()
