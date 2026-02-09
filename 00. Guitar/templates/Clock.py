import sys

input = sys.stdin.readline


class Clock:
    def __init__(self, hour=0, minute=0, second=0, date=0):
        self.hour = hour
        self.minute = minute
        self.second = second

        self.date = date

    def add_minute(self, m):
        self.minute += m

        # 60분가 넘으면 시로 올림
        if self.minute >= 60:
            self.hour += self.minute // 60
            self.minute %= 60

        # 24시가 넘으면 일로 올림
        if self.hour >= 24:
            self.date += self.hour // 24
            self.hour %= 24

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
        return f"{self.hour:02}:{self.minute:02}:{self.second:02}"

    # print(Clock)에 발동, java오버라이딩같은 느낌
    def __str__(self):
        return self.curr()


def main():
    N, K = map(int, input().split())

    clock = Clock()
    answer = []
    while clock.date <= N:
        clock.add_minute(15 * 60)
        if clock.date == N:
            answer.append(clock.curr())

        clock.add_minute(3 * 60)
        if clock.date == N:
            answer.append(clock.curr())

        clock.add_minute(3 * 60)
        if clock.date == N:
            answer.append(clock.curr())

        clock.add_minute(3 * 60 + K)

    print(len(answer))
    print("\n".join(answer))


if __name__ == "__main__":
    main()
