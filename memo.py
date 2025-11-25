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
