# def main() -> None:
#     N, K = map(int, input().split())

#     for i in range(int(N / 2) + 1):
#         if K == (i + 1) * (N - i + 1):
#             print("YES")
#             return

#     print("NO")


# main()


# 이 문제는 이분탐색이란다!!
def main() -> None:
    N, K = map(int, input().split())

    # hori가 first와 last 사이 범위에 있다고 생각하자.
    first = 0
    last = N // 2

    while first <= last:
        hori = (first + last) // 2
        vert = N - hori
        # print(hori, vert)

        piece = (hori + 1) * (vert + 1)

        if piece == K:
            print("YES")
            return

        # 조각 수가 부족하면 범위를 큰 쪽으로 좁힌다.
        # hori가 지금 hori보단 커져야 하니까 1을 더해서 first를 재설정해준다.
        if K > piece:
            first = hori + 1
        # 조각 수가 넘치면 범위를 작은 쪽으로 좁힌다.
        # hori가 지금 hori보단 작아져야 하니까 1을 빼서 last를 재설정해준다.
        else:  # K < piece
            last = hori - 1

    print("NO")


main()
