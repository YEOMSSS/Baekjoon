import sys

input = sys.stdin.readline


# 펜윅 트리
class FenwickTree:
    # fenwick = FenwickTree(n) 을 하면 n사이즈배열의 트리가 생긴다.
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
    def find_by_order(self, order):
        idx = 0
        bit_mask = 1 << (self.n.bit_length())
        while bit_mask:
            nxt = idx + bit_mask
            if nxt <= self.n and self.tree[nxt] < order:
                order -= self.tree[nxt]
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
            target_order = len_left - remain + 1
            # 트리에 들어있는 진행중인 선택정렬을 left로 한다.
            left = []
            # 역매핑해서 left에 집어넣는다.
            for order in range(1, len_left + 1):
                rank = fenwick.find_by_order(order)
                left.append(rank_to_value[rank])
                # 현재 진행중인 순서는 복사되어있으므로 한번 더 출력한다.
                if order == target_order:
                    left.append(rank_to_value[rank])

            # 현재 i값은 들어올려져 있으므로 출력되지 않는다. i+1부터 right가 됨.
            right = arr_original[i + 1 :]
            return left + right

        # shift만큼 cnt 사용하기
        remain -= shift

        # left에 insert한다. 정확히는 같은 효과를 낸다.
        fenwick.add(current_rank, 1)
        len_left += 1

        # 앞이 더 작아서 변화가 없으면 cnt소모 없음.
        if pos == len_left - 1:
            continue

        # insert할 때도 cnt를 소모한다.
        remain -= 1
        if remain == 0:
            left = []
            # 들어올린 i값을 정렬된 위치에 내려놓았기 때문에 복사할 필요 없다.
            for order in range(1, len_left + 1):
                rank = fenwick.find_by_order(order)
                left.append(rank_to_value[rank])

            # i를 트리에 넣었으니 i+1부터 right로 출력한다.
            right = arr_original[i + 1 :]
            return left + right

    # K가 모든 연산 수를 초과하는 경우
    return (-1,)


def main():
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    print(*insertion_sort_fenwick(arr, N, K))


if __name__ == "__main__":
    main()
