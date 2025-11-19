import sys

input = sys.stdin.readline


def main():
    input()

    result = 0
    count = [0, 0]
    for ch in input().rstrip():
        match ch:
            case "L":
                count[0] += 1
            case "S":
                count[1] += 1
            case "R":
                if count[0]:
                    result += 1
                    count[0] -= 1
                else:
                    break
            case "K":
                if count[1]:
                    result += 1
                    count[1] -= 1
                else:
                    break
            case _:
                result += 1
    print(result)


main()
