# Authored by : marigold2003
# Date : 2026-04-04
# Link : https://www.acmicpc.net/problem/19241


import sys

input = sys.stdin.readline


# [Summary] 해적과 보석

# 보물이 N(100K)개 있다. A와 B는 번갈아가며 보물을 하나씩 가진다.
# 각 보물에 대해 느끼는 가치는 서로 다르다.
# 자신이 챙기고 자기가 느끼는 보물의 가치 빼기
# 상대가 챙기고 상대가 느끼는 보물의 가치가
# 최대한 크게 하도록 보물을 가져간다.
# A의 가치 - B의 가치를 구하시오.


def main() -> None:

    # [Ideas]

    # 그리디인건 알겠다. 이해는 쉬움.
    # 각자의 기준에 따라 정렬한 리스트가 두 개 생긴다.
    # 그럼 보물을 가져갈때 두 리스트에서 모두 없애야 하는데.
    # 이 부분을 해결하는 것이 중요해 보임.

    # 각 리스트에서 pop(i)를 계속 하는건 너무 빡쎄. O(N**2)는 에바다.
    # 전부 정리된게 하나 있으면 좋겠는데. 딕셔너리든 리스트든.

    # 음, 오케이. 일단 A를 정렬하자.
    # 그리고 A에서의 보물이 B에 어디있는지를 딕셔너리로 만들어두자.
    # 양쪽 다 해두자고. 이것도 어렵긴 하겠지만... O(N)으로 할 수 있을듯함.

    # 상대가 좋은 걸 가져가지 못하게 견제하는 것도 포함되어야 하는구나.
    # 설마 절댓값만 정렬해도 답이 나오는건 아니겠지...? 제발 아니라고 해다오

    # 그럼 신경써야할게 좀 생긴다.
    # 내가 비싸다고 하는거 챙기기 또는 쟤가 비싸다고 생각하는거 뺏기.
    # 내가 느끼기에 싼데 쟤가 느끼기에 비싼 걸 먼저 챙겨야 한다. 오!

    # 그럼 A가치-B가치를 하면 되겠네. 클수록 A에 이득, 작을수록 B에 이득. 헐.
    # 양쪽에서 pop하려면 deque가 좋겠는걸?

    # 아니면... 설마 둘이 합쳐버리면 그만인거냐?
    # 진짜 이거라고? 왜 예제가 맞지 이거? 허어어...
    # 이 물건에 부여된 가치가 최대인 것부터 챙긴다고 생각하면, 그런 거냐...

    ##########

    T = int(input())

    def func():
        N = int(input())
        Treasures = []

        for _ in range(N):
            a, b = map(int, input().split())
            Treasures.append((a, b))

        Treasures.sort(key=lambda x: x[0] + x[1])

        Ares = 0
        Bres = 0

        for i in range(N):

            Tmax = Treasures.pop()

            if i % 2 == 0:
                Ares += Tmax[0]

            else:
                Bres += Tmax[1]

        print(Ares - Bres)

    for _ in range(T):
        func()

    ##########

    return


# [Review]

# 증명이 어려운


if __name__ == "__main__":
    main()


# 견제를 생각하지 않은 경우인 아쉬운 코드.
"""
    T = int(input())

    def func():
        N = int(input())

        Avals = []
        Bvals = []

        for i in range(N):
            a, b = map(int, input().split())
            Avals.append((a, i))
            Bvals.append((b, i))

        Avals.sort()
        Bvals.sort()

        i_List = [[] for _ in range(N)]

        for i, (_, orig) in enumerate(Avals):
            i_List[orig].append(i)
        for i, (_, orig) in enumerate(Bvals):
            i_List[orig].append(i)

        A_to_B = {a: b for a, b in i_List}
        B_to_A = {b: a for a, b in i_List}

        Aresult = 0
        Bresult = 0

        Asize = N - 1
        Bsize = N - 1

        while True:
            Amax = Avals.pop()[0]

            while Amax == -1:
                if not Avals:
                    print(Aresult - Bresult)
                    return
                Asize -= 1
                Amax = Avals.pop()[0]

            Bvals[A_to_B[Asize]] = (-1,)
            Asize -= 1
            Aresult += Amax

            Bmax = Bvals.pop()[0]

            while Bmax == -1:
                if not Bvals:
                    print(Aresult - Bresult)
                    return
                Bsize -= 1
                Bmax = Bvals.pop()[0]

            Avals[B_to_A[Bsize]] = (-1,)
            Bsize -= 1
            Bresult += Bmax

    for _ in range(T):
        func()
"""
