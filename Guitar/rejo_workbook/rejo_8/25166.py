def main():
    S, M = map(int, input().split())

    if S <= 1023:
        print("No thanks")

    elif ~M & (S - 1023):
        print("Impossible")

    else:
        print("Thanks")


main()
