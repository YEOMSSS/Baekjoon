string = "WelcomeToSMUPC"
length = len(string)


def main() -> None:
    N = int(input())

    # 나머지 0이어서 -1되도 처리가 된다는거임
    print(string[(N) % length - 1])


main()
