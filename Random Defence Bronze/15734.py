L, R, A = map(int, input().split())

big = max(L, R)
small = min(L, R)


if big < small + A:
    print(big * 2 + ((A - big + small) // 2) * 2)

else:
    print((small + A) * 2)
