# 확인용 코드.. 전부 1이 나온다.
# 아, k가 0이거나 a가 홀수면 a가 나온다.


def temp() -> None:
    a, k = map(int, input().split())
    prev = a
    for _ in range(k):
        a = prev**a
        print(a)
        print(a % (prev + 1))


def main() -> None:

    a, k = map(int, input().split())
    # k가 0인 경우, a가 홀수인 경우 처리
    if not k or a % 2 == 1:
        print(a)
        return

    print(1)


main()
