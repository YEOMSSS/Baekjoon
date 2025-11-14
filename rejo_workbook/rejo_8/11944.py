def main():
    n, M = map(int, input().split())

    N = str(n)
    if len(N) * n > M:
        print(N * (M // len(N)), end="")
        print(N[: M % len(N)])
    else:
        print(N * n)


main()

"""
# 브루트포스

def main():
    N, M = input().split()

    arr = N * int(N)

    print(arr[: int(M)])


main()
"""
