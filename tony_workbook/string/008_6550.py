import sys

input = sys.stdin.readline


def main() -> None:
    while True:
        string = input().rstrip()

        if not string:
            return

        find, original = string.split()

        i = 0
        for ch in original:
            if ch != find[i]:
                continue
            i += 1

            if i == len(find):
                print("Yes")
                break

        else:
            print("No")


main()
