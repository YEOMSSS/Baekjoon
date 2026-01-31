import sys

input = sys.stdin.readline


class Clock:
    def __init__(self):
        self.date = 0
        self.hour = 0
        self.minute = 0

    def add_minute(self, m):
        self.minute += m

        # 60초가 넘으면 분으로 올림
        if self.minute >= 60:
            self.hour += self.minute // 60
            self.minute %= 60

        # 60분이 넘으면 일로 올림
        if self.hour >= 24:
            self.date += self.hour // 24
            self.hour %= 24

    def curr(self):
        return f"{self.hour:02}:{self.minute:02}"

    # 이건 완전 자바같네. 오버라이딩 맛이 난다? 이 코드에선 필요없긴함. print(Clock)에 발동
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
