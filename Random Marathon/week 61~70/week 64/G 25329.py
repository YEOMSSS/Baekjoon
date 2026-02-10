
import sys
input = sys.stdin.readline

N = int(input())

# 이름 : 이용시간 으로 저장할 딕셔너리 생성
charge_dict = {}

for _ in range(N):
    time_input, name = input().split()

    # 첫 생성시 0으로
    if name not in charge_dict:
        charge_dict[name] = 0

    # 입력된 시간을 분으로 바꿔 누적합
    min = (int(time_input[ : 2]) * 60) + int(time_input[3 : ])
    charge_dict[name] += min

# 총 이용시간을 요금으로 바꾸기
for name, use_min in charge_dict.items():
    # 모든 이용자는 10원을 내고 시작함
    charge = 10
    use_min -= 100

    # 이용시간이 0 이하가 될 때까지 50분씩 빼고 3원을 냄
    while use_min > 0:
        use_min -= 50
        charge += 3
    
    # 총 이용시간을 비용으로 덮어쓰기
    charge_dict[name] = charge

# value에 대해 내림차순 후 key에 대해 오름차순 정렬
sorted_charge = sorted(charge_dict.items(), key= lambda x: (-x[1], x[0]))

for stuff in sorted_charge:
    print(*stuff)

# 감 떨어지지 않게..

