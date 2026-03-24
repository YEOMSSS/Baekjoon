# Authored by : marigold2003
# Date : 2026-03-23
# Link : https://www.acmicpc.net/problem/27312


import sys

input = sys.stdin.readline


# [Summary] 운영진에게 설정 짜기는 어려워

# 인터렉티브 문제다.

# 캐릭터의 설정은 N(<= 1K)개이다.
# i번째 속성의 값은 1 ~ ai(<= 1K) 정수로 표현된다.
# 어떤 두 캐릭터의 N개의 속성의 값이 모두 동일하면 두 캐릭터의 설정은 겹친다.

# 이미 만들어진 M(<= Q)개의 캐릭터가 있다.
# 누구와도 설정이 겹치지 않는 새로운 캐릭터를 만들고자 한다.

# k번째 캐릭터의 i번째 속성의 값을 묻는 질문이 Q(<= N)회 할 수 있다.
# Q번 이하 질문으로 캐릭터를 생성하시오.


def main() -> None:

    # [Ideas]

    # 질문을 잘 써야 한다.
    # 만들어진 캐릭터보다는 질문이 많다.
    # 속성의 가짓수도 만들어진 캐릭터보다 많다.

    # 한 캐릭터와 딱 하나의 속성값만 달라도 다른 설정이잖아.
    # i번째 캐릭터의 i번째 속성과 다른 속성값을 가지면 된다.
    # 인터렉티브만 잘 짜보자.

    ##########

    M, N, Q = map(int, input().split())
    A = list(map(int, input().split()))

    answer = [1] * N

    # 질문은 캐릭터 수만큼만 하면 된다.
    for i in range(M):
        print(f"? {i+1} {i+1}", flush=True)

        result = int(input())

        if result == 1:
            answer[i] = 2

    print("!", *answer, flush=True)

    ##########

    return


# [Review]

# 인터렉티브는 오랜만이네.
# 재밌게 풀었다.


if __name__ == "__main__":
    main()
