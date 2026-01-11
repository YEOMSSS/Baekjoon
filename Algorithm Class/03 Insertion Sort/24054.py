
# 삽입정렬은 인덱스1부터 확인한다.
# 일단 자신을 들어올린다.
# 왼쪽에 있는게 자신보다 크면 그놈을 자기 자리에 놓고 한칸 왼쪽으로 간다.
# 왼쪽에 더 없거나 왼쪽에 있는게 자신보다 작으면 자신을 내려놓고 중단한다.

# 얘도 O(n2)임. 500_000이 들어오면? ㅈ댓구만!

# 저장이라고 표현하는데, 이걸 오십만까지 다 덮어씌우고 바꾸다간 답이 없어.
# 바꾸는 척만 하고 그냥 인덱스로 찾아야 할 것 같은데.

'''
4 5         1 3 2

4 5         3 2
4 5         3 2
1 4 5       3 2

1 4 5       2
1 4 5       2
1 3 4 5     2

1 3 4 5
1 3 4 5
1 3 4 5
1 2 3 4 5

5, 4, 1,
5, 4, 3, 
5, 4 ,3, 2
'''

import sys
input = sys.stdin.readline

import bisect # 이진탐색으로 left에서 current를 끼워넣을 위치를 찾을 것이다.

def insertion_sort(arr, n, k):
    cnt = k
    left = [arr[0]]
    len_left = 1

    for i in range(1, n):
        current = arr[i]
        # 이진탐색으로 위치 찾기
        pos = bisect.bisect_right(left, current)
        # left에서 넘어가야 할 숫자의 수
        shift = len_left - pos
        if cnt <= shift:
            return left[len_left - cnt]
        cnt -= shift

        # 옮길 수 있는 횟수가 남았다면 끼워넣기
        left[pos:pos] = [current]

        if pos != len_left:
            cnt -= 1
            if cnt == 0:
                return current
        len_left += 1

    return -1

def main():
    N, K = map(int, input().split())
    arr_input = list(map(int, input().split()))

    print(insertion_sort(arr_input, N, K))

if __name__ == "__main__":
    main()

# 아깝다. 86%에서 시간초과.
# 아, 설마 readline.. 제발.
# popleft도 뺏고 음수인덱스도 없앴다. 제발좀
# insert도 없애고 슬라이싱으로 바꿔왔다 그만해다오 이건 더오래걸리네 아오
# bisect_right로 해볼까?????