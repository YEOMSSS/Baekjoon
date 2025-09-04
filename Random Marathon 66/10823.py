
# replace를 해보자.

import sys

data = sys.stdin.read()
data = data.replace('\n', '')
nums = list(map(int, data.split(',')))

print(sum(nums))