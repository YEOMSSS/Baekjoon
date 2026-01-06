import sys

input = sys.stdin.readline


def b_search(times: list, target: int) -> int:
    left = 0
    right = min(times) * target

    result = 0

    while left <= right:
        mid = (left + right) // 2

        cur = 0
        # 각 심사대에서 이번 mid에 처리할 수 있는 사람의 수
        for t in times:
            cur += mid // t

        # 더 많이 처리할 수 있으면 시간을 줄여도 된다.
        if cur >= target:
            result = mid
            right = mid - 1
        # 더 적게 처리했다면 시간을 늘려야만 한다.
        else:
            left = mid + 1

    return result


def main() -> None:
    N, M = map(int, input().split())
    times = tuple(int(input()) for _ in range(N))
    print(b_search(times, M))


if __name__ == "__main__":
    main()
