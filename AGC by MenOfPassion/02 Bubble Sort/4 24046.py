
# // 핵심은 현재 인덱스 앞, 현, 뒤 3개만 확인한다는 것에 있다.
# // swap을 하면 세가지 경우에만 영향을 주게 된다.
# // a b c d 에서 b와 c를 스왑하면? a c b d.
# // ab bc cd가 ac cb bd가 되었다.
# // 세 칸을 확인해서 역전이 있는 경우만 힙에 넣고, 그때만 swap을 실행한다.
# // 그런데 이게뭐야, 가운데는 볼 필요 없는거같은데? bc가 cb가 된건 변함이 없잖아?
# // 아니 애초에, 비교는 똑같이 되고 있는거 아니야? 아 씨, 뭐지? 씨발 뭐지?
# // 괜히 플래티넘이 아니다 이거냐? 수업끝나고해야겠네이씨. 아......

'''
def main():
    N, K = map(int, input().split())
    arr_N = list(map(int, input().split()))

    cnt = 0
    for i in range(N):
        for j in range(N - i - 1):
            if arr_N[j] > arr_N[j + 1]:
                arr_N[j], arr_N[j + 1] = arr_N[j + 1], arr_N[j]
                cnt += 1

                if cnt == K:
                    print(arr_N[j], arr_N[j + 1])
                    return
    print(-1)
    return

if __name__ == "__main__":
    main()
'''
'''
a b c d e f
a b d c e f 2, 4
a b d e c f 3, 5

6 5 4 3 2 1     0 1 2 3 4
5 6 4 3 2 1     1 2 3 4     이번턴에 1이 역전이지만 원래 역전이었기때문에 pass?
5 4 6 3 2 1     2 3 4 0     오른쪽이 역전이면 바로 다음턴에 바뀌네?
5 4 3 6 2 1     3 4 0 1
5 4 3 2 6 1     4 0 1 2
5 4 3 2 1 6     0 1 2 3     뒷자리, 앞자리 확인해.
앞자리가 역전이면 append, 뒷자리가 역전이면 appendleft.
'''

import sys
input = sys.stdin.readline

from collections import deque

def main():
    N, K = map(int, input().split())
    arr_N = list(map(int, input().split()))

    queue = deque()

    # 일단 처음 상태 확인용
    for i in range(N - 1):
        if arr_N[i] > arr_N[i + 1]:
            queue.append(i)

    cnt = 0
    while queue:
        cnt += 1
        current = queue.popleft()
        arr_N[current], arr_N[current + 1] = arr_N[current + 1], arr_N[current]

        if current < N - 2 and arr_N[current + 1] > arr_N[current + 2]:
            if not queue or queue[0] != current + 1:
                queue.appendleft(current + 1)

        if 0 < current and arr_N[current - 1] > arr_N[current]:
            queue.append(current - 1)

        if cnt == K:
            print(arr_N[current], arr_N[current + 1])
            return

    print(-1)


if __name__ == "__main__":
    main()

# GPT 개새끼야, 결국 내가 이겼다는 거다.
# 너같은 로봇새끼는 이렇게 쉬운 풀이는 생각 못해낼걸.