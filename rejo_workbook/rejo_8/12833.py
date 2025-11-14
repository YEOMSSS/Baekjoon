# def main():
#     A, B, C = map(int, input().split())

#     result = A
#     for _ in range(C):
#         result ^= B

#     print(result)


# main()


def main():
    A, B, C = map(int, input().split())
    if C % 2:
        print(A ^ B)
    else:
        print(A)


main()
