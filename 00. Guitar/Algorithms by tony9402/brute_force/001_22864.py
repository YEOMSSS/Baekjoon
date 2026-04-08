# 그리디. 일을 할 수 있으면 하면 된다.


def main() -> None:
    A, B, C, M = map(int, input().split())

    tired = 0
    worked = 0

    for i in range(24):

        # 일할 수 없는 경우
        if tired + A > M:
            tired -= C
            if tired < 0:
                tired = 0

        # 일할 수 있는 경우
        else:
            tired += A
            worked += B

    print(worked)


main()
