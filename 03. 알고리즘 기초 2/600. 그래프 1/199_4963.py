'''
문제
정사각형으로 이루어져 있는 섬과 바다 지도가 주어진다.
섬의 개수를 세는 프로그램을 작성하시오.

한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다. 

두 정사각형이 같은 섬에 있으려면, 한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있어야 한다.
지도는 바다로 둘러싸여 있으며, 지도 밖으로 나갈 수 없다.

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다.
각 테스트 케이스의 첫째 줄에는 지도의 너비 w와 높이 h가 주어진다.
w와 h는 50보다 작거나 같은 양의 정수이다.

둘째 줄부터 h개 줄에는 지도가 주어진다. 1은 땅, 0은 바다이다.

입력의 마지막 줄에는 0이 두 개 주어진다.

출력
각 테스트 케이스에 대해서, 섬의 개수를 출력한다.

예제 입력 1 
1 1
0
2 2
0 1
1 0
3 2
1 1 1
1 1 1
5 4
1 0 1 0 0
1 0 0 0 0
1 0 1 0 1
1 0 0 1 0
5 4
1 1 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 1 1
5 5
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0
예제 출력 1 
0
1
1
3
1
9
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

while True:
    W, H = map(int, input().split())
    if W == 0 and H == 0:
        break

    MAPs = [list(map(int, input().split())) for _ in range(H)]

    graph = [[] for _ in range(W * H)]

    for row in range(H):
        for col in range(W):
            if MAPs[row][col] == 1:
                # 우측
                if col + 1 < W and MAPs[row][col + 1] == 1:
                    graph[row * W + col].append(row * W + (col + 1))
                    graph[row * W + (col + 1)].append(row * W + col)
                # 하단
                if row + 1 < H and MAPs[row + 1][col] == 1:
                    graph[row * W + col].append((row + 1) * W + col)
                    graph[(row + 1) * W + col].append(row * W + col)
                # 좌하단
                if 0 <= col - 1 and row + 1 < H and MAPs[row + 1][col - 1] == 1:
                    graph[row * W + col].append((row + 1) * W + (col - 1))
                    graph[(row + 1) * W + (col - 1)].append(row * W + col)
                # 우하단
                if col + 1 < W and row + 1 < H and MAPs[row + 1][col + 1] == 1:
                    graph[row * W + col].append((row + 1) * W + (col + 1))
                    graph[(row + 1) * W + (col + 1)].append(row * W + col)

    visited = [False] * (W * H + 1)

    def dfsR(node):
        if visited[node]:
            return
        
        visited[node] = True
        for neighbor in graph[node]:
            dfsR(neighbor)

    answer = 0
    for i in range(W * H):
        if not visited[i] and MAPs[i // W][i % W] == 1:
            dfsR(i)
            answer += 1

    print(answer)

    

    