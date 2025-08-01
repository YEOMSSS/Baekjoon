'''
문제
BOJ에서 정답이 여러가지인 경우에는 스페셜 저지를 사용한다.
스페셜 저지는 유저가 출력한 답을 검증하는 코드를 통해서 정답 유무를 결정하는 방식이다.
오늘은 스페셜 저지 코드를 하나 만들어보려고 한다.

정점의 개수가 N이고, 정점에 1부터 N까지 번호가 매겨져있는 양방향 그래프가 있을 때,
BFS 알고리즘은 다음과 같은 형태로 이루어져 있다.

큐에 시작 정점을 넣는다. 이 문제에서 시작 정점은 1이다. 1을 방문했다고 처리한다.
큐가 비어 있지 않은 동안 다음을 반복한다.
큐에 들어있는 첫 정점을 큐에서 꺼낸다. 이 정점을 x라고 하자.
x와 연결되어 있으면, 아직 방문하지 않은 정점 y를 모두 큐에 넣는다. 모든 y를 방문했다고 처리한다.
2-2 단계에서 방문하지 않은 정점을 방문하는 순서는 중요하지 않다.
따라서, BFS의 결과는 여러가지가 나올 수 있다.

트리가 주어졌을 때, 올바른 BFS 방문 순서인지 구해보자.

입력
첫째 줄에 정점의 수 N(2 ≤ N ≤ 100,000)이 주어진다.
둘째 줄부터 N-1개의 줄에는 트리의 간선 정보가 주어진다. 마지막 줄에는 BFS 방문 순서가 주어진다.
BFS 방문 순서는 항상 N개의 정수로 이루어져 있으며, 1부터 N까지 자연수가 한 번씩 등장한다.

출력
입력으로 주어진 BFS 방문 순서가 올바른 순서면 1, 아니면 0을 출력한다.

예제 입력 1 
4
1 2
1 3
2 4
1 2 3 4
예제 출력 1 
1
올바른 순서는 1, 2, 3, 4와  1, 3, 2, 4가 있다.

예제 입력 2 
4
1 2
1 3
2 4
1 2 4 3
예제 출력 2 
0
'''
# 모든 bfs탐색경로를 찾을 수는 없다.
# 들어온 입력이 bfs탐색이 가능한지를 판단해야 한다.

import sys
input = sys.stdin.readline

from collections import deque

N = int(input())

graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

check = list(map(int, input().split()))

def bfs():
    visited = [False] * (N + 1)
    queue = deque(check)
    visited[1] = True

    index = 1 # 1은 제외하고 시작이니 check인덱스를 1부터
    while queue:
        current = queue.popleft()
        neighbors = [node for node in graph[current] if not visited[node]]
        # 순서 없이 nei가 올 수 있으니 set으로 비교를...
        if set(neighbors) == set(check[index : index + len(neighbors)]):
            index += len(neighbors) # 비교 후 nei개수만큼 check인덱스 옮겨주기
        else:
            return False

        for neighbor in neighbors:
            visited[neighbor] = True
    
    return True

print(1 if bfs() else 0)

# 아~ 원콤이에요~~~~~