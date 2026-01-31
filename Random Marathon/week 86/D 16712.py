import sys

input = sys.stdin.readline


def main() -> None:

    # 참가자 N, 대회당 참가자 M
    N, M = map(int, input().split())
    levels = tuple(map(int, input().split()))
    contests = tuple(map(int, input().split()))

    current_contest = list(levels[:M])
    idx = M

    for v in contests:
        current_contest.sort()
        if idx == N:
            current_contest[v - 1] = 0
            continue
        current_contest[v - 1] = levels[idx]
        idx += 1

    current_contest.sort()
    print(*current_contest[1:])


if __name__ == "__main__":
    main()
