# Authored by : marigold2003
# Date : 2026-02-09
# Link : https://www.acmicpc.net/problem/2530


import sys

input = sys.stdin.readline


# [Summary] 인공지능 시계

# 시작 시각이 주어진다.
# 요리에 걸리는 시간이 주어진다.
# 완료되는 시각을 구하여라. 입력은 초 단위다.


def main() -> None:

    # [Ideas]

    # 전에 만들어둔 시계를 가져다 쓰자.

    ##########

    class Clock:
        def __init__(self, hour=0, minute=0, second=0, date=0):
            self.hour = hour
            self.minute = minute
            self.second = second

            self.date = date

        def add_second(self, m):
            self.second += m

            # 60초가 넘으면 분으로 올림
            if self.second >= 60:
                self.minute += self.second // 60
                self.second %= 60

            # 60분이 넘으면 시로 올림
            if self.minute >= 60:
                self.hour += self.minute // 60
                self.minute %= 60

            # 24시가 넘으면 일로 올림
            if self.hour >= 24:
                self.date += self.hour // 24
                self.hour %= 24

        def curr(self):
            return f"{self.hour} {self.minute} {self.second}"

        def __str__(self):
            return self.curr()

    clock = Clock(*map(int, input().split()))
    clock.add_second(int(input()))
    print(clock)

    ##########

    return


# [Review]

# 편안하다.


if __name__ == "__main__":
    main()
