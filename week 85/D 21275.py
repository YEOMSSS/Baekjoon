import sys

input = sys.stdin.readline


def main() -> None:
    X_base_A, X_base_B = input().split()

    xa_list = [None] * 37
    xb_list = [None] * 37

    len_X_base_A = len(X_base_A)
    len_X_base_B = len(X_base_B)

    for base in range(2, 37):
        temp_xa = 0
        for i, ch in enumerate(X_base_A):
            n = int(ch, 36)
            if n >= base:
                break
            temp_xa += base ** (len_X_base_A - i - 1) * n
        else:
            xa_list[base] = temp_xa

        temp_xb = 0
        for i, ch in enumerate(X_base_B):
            n = int(ch, 36)
            if n >= base:
                break
            temp_xb += base ** (len_X_base_B - i - 1) * n
        else:
            xb_list[base] = temp_xb

    answer = None
    for a in range(2, 37):
        for b in range(2, 37):

            xa = xa_list[a]
            xb = xb_list[b]

            if xa == None or xb == None:
                continue
            if a == b:
                continue

            if xa == xb:
                if answer:
                    print("Multiple")
                    return
                answer = (xa, a, b)

    if answer:
        print(*answer)
    else:
        print("Impossible")


if __name__ == "__main__":
    main()
