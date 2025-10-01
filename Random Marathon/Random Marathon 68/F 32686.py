
import sys
input = sys.stdin.readline

N, S, E = map(int, input().split())
time = E - S

total = 0
for _ in range(N):

    R, A, D = map(int, input().split())
    cast = R + A
    cast_log = [0] * R + [1] * A

    log = cast_log * (E // cast) + cast_log[:(E % cast)]

    cnt = sum(log[S : E])
    total += round(cnt / A * D, 10)

print(round(total / time, 10))

# 0111011101
# 이게 써보니까 아이디어가 생각나네
# 이 개념을 이용해서 수학적으로 풀 수 있을듯.