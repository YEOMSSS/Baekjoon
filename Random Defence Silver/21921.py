import sys

input = sys.stdin.readline


def main():
    N, X = map(int, input().split())
    arr = list(map(int, input().split()))

    if not sum(arr):
        print("SAD")
        return

    value = sum(arr[:X])
    total, count = value, 1

    # 슬라이딩 윈도우
    for i in range(X, N):
        # 지나온 칸 빼주고, 새로운 칸 더하고
        value += -arr[i - X] + arr[i]

        # 최댓값 뚫리면 갱신
        if total < value:
            total = value
            count = 1

        # 동일할 경우 나온 횟수 증가
        elif total == value:
            count += 1

    print(total)
    print(count)


if __name__ == "__main__":
    main()
