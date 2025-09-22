
# 그리디로 풀 수 있나.
# 그냥 다 더하면 안되나? 평일인 일수 구해서 빼준 나머지가 초과근무지.
# 음, 마감일이라는 게 있구나. 급한거 우선으로 정렬하자.

N = int(input())

works = [list(map(int, input().split())) for _ in range(N)]
works.sort(key= lambda x: x[0])

# 평일에는 2회 일할 수 있고, 주말에는 1회만 일할 수 있다.


