import sys

input = sys.stdin.readline


def main():
    N = int(input())

    line = [int(input()) for _ in range(N)]

    # stack에는 (키, 같은키연속횟수)로 저장됨
    # 이 스택에서 키는 항상 내림차순으로 쌓이게 된다. 중요한 포인트.
    stack = []
    result = 0

    # 앞사람부터 순서대로 쌓아갈거다.
    for p in line:

        # 더 키가 큰사람이 오면 더이상 못본다.
        while stack and stack[-1][0] < p:
            # 쌓아온거 합쳐주고 pop
            result += stack.pop()[1]

        # 스택이 비었으면 그냥 push하고 continue
        if not stack:
            stack.append((p, 1))
            continue

        # 키가 같으면 볼 수 있으니까 쌓아온거 합쳐준다.
        if stack[-1][0] == p:
            cnt = stack.pop()[1]
            result += cnt

            # 앞에 나보다 큰사람이 있으면 날 볼 수 있다.
            if stack:
                result += 1

            # 키 연속을 증가한 걸 다시 넣어준다.
            stack.append((p, cnt + 1))

        # 더 키가 작은사람이 오면 그냥 push하고 1쌍 추가.
        else:
            stack.append((p, 1))
            result += 1

    print(result)


main()

# 논리가 좀 어렵다. 뭐랄까 난해하네.
