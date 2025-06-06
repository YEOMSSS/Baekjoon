'''
문제
효주는 포도주 시식회에 갔다. 
그 곳에 갔더니, 테이블 위에 다양한 포도주가 들어있는 포도주 잔이 일렬로 놓여 있었다. 
효주는 포도주 시식을 하려고 하는데, 여기에는 다음과 같은 두 가지 규칙이 있다.

포도주 잔을 선택하면 그 잔에 들어있는 포도주는 모두 마셔야 하고, 
마신 후에는 원래 위치에 다시 놓아야 한다.
연속으로 놓여 있는 3잔을 모두 마실 수는 없다.
효주는 될 수 있는 대로 많은 양의 포도주를 맛보기 위해서 어떤 포도주 잔을 선택해야 할지 고민하고 있다. 
1부터 n까지의 번호가 붙어 있는 n개의 포도주 잔이 순서대로 테이블 위에 놓여 있고, 
각 포도주 잔에 들어있는 포도주의 양이 주어졌을 때, 
효주를 도와 가장 많은 양의 포도주를 마실 수 있도록 하는 프로그램을 작성하시오. 

예를 들어 6개의 포도주 잔이 있고, 
각각의 잔에 순서대로 6, 10, 13, 9, 8, 1 만큼의 포도주가 들어 있을 때, 
첫 번째, 두 번째, 네 번째, 다섯 번째 포도주 잔을 선택하면 총 포도주 양이 33으로 최대로 마실 수 있다.

입력
첫째 줄에 포도주 잔의 개수 n이 주어진다. (1 ≤ n ≤ 10,000) 
둘째 줄부터 n+1번째 줄까지 포도주 잔에 들어있는 포도주의 양이 순서대로 주어진다. 
포도주의 양은 1,000 이하의 음이 아닌 정수이다.

출력
첫째 줄에 최대로 마실 수 있는 포도주의 양을 출력한다.

예제 입력 1 
6
6
10
13
9
8
1
예제 출력 1 
33
'''
# 경우의 수는?
# 이번 칸을 선택하거나, 선택하지 않거나.
# 선택하려면 전칸 또는 전전칸을 선택하지 않아야 한다.
# dp[i]에는 무엇을 저장해야 하지?
# 앞칸을 선택 안한경우, 앞앞칸을 선택 안한경우
# 그러면 dp[i] = 자신+maxdp[i-2], 자신+dp[i-1][0]
'''
import sys

n = int(sys.stdin.readline())

N = list(map(int, sys.stdin.read().rstrip().split()))

dp = [[0] * 2 for _ in range(n + 1)]
dp[1] = [N[0]] * 2

for i in range(2, n + 1):
    dp[i][0] = max(dp[i - 2]) + N[i - 1] # 앞칸이 빔
    dp[i][1] = dp[i - 1][0] + N[i - 1] # 앞앞칸이 빔

print(max(dp[n - 1] + dp[n]))
'''
# print(dp)
# 잘 생각하고 출력해야 하는게, 그냥 max(dp[N])을 출력하면
# 마지막잔을 마시는 경우만 고려하는게 된다.
# 예제만 봐도 마지막잔을 마시지 않는 것이 정답이다.

# 근데 솔직히 틀릴 것 같긴 했다.
# 6
# 100
# 100
# 1
# 1
# 100
# 100
# 이런 걸 못 잡거든. 301이 나와버린다.

# 다시!
# dp[i]는 그냥 현재까지의 최댓값으로 한다. 꼭 i잔을 마실 필요 없다.

import sys

n = int(input())

N = list(map(int, sys.stdin.read().rstrip().split()))

if n == 1:
    print(N[0])
    sys.exit()

elif n == 2:
    print(N[0] + N[1])
    sys.exit()

dp = [0] * (n + 1)
dp[1] = N[0]
dp[2] = N[0] + N[1]

for i in range(3, n + 1):
    dp[i] = max(
        dp[i - 1], # 자신을 선택 안함
        dp[i - 2] + N[i - 1], # 자신 이전을 선택 안함
        dp[i - 3] + N[i - 1] + N[i - 2] # 자신 전전을 선택택 안함
    )

print(dp[n])