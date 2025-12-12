import sys

input = sys.stdin.readline


# 중심좌표를 오름차순으로 정리해서 확인하면
# 1, 2번원끼리 가능한 경우 3번원은 1번원을 확인할 필요가 없음.
# 2번원이랑 안닿으면 1번이랑은 당연히 닿지 않을 것이다.
# 교점이 같으면 반지름 오름차순 정렬이 필요.

# 어? 반지름이 엄청 큰놈이 앞에 있으면 걔를 확인해야한다.
# 좌표가 이전이어도 반지름이 현재 원을 넘을 수 있다.
# 겁나 큰 원 안에 나머지 작은 원들이 다 들어가는 경우도 있겠는데.

# 정렬을 반지름 순서로 해야하나 이거? 쉬운 문제가 아니었다.
# 원을 x축 위에 압축한다고 생각해보자.
# 그러면 x위에 수평선으로 나타낼 수 있고, 선들끼리 걸쳐지면 안 된다.
# 완전히 겹쳐있거나 아예 닿지 않거나.
# 이러면 괄호 문제랑 비슷하게 생각할 수 있겠는데? 괄호의 종류가 원의 개수만큼 있는거다.


# 어떻게 input을 괄호로 바꿀 수 있을까? 바꾸기만 하면 판별은 쉽다.
# 012332145540667887 이런느낌으로 만들고 싶은데.
# (0, x-r), (0, x+r) 이런느낌으로 스택에 밀어넣고 [1]기준 정렬해야겠다.
def main() -> None:
    N = int(input())

    # 괄호 형태로 만들기
    x_r_list = []
    for i in range(N):
        x, r = map(int, input().split())
        x_r_list.append((i, x - r))
        x_r_list.append((i, x + r))

    x_r_list.sort(key=lambda x: x[1])

    # 괄호 검사
    stack = []
    for x, r in x_r_list:
        if not stack or stack[-1] != x:
            stack.append(x)
            continue

        stack.pop()

    if stack:
        print("NO")
    else:
        print("YES")


main()
