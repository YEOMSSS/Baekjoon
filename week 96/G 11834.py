# Authored by : marigold2003
# Date : 2026-04-03
# Link : https://www.acmicpc.net/problem/11834


import sys

input = sys.stdin.readline


# [Summary] 홀짝

# 홀수 1개, 짝수 2개, 홀수 3개... 로 이뤄진 수열이 있다.
# 1 2 4 5 7 9 10... 으로 진행될 때, N(<= 10*100)번째 원소를 구하시오.


def main() -> None:

    # [Ideas]

    # 내가 잘못보고있나, 10**100은 뭐야;;
    # 일단 확실한건, 절대로 다 만들순 없다는거다.
    # 수학적인 공식이 존재할 텐데...

    # 일단 N이 어떤 덩어리에 들어가는지를 알아야 한다.
    # 이거만 알면 숫자는 쉽게 구할 수 있다.
    # 홀수면 앞에있는 짝수덩어리수만큼 앞으로 가서 그냥 홀수배열 인덱스 출력하고
    # 짝수면 앞에있는 홀수덩어리수만큼 앞으로 가서 그냥 짝수배열 인덱스 출력하면 된다.

    # 덩어리를 어떻게 구하지? 1+2+3+4+...
    # 그 공식 있잖아. (1+N)N/2. 가장 가까운 N을 찾아야한다.
    # 오, 이분탐색?

    ##########

    N = int(input())

    # 몇번째 덩어리인지 찾기. n(n+1)//2
    def b_search(N: int) -> int:
        left = 0
        right = N

        result = -1

        flag = False
        while left <= right:
            mid = (left + right) // 2

            curr = (mid * (mid + 1)) // 2
            # 원소가 남았으면 덩어리를 늘려봐도 된다.
            if curr <= N:
                result = mid
                left = mid + 1

                if curr == N:
                    flag = True
            # 쓸 수 있는 원소를 넘었다면 덩어리 수를 줄여야만 한다.
            else:
                right = mid - 1

        if flag:
            result -= 1
        return result + 1

    locate = b_search(N)

    # 현재 덩어리가 짝수면
    if not locate % 2:
        print((N * 2) - (2 * (locate // 2)))
    # 현재 덩어리가 홀수면
    else:
        print((N * 2 - 1) - (2 * (locate - 1) // 2))

    ##########

    return


# [Review]

# 오, 뭔가 맞는거같아! 수학 싫어!
# 이분탐색은 좋아!!


if __name__ == "__main__":
    main()
