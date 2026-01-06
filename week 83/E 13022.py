import sys

input = sys.stdin.readline

from itertools import groupby


def main():
    string = input().rstrip()

    prev = "f"
    prev_len = 0

    for ch, group in groupby(string):

        # groupby iterator는 len()을 사용할 수 없다.
        current_len = sum(1 for _ in group)

        if prev == "f" and ch == "w":
            prev_len = current_len
            prev = ch

        elif (
            (prev == "w" and ch == "o")
            or (prev == "o" and ch == "l")
            or (prev == "l" and ch == "f")
        ):
            if current_len != prev_len:
                break
            prev = ch

        else:
            break

    else:
        print(1 if prev == "f" else 0)
        return

    print(0)


if __name__ == "__main__":
    main()
