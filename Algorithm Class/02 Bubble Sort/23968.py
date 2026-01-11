
def main():
    N, K = map(int, input().split())
    arr_N = list(map(int, input().split()))

    cnt = 0
    for i in range(N):
        for j in range(N - i - 1):
            if arr_N[j] > arr_N[j + 1]:
                arr_N[j], arr_N[j + 1] = arr_N[j + 1], arr_N[j]
                cnt += 1

                if cnt == K:
                    print(arr_N[j], arr_N[j + 1])
                    return
    print(-1)
    return

if __name__ == "__main__":
    main()

# 개 쉽네... ㅈ같은 c언어...