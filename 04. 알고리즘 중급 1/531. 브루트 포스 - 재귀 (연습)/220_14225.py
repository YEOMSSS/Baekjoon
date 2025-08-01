'''
문제
수열 S가 주어졌을 때, 수열 S의 부분 수열의 합으로 나올 수 없는 가장 작은 자연수를 구하는 프로그램을 작성하시오.

예를 들어, S = [5, 1, 2]인 경우에 1, 2, 3(=1+2), 5, 6(=1+5), 7(=2+5), 8(=1+2+5)을 만들 수 있다.
하지만, 4는 만들 수 없기 때문에 정답은 4이다.

입력
첫째 줄에 수열 S의 크기 N이 주어진다. (1 ≤ N ≤ 20)

둘째 줄에는 수열 S가 주어진다.
S를 이루고있는 수는 100,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 수열 S의 부분 수열의 합으로 나올 수 없는 가장 작은 자연수를 출력한다.

예제 입력 1 
3
5 1 2
예제 출력 1 
4
예제 입력 2 
3
2 1 4
예제 출력 2 
8
예제 입력 3 
4
2 1 2 7
예제 출력 3 
6
'''
# 비트마스킹 귀찮아서 안했는데 맛있어보임.

import sys
input = sys.stdin.readline

from itertools import combinations

N = int(input())
S = list(map(int, input().split()))

sums = set()

for i in range(1, N + 1):
    combs = combinations(S, i)
    for comb in combs:
        sums.add(sum(comb))

i = 0
while True:
    i += 1
    if i not in sums:
        print(i)
        break