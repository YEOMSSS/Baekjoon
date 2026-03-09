# Authored by : marigold2003
# Date : 2026-03-06
# Link : https://www.acmicpc.net/problem/20311


import sys

input = sys.stdin.readline


# [Summary] 화학 실험

# N(300K)개의 시험관이 일렬로 나열되어 있다.
# 색은 K(<=N)종류 있으며, 색깔별로 시약의 수가 주어진다.
# 조건을 만족하는 시험관 배열을 만들 수 있으면 색깔 번호를 출력하시오.


def main() -> None:

    # [Ideas]

    # 일단 시약이 많은 색을 먼저 소모하는 게 좋겠다.
    # 그래, 그거다! 힙이구나, 이거!
    # 최대힙에 색들을 다 밀어넣고, 많은거부터 꺼내쓰면 되겠구나.

    # 처리할 포인트는, 같은 색을 연속해서 뽑지 못하게 하는 거지.
    # 만약 같은 걸 뽑았다면, 한번 더 꺼내는 방식으로 해야겠다.

    # 아니면 두개씩 꺼내면 되지 않을까?
    # 순서대로 heappop 두번 하고 1씩 빼서 다시 집어넣는 식으로.
    # 그러면 힙에는 (cnt, id)로 들어가야겠다.

    ##########

    import heapq

    N, K = map(int, input().split())

    # 색이 하나인데 시험관이 2개 이상이면 바로 탈락
    if K == 1 and N >= 2:
        print(-1)
        return

    counts = list(map(int, input().split()))
    max_heap = []
    for i in range(K):
        heapq.heappush(max_heap, (-counts[i], i + 1))

    answer = []
    # N//2번 돌리면 홀수일때 하나 남는다.
    for _ in range(N // 2):
        # 일단 제일 많은걸 꺼낸다.
        cnt1, nid1 = heapq.heappop(max_heap)
        if cnt1:
            answer.append(nid1)

        # 다음으로 많은걸 꺼낸다.
        cnt2, nid2 = heapq.heappop(max_heap)
        # 못꺼내면 바로 탈락
        if cnt2:
            answer.append(nid2)
        else:
            print(-1)
            return

        # 최소힙으로 돌아가고있으니 그냥 +1해버렸다.
        heapq.heappush(max_heap, (cnt1 + 1, nid1))
        heapq.heappush(max_heap, (cnt2 + 1, nid2))

    # 홀수일 때 남은 하나 처리
    cnt, nid = heapq.heappop(max_heap)
    if cnt:
        answer.append(nid)

    print(*answer)

    ##########

    return


# [Review]

# 그리디라서 최대힙으로 쉽게 풀었다.
# 그냥 정렬로도 풀 수 있을듯.


if __name__ == "__main__":
    main()
