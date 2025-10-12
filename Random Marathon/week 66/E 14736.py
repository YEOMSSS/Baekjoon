
import sys
input = sys.stdin.readline

def main():
    N, K, A = map(int, input().split())

    result = float("inf")
    for _ in range(N):
        t, s = map(int, input().split())

        temp = 0
        # 콜라 마시는 데 걸리는 시간
        temp += (K + A - 1) // A
        # 쉬는 데 걸리는 시간
        temp += ((K + (t * A) - 1) // (t * A) - 1) * s

        result = min(temp, result)
    print(result)

if __name__ == "__main__":
    main()