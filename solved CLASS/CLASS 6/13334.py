# Authored by : marigold2003
# Date : 2026-04-06
# Link : https://www.acmicpc.net/problem/13334


import sys

input = sys.stdin.readline


# [Summary] 철로

# 수직선 위에 선분이 N(<= 100K)개 있다.
# 길이가 d(<= 200M)인 범위 L이 있을 때,
# 범위에 포함된 선분의 수의 최댓값을 출력하시오.


def main() -> None:

    # [Ideas]

    # 그냥 슬라이딩윈도우처럼 투포인터로 정해진 선분 길이만큼 민다고 처음에 생각.
    # 그런데 좀 보니까, 그 안에 얼마나 많은 선분이 포함되어 있는지 판단하기가 쉽지가 않다.
    # 알고리즘을 까보니 힙이랑 스위핑이 들어있다. 정렬하고 쓰는걸로 한번에 털린다고 이게?
    # 쭉쭉 밀면서 힙으로 뭘 관리해야 하는 것인가??

    # 일단 선분을 시작~끝 정해놓고, 큰게 선분 안에 들어오면 작은게 선분 안에 있는지 확인하고 힙에 넣자.
    # 그러고 힙의 탑을 계속 확인하면서 지나갈때마다 털어주면 되겠는데?
    # 계속 선분 내부가 정렬되어야 한다는게 포인트니까, 그걸 최소힙으로 관리하면 된다.

    # 그러면... 선분 끝점기준으로 오름차정렬하고, 힙에는 선분 시작점으로 넣어주면 되겠구만.
    # 아니면 아예 L보다 긴 선분은 다 털어버리자. 그러면 넣을때 시작점 확인할필요 없겠네.

    # 일단 짜봐. 대충 그림 그려진다. 아, 선분 양끝점 입력이 오름차순이 아니군.

    # 근데 또 문제가 있네? 범위가 너무 넓어서 슬라이딩윈도우는 안돼.
    # 입력된 선분들을 기준으로 스위핑을 해야한다. 이건 어떻게하지?
    # 아, 범위의 끝을 당기는 방식으로 진행하고 있으니 차이만큼 더해주면 되겠네. 간만큼.
    # 이건 좀 짜보면서 해야겠는데. 글로만은 헷갈린다.

    ##########

    import heapq

    N = int(input())
    temp_lines = [map(int, input().split()) for _ in range(N)]
    L = int(input())

    lines = []
    for a, b in temp_lines:
        if abs(a - b) > L:
            continue
        if a > b:
            a, b = b, a
        lines.append((a, b))
    lines.sort(key=lambda x: x[1])
    N = len(lines)

    if not N:
        print(0)
        return

    if N == 1:
        print(1)
        return

    min_heap = []

    # end보다 b가 작으면 다 넣는다.
    # start보다 a가 작으면 다 꺼낸다.
    heapq.heappush(min_heap, lines[0][0])
    answer = 1
    d_end = lines[1][1] + 1
    d_start = d_end - L - 1

    i = 1
    while i < N:
        while i < N and lines[i][1] < d_end:
            heapq.heappush(min_heap, lines[i][0])
            i += 1

        while min_heap and min_heap[0] < d_start:
            heapq.heappop(min_heap)

        answer = max(answer, len(min_heap))

        if i < N:
            d_end = lines[i][1] + 1
            d_start = d_end - L - 1

    print(answer)

    ##########

    return


# [Review]

# 문제가 재밌네. 생각할 것도 있고 구현하기도 좋다.
# 반례도 좀 잡아야 하고 말이지.
# 좋은 스위핑 문제다. 힙을 이용해서 스위핑을 관리하는 생각할 게 있는 문제.


if __name__ == "__main__":
    main()
