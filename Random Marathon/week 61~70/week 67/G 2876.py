
import sys
input = sys.stdin.readline

N = int(input())

table = [tuple(map(int, input().split())) for _ in range(N)]

# dp에는 (왼쪽선택시, 오른쪽선택시)로 저장됨
dp = [[1, 1] for _ in range(N)]

for i in range(1, N):

    # 좌, 우 한번씩 실행
    for j in range(2):
        
        # 전 단계 왼쪽과 현재가 같은 경우
        if table[i - 1][0] == table[i][j]:
            dp[i][j] = dp[i - 1][0] + 1
        # 전 단계 오른쪽과 현재가 같은 경우
        elif table[i - 1][1] == table[i][j]:
            dp[i][j] = dp[i - 1][1] + 1
        # 전 단계와 현재가 같은 게 없는 경우
        else:
            dp[i][j] = 1

result = [0, 6]

for i, desk in enumerate(dp):
    
    for j in range(2):

        # 연속 미달시 패스
        if desk[j] < result[0]:
            continue
        # 동일 연속인데 등급 초과   시 패스
        if desk[j] == result[0] and table[i][j] >= result[1]:
            continue
        result = [desk[j], table[i][j]]

print(*result)