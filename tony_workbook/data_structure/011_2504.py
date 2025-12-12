import sys

input = sys.stdin.readline


def main():
    string = list(input().rstrip())

    stack = []

    # 우선 가능한지 검사
    for ch in string:
        match ch:
            case "(" | "[":
                stack.append(ch)

            case ")":
                if not stack or stack[-1] != "(":
                    print(0)
                    return
                stack.pop()

            case "]":
                if not stack or stack[-1] != "[":
                    print(0)
                    return
                stack.pop()
    if stack:
        print(0)
        return

    # 이전 턴에 열린괄호였다면 True
    flag = False

    def func(n):
        nonlocal flag

        if flag:
            stack.pop()
            stack.append(n)
            flag = False

        else:  # not flag
            tmp = stack.pop()
            stack.pop()
            stack.append(tmp * n)

    # 계산 시작, 스택은 비어있는 상태
    for ch in string:
        match ch:
            case "(" | "[":
                flag = True
                stack.append(ch)

            case ")":
                func(2)

            case "]":
                func(3)

        while len(stack) > 1:
            if type(stack[-1]) != int:
                break
            if type(stack[-2]) != int:
                break
            stack.append(stack.pop() + stack.pop())

    print(*stack)


main()
