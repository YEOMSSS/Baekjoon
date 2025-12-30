def main() -> None:
    x = int(input())

    match x % 3:
        case 1:
            print("U")
        case 2:
            print("O")
        case 0:
            print("S")


main()
