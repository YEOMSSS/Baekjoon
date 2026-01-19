from itertools import groupby

string = "aadddkkkkknnaaavv"

for ch, group in groupby(string):
    print(ch, list(group))

"""
a ['a', 'a']
d ['d', 'd', 'd']
k ['k', 'k', 'k', 'k', 'k']
n ['n', 'n']
a ['a', 'a', 'a']
v ['v', 'v']
"""

# groupby는 연속으로 같은 값들을 묶어주는 함수다.
