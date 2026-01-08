import sys

input = sys.stdin.readline


def main():
    N, K = map(int, input().split())
    temperatures = list(map(int, input().split()))

    value = sum(temperatures[:K])
    result = value

    # 슬라이딩 윈도우
    for i in range(K, N):
        # 지나온 칸 빼주고, 새로운 칸 더하고
        value += -temperatures[i - K] + temperatures[i]

        # 최댓값 뚫리면 갱신
        result = max(value, result)

    print(result)


if __name__ == "__main__":
    main()
