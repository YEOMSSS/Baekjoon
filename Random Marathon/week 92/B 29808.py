# Authored by : marigold2003
# Date : 2026-03-04
# Link : https://www.acmicpc.net/problem/29808


import sys

input = sys.stdin.readline


# [Summary] 너의 수능 점수가 궁금해

# 학번이 입력된다.
# 국어점수가 영어점수보다 높다면, 두 점수의 차에 508을 곱한다.
# 국어점수가 영어점수보다 낮거나 같다면, 두 점수의 차에 108을 곱한다.
# 수학점수가 탐구점수보다 높다면, 두 점수의 차에 212를 곱한다.
# 수학점수가 탐구점수보다 낮거나 같다면, 두 점수의 차에 305를 곱한다.
# 두 값을 더한 뒤, 4763을 곱하면 학번이 나온다.

# 국어와 영어 점수의 차와 수학과 탐구 점수의 차를 출력하시오.
# 가능한 경우가 여러가지일 경우, 전부 출력하시오.


def main() -> None:

    # [Ideas]

    # 뭐, 간단해보이는 문제다. 거꾸로 타고 올라가면 될 거 같음.
    # 학번을 일단 //4763을 해주자.

    # 그리고 그걸 두가지로 나누는 모든 경우를 재봐야하려나?
    # 아니다, 305의 배수를 빼서 508이나 108의 배수가 나오는지 확인하거나
    # 212의 배수를 빼서 508이나 108의 배수가 나오는지 전부 확인해보자.

    # 가능한 모든 경우를 담은 리스트를 정렬해서 출력하자.

    ##########

    number = int(input())
    if number % 4763 != 0:
        print(0)
        return
    number //= 4763

    answer = set()

    # 305에 대해 (차가 0인 경우 포함됨)
    for i in range(0, min(number // 305, 200) + 1):
        curr = number - (i * 305)

        if curr % 508 == 0:
            temp = curr // 508
            if 0 < temp <= 200:
                answer.add((curr // 508, i))

        if curr % 108 == 0:
            temp = curr // 108
            if 0 <= temp <= 200:
                answer.add((curr // 108, i))

    # 212에 대해
    for i in range(1, min(number // 212, 200) + 1):
        curr = number - (i * 212)

        if curr % 508 == 0:
            temp = curr // 508
            if 0 < temp <= 200:
                answer.add((curr // 508, i))

        if curr % 108 == 0:
            temp = curr // 108
            if 0 <= temp <= 200:
                answer.add((curr // 108, i))

    print(len(answer))
    if not answer:
        return
    answer = sorted(answer)
    for a, b in answer:
        print(a, b)

    ##########

    return


# [Review]

# 구현하기 재밌는 문제
# 아니 근데 당연히 4763의 배수일거라고 생각했죠...
# 아, 최소공배수일수도 있네? 하...

# 브루트포스 할껄!!!
# 201 * 201 * 2 * 2 = 160K ;;;;;;


if __name__ == "__main__":
    main()
