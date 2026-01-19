# 동남서북 0123

start = 3  # 북에서 시작
for _ in range(10):
    t = int(input())

    start = (start + t) % 4

list = ["E", "S", "W", "N"]
print(list[start])
