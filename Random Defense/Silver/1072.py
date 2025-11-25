SCALE = 1_000_000_000_000
EPS = 1e-12


def main() -> None:
    X, Y = map(int, input().split())

    target = (int(Y / X * 100 + EPS) + 1) * SCALE

    # 0 <= Y <= X
    first = 0
    last = X

    while first <= last:
        win = (first + last) // 2
        win_rate = int((win + Y) / (win + X) * 100 * SCALE)
        # print(win, win_rate)

        if win_rate == target:
            print(win)
            return

        if win_rate < target:
            first = win + 1
        else:  # win_rate > target
            last = win - 1

    if win_rate < target:
        win += 1

    if win > X:
        print(-1)
        return

    print(win)


main()


"""
# float를 사용하면 안 되는 문제다.

def main() -> None:
    X, Y = map(int, input().split())

    # 현재 승률
    z = Y * 100 // X
    # 승률이 이미 99 이상이면 절대 안 변함
    if z >= 99:
        print(-1)
        return

    target = z + 1

    first = 0
    last = X  # upper bound 넉넉하게

    answer = -1

    while first <= last:
        win = (first + last) // 2
        win_rate = (Y + win) * 100 // (X + win)

        if win_rate >= target:
            answer = win
            last = win - 1
        else:
            first = win + 1

    print(answer)


main()

"""
