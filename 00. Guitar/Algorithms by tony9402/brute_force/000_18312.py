def main() -> None:
    N, K = map(int, input().split())

    cnt = 0

    # K==0일때를 따로 처리한다.
    if K == 0:
        for h in range(N + 1):
            if h <= 10 or h % 10 == 0:
                cnt += 3600
                continue
            for m in range(60):
                if m <= 10 or m % 10 == 0:
                    cnt += 60
                    continue
                for s in range(60):
                    if s <= 10 or s % 10 == 0:
                        cnt += 1

    else:
        K = str(K)
        for h in range(N + 1):
            if K in str(h):
                cnt += 3600
                continue
            for m in range(60):
                if K in str(m):
                    cnt += 60
                    continue
                for s in range(60):
                    if K in str(s):
                        cnt += 1

    print(cnt)


main()
