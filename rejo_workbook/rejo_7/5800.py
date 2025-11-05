import sys

input = sys.stdin.readline


def main():
    K = int(input())
    for i in range(K):
        input_list = list(map(int, input().split()))

        N = input_list[0]
        scores = sorted(input_list[1:], reverse=True)

        gap_max = 0
        for j in range(N - 1):
            gap_max = max(gap_max, scores[j] - scores[j + 1])

        print(f"Class {i + 1}")
        print(f"Max {scores[0]}, Min {scores[-1]}, Largest gap {gap_max}")


main()
