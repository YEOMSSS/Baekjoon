# P5를 찍은 후 제출하도록 하자.
# 만약 입력이 알파벳만으로 확실하다면 build_pos에서 딕셔너리 대신 26짜리 리스트를 만드는 것도 고려


def build_pos(B):
    pos = {}
    for i, c in enumerate(B):
        # or연산으로
        pos[c] = pos.get(c, 0) | (1 << i)
    return pos


def lcs_bitset_range(S, start, n, pos):
    dp = 0
    for i in range(start, start + n):
        c = S[i]
        x = pos.get(c, 0) | dp
        dp = (dp << 1) | 1
        dp = x & ~(x - dp)
    return dp.bit_count()


def main():
    A, B = input().strip(), input().strip()
    n = len(A)

    pos = build_pos(B)

    AA = A + A
    revA = A[::-1]
    rAA = revA + revA

    ans = 0
    for i in range(n):
        ans = max(ans, lcs_bitset_range(AA, i, n, pos))
        ans = max(ans, lcs_bitset_range(rAA, i, n, pos))

    print(ans)


if __name__ == "__main__":
    main()
