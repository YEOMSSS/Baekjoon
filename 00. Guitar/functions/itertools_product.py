from itertools import product


l = ["a", "b", "c"]
m = [1, 2]
n = (4, 5, 6, 7)
for i in product(l, repeat=3):
    print(i)

# 중복허용 순열은 이걸로 만드는게 더 편하겠는데? ㅋㅋㅋㅋㅋ
# 와 좋은거 알았다. 진짜로.
