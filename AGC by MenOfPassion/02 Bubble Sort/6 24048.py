
# 앞자리가 역전이면 append, 뒷자리가 역전이면 appendleft.

# 배열을 비교하는 과정에서 시간초과가 계속 나는걸?
# 바뀐 자리만 확인해야겠어.

import sys
input = sys.stdin.readline

from collections import deque

def main():
    N, K = map(int, input().split())
    arr_A = list(map(int, input().split()))
    arr_B = list(map(int, input().split()))

    # 다른 원소의 개수를 세어둔다.
    not_same = 0
    for i in range(N):
        not_same += (arr_A[i] != arr_B[i])
    
    # 처음부터 같은 배열이 입력되었다면 즉시 종료
    if not_same == 0:
        print(1)
        return

    queue = deque()

    # 일단 처음 상태 확인용
    for i in range(N - 1):
        if arr_A[i] > arr_A[i + 1]:
            queue.append(i)

    cnt = 0
    while queue:
        cnt += 1

        # K회 안에 A배열과 B배열이 같아지는지 검사. 넘어가면 즉시 종료
        if cnt > K:
            print(0)
            return

        current = queue.popleft()

        before_cur = (arr_A[current] != arr_B[current])
        before_next_cur = (arr_A[current + 1] != arr_B[current + 1])

        arr_A[current], arr_A[current + 1] = arr_A[current + 1], arr_A[current]

        after_cur = (arr_A[current] != arr_B[current])
        after_next_cur = (arr_A[current + 1] != arr_B[current + 1])

        not_same += (after_cur - before_cur) + (after_next_cur - before_next_cur)

        # A배열과 B배열이 같아지면 조건 만족 = 다른 게 없으면 같은 것
        if not_same == 0:
            print(1)
            return

        if current < N - 2 and arr_A[current + 1] > arr_A[current + 2]:
            if not queue or queue[0] != current + 1:
                queue.appendleft(current + 1)

        if 0 < current and arr_A[current - 1] > arr_A[current]:
            queue.append(current - 1)

    print(0)


if __name__ == "__main__":
    main()
