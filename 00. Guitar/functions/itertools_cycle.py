from itertools import cycle

l = ["a", "b", "c"]
m = [1, 2]
n = (4, 5, 6, 7)

it = cycle(l)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
