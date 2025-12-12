def func1(W0, I0, T, D, DI, A):
    W = W0
    I = I0

    for _ in range(D):
        W += DI - (I + A)

        if W <= 0:
            return ("Danger Diet",)

    return (W, I)


def func2(W0, I0, T, D, DI, A):
    W = W0
    I = I0

    for _ in range(D):
        use = DI - (I + A)
        W += use

        if abs(use) > T:
            I += use // 2

        if W <= 0 or I <= 0:
            return ("Danger Diet",)

    if I0 - I > 0:
        return (W, I, "YOYO")
    else:
        return (W, I, "NO")


def main() -> None:
    # 체중, 섭취량=기초대사량, 변화역치
    W0, I0, T = map(int, input().split())
    # 기간, 다이어트섭취량, 다이어트활동량
    D, DI, A = map(int, input().split())

    print(*func1(W0, I0, T, D, DI, A))
    print(*func2(W0, I0, T, D, DI, A))


main()
