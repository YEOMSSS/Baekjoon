# Authored by : marigold2003
# Date : 2026-11-23
# Link : https://www.acmicpc.net/problem/33663


import sys

input = sys.stdin.readline


# [Summary] 루미의 진정한™ 보라색 찾기

# 문제에 있는 수식대로 구현하면 된다.


def main() -> None:

    # [Ideas]

    # 진짜 수식 구현이라 할말이 없음.

    ##########

    H_lo, H_hi = map(int, input().split())
    S_lo, S_hi = map(int, input().split())
    V_lo, V_hi = map(int, input().split())
    R, G, B = map(int, input().split())

    M = max(R, G, B)
    m = min(R, G, B)

    V = M
    S = 255 * ((V - m) / V)

    if V == R:
        H = 60 * (G - B) / (V - m)
    elif V == G:
        H = 120 + ((60 * (B - R)) / (V - m))
    elif V == B:
        H = 240 + ((60 * (R - G)) / (V - m))

    if H < 0:
        H += 360

    if H < H_lo or H > H_hi or S < S_lo or S > S_hi or V < V_lo or V > V_hi:
        print("Lumi will not like it.")
        return
    print("Lumi will like it.")

    ##########

    return


# [Review]

# 수식 구현 문제
# 근데 문제 좀 잘 읽자. 조건이 많은 문제는 더 조심해야함.


if __name__ == "__main__":
    main()
