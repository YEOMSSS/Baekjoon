def main():
    clock = input().rstrip()

    result = [[".", ".", ".", "."] for _ in range(4)]

    for i in range(4):
        check = 3
        for n in bin(int(clock[i]))[::-1]:
            if n == "b":
                break
            if n == "1":
                result[check][i] = "*"
            check -= 1

    for row in result:
        print(*row[:2], " ", *row[2:])


main()
