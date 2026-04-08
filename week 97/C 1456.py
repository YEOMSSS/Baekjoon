# Authored by : marigold2003
# Date : 2026-04-08
# Link : https://www.acmicpc.net/problem/1456


import sys

input = sys.stdin.readline


# [Summary] 거의 소수

# 어떤 수가 소수의 N제곱꼴일때, 그 수는 거의 소수라고 한다.
# A 이상 B 이하인 거의 소수가 몇 개인지 구하시오. (<= 10**14)


def main() -> None:

    # [Ideas]

    # 일단 소수 본인은 제외된다는 점이 포인트.
    # 그러면 소수판정을 10**7까지만 해주면 된다.
    # 그리고 걔들을 제곱해놓은 리스트를 하나 뽑아주면 끝.

    # 뭐, 1~루트B까지 찾는단 마인드.
    # 근데 N제곱꼴인게 좀 그러네, 모든 소수에 대해서 다 해봐야하겠지?
    # 뭐, 할만할거같기도 하고.

    ##########

    def sieve(n):
        # 입력: n (정수)
        # 상태: 0~n까지 소수 여부 배열
        is_prime = [True] * (n + 1)

        # 조건: 0,1은 소수가 아님 (불변량 정리)
        if n >= 0:
            is_prime[0] = False
        if n >= 1:
            is_prime[1] = False

        # 연산: i <= sqrt(n) 까지만 배수 제거
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:  # 아직 제거되지 않았다면
                # 상태 변화: i의 배수 제거
                for multiple in range(i * i, n + 1, i):
                    is_prime[multiple] = False

        # 결과 확인: True인 인덱스만 반환
        return [i for i in range(2, n + 1) if is_prime[i]]

    A, B = map(int, input().split())
    primes = sieve(int(B**0.5) + 1)

    count = 0

    for p in primes:
        square = p
        square *= p
        while square <= B:
            if A <= square:
                count += 1
            square *= p

    print(count)

    ##########

    return


# [Review]

# 시간초과가 걱정이긴 한데
# 로그로 겁나 줄여놨으니 뭐... 괜찮겠지.


if __name__ == "__main__":
    main()
