
import sys
input = sys.stdin.readline

strings = list(input().split())
check_list = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']

result = strings[0][0].upper()

for word in strings[1:]:
    if word in check_list:
        continue
    result += word[0].upper()

print(result)