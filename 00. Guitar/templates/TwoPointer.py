# 연속된 수들의 부분합 중
# 합이 S 이상이 되는 것 중
# 가장 짧은 것의 길이 구하기

N, S = map(int, input().split())
arr = list(map(int, input().split()))

answer = 100001

curr_sum = 0
end = 0

for start in range(N):

    # 현재 합이 S보다 작으면 오른쪽으로 늘려보자.
    # 단, 늘릴 수 있을 때만 늘리자.
    while curr_sum < S and end < N:
        curr_sum += arr[end]
        end += 1

    # 합이 target보다 같거나 클 때, 즉 조건만족시 실행
    if curr_sum >= S:
        # print(start, end, curr_sum)
        answer = min(answer, end - start)

    curr_sum -= arr[start]
