import sys

input = sys.stdin.readline


def main() -> None:
    string, K = input().split()
    string = string.lower()
    K = int(K)

    check_set = set()

    prev = string[0]
    cnt = 1

    result = []
    for ch in string[1:]:

        if ch == prev:
            cnt += 1
        else:
            if prev not in check_set:
                if cnt >= K:
                    result.append(1)
                else:
                    result.append(0)

            check_set.add(prev)
            prev = ch
            cnt = 1

    if string[-1] not in check_set:
        if cnt >= K:
            result.append(1)
        else:
            result.append(0)

    print("".join(map(str, result)))


main()
