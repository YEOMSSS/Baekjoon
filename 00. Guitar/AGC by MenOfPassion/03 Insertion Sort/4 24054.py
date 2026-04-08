import sys

input = sys.stdin.readline


# 펜윅 트리
class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    # i에 1이 더해졌으니 를 포함하는 모든 상위 구간에 1씩 더해준다.
    def add(self, i, v=1):
        while i <= self.n:
            self.tree[i] += v
            # i & -i 는 i에서 최우측 1만 남긴 값이다.
            # i에 그 값을 빼면 1이 존재하는 최하위 비트에 1을 더한 것이 된다.
            # 상위 책임 구간으로 점프하게 된다.
            i += i & -i

    # 1부터 i까지 sum한다.
    # 111 -> 110 -> 100 에 있는 값을 다 더하면 001~111의 합이 된다.
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            # i & -i 는 i에서 최우측 1만 남긴 값이다.
            # i에 그 값을 빼면 1이 존재하는 최하위 비트를 0으로 바꾼 것이 된다.
            # 하위 책임 구간으로 현재 구간을 제외하고 내려간다.
            i -= i & -i
        return s

    # 누적합이 k 이상이 되는 최소 인덱스
    # 펜윅에 존재하는 인덱스 중에서 k번째 인덱스를 반환하게 된다.
    def find_by_rank(self, rank):
        idx = 0
        bit_mask = 1 << (self.n.bit_length())
        while bit_mask:
            nxt = idx + bit_mask
            if nxt <= self.n and self.tree[nxt] < rank:
                rank -= self.tree[nxt]
                idx = nxt
            bit_mask >>= 1
        return idx + 1


def insertion_sort_fenwick(arr_original, N, K):

    # 좌표압축. 작은 수부터 정렬해서, 1부터 순서대로 붙인다.
    arr_sorted = sorted(arr_original)

    # 값 -> 인덱스 매핑. 펜윅트리 쓸거니까 1부터 시작한다.
    value_to_rank = {v: i + 1 for i, v in enumerate(arr_sorted)}
    # 인덱스 -> 값 매핑. 값 복원용 역매핑
    rank_to_value = {i + 1: v for i, v in enumerate(arr_sorted)}

    # 중복없음이 보장되므로 m = len(vals)은 필요 없다.
    fenwick = FenwickTree(N)
    remain = K
    len_left = 0

    # 첫 원소부터 left로.
    fenwick.add(value_to_rank[arr_original[0]])
    len_left = 1

    for i in range(1, N):
        current = arr_original[i]

        # 좌표압축된거 가져오기
        current_rank = value_to_rank[current]

        # 1부터 cidx까지 트리를 더하면 개수가 나온다.
        # pos = 작거나 같은 개수 (삽입 인덱스)
        pos = fenwick.sum(current_rank)
        # shift = 더 큰 개수. 를 세야 하므로 len_left에서 빼준다.
        shift = len_left - pos

        # cnt를 다 사용했으면 값을 반환해야한다.
        if remain <= shift:
            # 오른쪽에서 cnt번째 큰 값
            # = 왼쪽에서 (len_left - cnt + 1)번째 작은 값
            rank = len_left - remain + 1
            idx = fenwick.find_by_rank(rank)
            # 좌표 역매핑 복원
            return rank_to_value[idx]

        # shift만큼 cnt 사용하기
        remain -= shift

        # left에 insert한다. 정확히는 같은 효과를 낸다.
        fenwick.add(current_rank, 1)
        len_left += 1

        # insert할 때도 cnt를 소모한다.
        if pos != len_left - 1:
            remain -= 1
            if remain == 0:
                return current

    return -1


def main():
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    print(insertion_sort_fenwick(arr, N, K))


if __name__ == "__main__":
    main()


"""
# 삽입정렬은 인덱스1부터 확인한다.
# 일단 자신을 들어올린다.
# 왼쪽에 있는게 자신보다 크면 그놈을 자기 자리에 놓고 한칸 왼쪽으로 간다.
# 왼쪽에 더 없거나 왼쪽에 있는게 자신보다 작으면 자신을 내려놓고 중단한다.

# 얘도 O(n2)임. 500_000이 들어오면? ㅈ댓구만!

# 저장이라고 표현하는데, 이걸 오십만까지 다 덮어씌우고 바꾸다간 답이 없어.
# 바꾸는 척만 하고 그냥 인덱스로 찾아야 할 것 같은데.


# 4 5         1 3 2

# 4 5         3 2
# 4 5         3 2
# 1 4 5       3 2

# 1 4 5       2
# 1 4 5       2
# 1 3 4 5     2

# 1 3 4 5
# 1 3 4 5
# 1 3 4 5
# 1 2 3 4 5

# 5, 4, 1,
# 5, 4, 3, 
# 5, 4 ,3, 2


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
# """
