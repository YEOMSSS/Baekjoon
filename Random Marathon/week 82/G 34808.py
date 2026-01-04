# 난 이런 기믹성 문제가 너 무 싫어.
# 애드혹은 정말 좃같아.

import sys

input = sys.stdin.readline


def main():
    N, M, K = map(int, input().split())

    # 2*2넘기면 불가능
    if N >= 2 and M >= 2:
        print(-1)
        return
    # 여기부터는 N이나 M중 하나는 1이다.
    # 1이 아닌 것을 L로 설정
    L = max(N, M)

    # K = 0 처리
    if K == 0:
        # 인접 칸이 생기면 탈락. 이상과 초과는 공존 불가능
        if L >= 3:
            print(-1)
            return
        # L = 1 or 2: 전부 0 가능
        if N == 1:
            print(*([0] * M))
        else:
            for _ in range(N):
                print("0")
        return

    # K > 0: x[i] = i * K 를 하면 인접칸끼리 K만큼 차이나고, 비인접칸끼리 2K만큽 차이난다.
    result = [i * K for i in range(L)]

    # 1 x M
    if N == 1:
        print(*result)

    # N x 1
    else:
        for r in result:
            print(r)


if __name__ == "__main__":
    main()
