import sys

input = sys.stdin.readline

vowels = set("aeiou")


def main() -> None:
    while True:
        string = input().rstrip().lower()
        if string == "#":
            return

        count = 0
        for ch in string:
            if ch in vowels:
                count += 1

        print(count)


if __name__ == "__main__":
    main()
