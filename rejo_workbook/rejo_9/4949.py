import sys

input = sys.stdin.readline


def func(string):
    stack = []

    for ch in string:
        match ch:
            case "(" | "{" | "[":
                stack.append(ch)
            case ")":
                if not stack:
                    return 1
                if stack[-1] != "(":
                    return 1
                stack.pop()
            case "}":
                if not stack:
                    return 1
                if stack[-1] != "{":
                    return 1
                stack.pop()
            case "]":
                if not stack:
                    return 1
                if stack[-1] != "[":
                    return 1
                stack.pop()
            case _:
                pass
    if stack:
        return 1

    return 0


def main():
    while True:
        string = input().rstrip()
        if string == ".":
            break

        if func(string):
            print("no")
        else:
            print("yes")


main()
