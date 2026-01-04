# import sys

# input = sys.stdin.readline

# vow_upper = [
#     65,
#     73,
#     89,
#     69,
#     79,
#     85,
# ]
# vow_lower = [
#     97,
#     105,
#     121,
#     101,
#     111,
#     117,
# ]
# con_upper = [
#     66,
#     75,
#     88,
#     90,
#     78,
#     72,
#     68,
#     67,
#     87,
#     71,
#     80,
#     86,
#     74,
#     81,
#     84,
#     83,
#     82,
#     76,
#     77,
#     70,
# ]
# con_lower = [
#     98,
#     107,
#     120,
#     122,
#     110,
#     104,
#     100,
#     99,
#     119,
#     103,
#     112,
#     118,
#     106,
#     113,
#     116,
#     115,
#     114,
#     108,
#     109,
#     102,
# ]


# def main():
#     while True:
#         string = input()
#         if not string:
#             return
#         string = list(map(ord, string.rstrip()))

#         for ch in string:
#             if ch in vow_upper:
#                 print(chr(vow_upper[(vow_upper.index(ch) - 3) % 6]), end="")
#             elif ch in vow_lower:
#                 print(chr(vow_lower[(vow_lower.index(ch) - 3) % 6]), end="")
#             elif ch in con_upper:
#                 print(chr(con_upper[(con_upper.index(ch) - 10) % 20]), end="")
#             elif ch in con_lower:
#                 print(chr(con_lower[(con_lower.index(ch) - 10) % 20]), end="")
#             else:
#                 print(chr(ch), end="")
#         print()


# if __name__ == "__main__":
#     main()

# 애초에 ord와 chr을 왔다갔다 할 필요도 없다.
import sys

input = sys.stdin.readline

vow_upper = "AIYEOU"
vow_lower = "aiyeou"
con_upper = "BKXZNHDCWGPVJQTSRLMF"
con_lower = "bkxznhdcwgpvjqtsrlmf"

decode_map = {}

for i, c in enumerate(vow_upper):
    decode_map[c] = vow_upper[(i - 3) % 6]

for i, c in enumerate(vow_lower):
    decode_map[c] = vow_lower[(i - 3) % 6]

for i, c in enumerate(con_upper):
    decode_map[c] = con_upper[(i - 10) % 20]

for i, c in enumerate(con_lower):
    decode_map[c] = con_lower[(i - 10) % 20]


def main():
    while True:
        line = input()
        if not line:
            break

        for ch in line.rstrip():
            # dict.get(key, default)
            # key가 dict에 있으면 value 반환, 없으면 default 반환
            print(decode_map.get(ch, ch), end="")
        print()


if __name__ == "__main__":
    main()
