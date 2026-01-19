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
