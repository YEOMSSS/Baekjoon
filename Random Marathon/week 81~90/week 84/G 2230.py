import sys

input = sys.stdin.readline


def main() -> None:
    N, M = map(int, input().split())

    arr = list(int(input()) for _ in range(N))
    arr.sort()

    # 같은 수를 선택할 수도 있다.
    left, right = 0, 0
    # answer = sys.maxsize
    answer = 2_000_000_001  # 가능한 최대 차이

    while left < N and right < N:

        gap = arr[right] - arr[left]

        # 차이가 M이 되면 최솟값이니 즉시 종료
        # M이 0일 경우, left와 right의 인덱스가 같기에 바로 retrun된다.
        if gap == M:
            print(M)
            return

        # 차이가 M보다 작으면 오른쪽으로 한칸 늘려 차이를 키운다.
        if gap < M:
            right += 1
            continue

        # 차이가 M보다 크면 왼쪽을 한칸 줄여 차이를 줄인다.
        left += 1
        answer = min(gap, answer)

    print(answer)


if __name__ == "__main__":
    main()
