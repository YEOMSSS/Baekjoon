# https://www.acmicpc.net/problem/15873

# 경우가 뭐가있을까? 1~10이 2개들어오는데 붙어들어온다.
# 1010 길이4
# 101, 110 길이3일때 i1이 0이거나 i2가 0이거나.
# 11 길이2면 그냥 반으로.


def main() -> None:
    string = input().rstrip()
    length = len(string)

    if length == 4:
        print(20)
    elif length == 3:
        if string[1] == "0":
            print(10 + int(string[2]))
        else:  # string[2] == "0"
            print(int(string[0]) + 10)
    else:  # len == 2
        print(int(string[0]) + int(string[1]))


main()
