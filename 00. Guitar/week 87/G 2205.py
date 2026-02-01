# Authored by : marigold2003
# Date : 2026-02-01
# Link : https://www.acmicpc.net/problem/2205

import sys

input = sys.stdin.readline


# [Summary]

# 1~N의 무게를 가진 납덩어리에 1~N의 무게를 가진 주석덩어리를 합친다.
# 합친 결과는 모두 2의 거듭제곱이 되어야 한다.
# 1~N의 납에 합친 주석의 무게를 순서대로 출력하자.


def main():

    # [Ideas]

    # 11
    # 11 22
    # 13 22 31
    # 13 22 31 44
    # 11 22 35 44 53
    # 11 26 35 44 53 62
    # 17 26 35 44 53 62 71
    # 17 26 35 44 53 62 71 88

    # 뭔가 냄새가 나잖아.
    # 제일 큰 것부터 확인해서, 2의 거듭제곱을 만드는 제일 큰 짝꿍을 찾는다. 그리고 짝꿍까지 뒤집는다.
    # 이제 남은 애들로 반복하면 된다.

    ##########

    N = int(input())
    answer = list(range(N + 1))

    while N > 1:
        # 2**14 = 16384
        for i in range(15):
            temp = 2**i
            if N < temp:
                break

        # 이미 2의 거듭제곱이면 건너뛰어도 된다.
        if N == temp:
            N -= 1
            continue

        # 짝꿍 찾아서 뒤집기
        answer[temp - N : N + 1] = answer[temp - N : N + 1][::-1]

        # 짝꿍 앞부터 다시 확인
        N = temp - N - 1

    print("\n".join(map(str, answer[1:])))

    ##########

    return


# [Review]

# 발상이 생각보다 쉬웠다. 근데 구현 너무 오래걸렸음.
# 구현 연습을 더 많이 해야한다.

if __name__ == "__main__":
    main()
