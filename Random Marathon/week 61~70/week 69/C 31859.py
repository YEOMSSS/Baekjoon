
import sys
input = sys.stdin.readline

N, name = input().split()
used = set()

new_name = ""
for char in name:
    if char in used:
        continue
    used.add(char)
    new_name += char

result = str(int(N) + 1906) + new_name + str(len(name) - len(new_name) + 4)

print("smupc_" + result[::-1])
