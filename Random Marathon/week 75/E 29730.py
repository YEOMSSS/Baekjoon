import sys

input = sys.stdin.readline


def main():
    N = int(input())

    bojs = []
    otehrs = []

    for _ in range(N):
        study = input().rstrip()

        if study[:7] == "boj.kr/":
            bojs.append(study)
        else:
            otehrs.append(study)

    otehrs.sort(key=lambda x: (len(x), x))
    bojs.sort(key=lambda x: int(x[7:]))

    for other in otehrs:
        print(other)
    for boj in bojs:
        print(boj)


main()
