def main():
    string = input().rstrip()

    stack = []

    for ch in string:
        match ch:
            case "(":
                stack.append("(")
            case ")":
                if not stack or stack[-1] == ")":
                    stack.append(")")
                if stack[-1] == "(":
                    stack.pop()

    print(len(stack))


main()
