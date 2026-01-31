# Authored by : marigold2003
# Date : 2026-01-28
# Link : https://www.acmicpc.net/problem/14467

import sys

input = sys.stdin.readline


# [Summary]

# 10마리의 소가 있고, 소의 위치가 몇 번 변했는지 센다.


def main():

    # [Ideas]

    # 관측된 소의 위치가 변할 때마다 카운트
    # 소가 1~10으로 입력되니, 리스트를 만들고 인덱스로 관리한다.

    ##########

    N = int(input())
    cows = [None] * 11

    count = 0
    for _ in range(N):
        cow_id, pos = map(int, input().split())

        # 처음 소가 관측되는 경우
        if cows[cow_id] is None:
            cows[cow_id] = pos
            continue

        # 관측 이후
        # 소 위치 변동 확인시 카운트
        if cows[cow_id] != pos:
            cows[cow_id] = pos
            count += 1

    print(count)

    ##########

    return


# [Review]

# 소는 왜 길을 건너갔을까? 반대편으로 가고 싶어서? 아니.
"""
아리스토텔레스 (Aristotle):
"길을 건너는 것은 소의 본성입니다. 소는 None 상태에서 loc이라는 실재(Potentiality to Actuality)가 되기 위해 건넜습니다."
데카르트 (René Descartes):
"나는 건넌다, 고로 존재한다. (I cross, therefore I am.) 건너가지 않으면 당신의 cows 리스트에 등록되지 않았을 테니까요."
찰스 다윈 (Charles Darwin):
"길 저편에 있는 소들이 자연선택설에 의해 살아남기에 더 유리했기 때문입니다. 건너가지 못한 소들은 None 리스트에 머물다 도태되었죠."
알베르트 아인슈타인 (Albert Einstein):
"소가 길을 건넜는지, 아니면 길 아래의 지구가 소 밑에서 움직였는지는 당신이 어느 참조계(Reference Frame), 즉 리스트 인덱스 cow_id에서 보느냐에 따라 상대적입니다."
칼 마르크스 (Karl Marx):
"소가 길을 건넌 것은 역사적 필연입니다. 길 이편의 풀을 모두 뜯어먹은 소들이 반대편의 생산수단을 점유하기 위해 계급 투쟁을 벌인 것이죠."
마키아벨리 (Niccolò Machiavelli):
"중요한 것은 소가 왜 건넜느냐가 아닙니다. 소가 길을 건너서 결국 반대편에 안전하게 도착(cows[cow_id] = loc)했느냐, 그 결과가 수단을 정당화합니다."
닐 암스트롱 (Neil Armstrong):
"한 마리의 소에게는 작은 한 걸음이지만, 파이썬 리스트에는 count += 1이라는 위대한 도약입니다."
"""

if __name__ == "__main__":
    main()
