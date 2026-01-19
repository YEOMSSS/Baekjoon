def func(N: int, M: int) -> None:

    if M > N:
        N, M = M, N

    print((N - 1) + (M - 1) * N)


if __name__ == "__main__":
    N, M = map(int, input().split())
    func(N, M)
