import sys

input = sys.stdin.readline


def func():
    N, X, Y = map(int, input().split())
    V = list(map(int, input().split()))

    fastest = float("inf")

    if max(V) == V[N - 1]:
        print(0)
        return

    V_time = []
    for i in range(N - 1):
        my_time = X / V[i]
        V_time.append(my_time)
        fastest = min(fastest, my_time)

    N_speed = V[N - 1]
    N_time = X / N_speed

    boost = 0
    while boost <= Y:
        N_time = (X - boost) / N_speed + 1

        if N_time < fastest:
            print(boost)
            return

        boost += 1

    print(-1)


def main():
    T = int(input())

    for _ in range(T):
        func()


if __name__ == "__main__":
    main()
