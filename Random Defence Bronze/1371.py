import sys

from collections import Counter


def main() -> None:
    string = sys.stdin.read()

    string_counter = Counter(string)

    result = []
    temp = 0
    for key, value in string_counter.most_common(len(string_counter)):
        if key == " " or key == "\n":
            continue

        if not temp:
            temp = value

        if temp == value:
            result.append(key)
        else:
            break

    print("".join(sorted(result)))


if __name__ == "__main__":
    main()
