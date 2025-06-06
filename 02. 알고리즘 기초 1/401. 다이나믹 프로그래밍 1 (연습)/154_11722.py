'''
문제
수열 A가 주어졌을 때, 가장 긴 감소하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 30, 10, 20, 20, 10} 인 경우에
가장 긴 감소하는 부분 수열은 A = {10, 30, 10, 20, 20, 10} 이고, 길이는 3이다.

입력
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

출력
첫째 줄에 수열 A의 가장 긴 감소하는 부분 수열의 길이를 출력한다.

예제 입력 1 
6
10 30 10 20 20 10
예제 출력 1 
3
'''

import sys
input = sys.stdin.readline

def main():
    n = int(input())

    nums = list(map(int, input().split()))

    dp = [1] * n

    for i in range(n):
        for j in range(i): # i==0일땐 자동으로 건너뛰어짐.
            if nums[i] < nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(max(dp))
    # print(dp) 디버깅을 했으면 지우던가, 주석처리를 하던가..

if __name__ == "__main__":
    main()