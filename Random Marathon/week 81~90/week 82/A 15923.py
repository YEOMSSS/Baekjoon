import sys

input = sys.stdin.readline


def main():
    T = int(input())

    result = 0
    first_x, first_y = tuple(map(int, input().split()))
    prev_x, prev_y = first_x, first_y

    for _ in range(T - 1):
        cur_x, cur_y = tuple(map(int, input().split()))

        result += abs(prev_x - cur_x) + abs(prev_y - cur_y)
        prev_x, prev_y = cur_x, cur_y

    result += abs(first_x - cur_x) + abs(first_y - cur_y)
    print(result)


main()
