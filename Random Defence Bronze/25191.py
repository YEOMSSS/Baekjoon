def main() -> None:

    # 최대 치킨, 콜라수(0.5치킨), 맥주수(1치킨)
    N = int(input())
    A, B = map(int, input().split())

    temp = A // 2 + B
    print(min(N, temp))


if __name__ == "__main__":
    main()
