# 비둘기집 원리.
# 어차피 선택할 수 있는건 2개뿐이다. 3중복부터는 의미가 없어진다.
# 999개니까, 1998개만 확인하면 그게 최대가 된다. 1998**2는 충분히 가능.


# 자릿수 합해주는 함수
def func(num) -> int:
    temp = 0
    for n in str(num):
        temp += int(n)

    return temp


from collections import Counter
from itertools import combinations


def main() -> None:
    N = int(input())

    nums = list(map(int, input().split()))
    nums_Counter = Counter(nums)

    # 2회를 초과한 중복은 2회로 맞춰서 저장해준다.
    for key, value in nums_Counter.items():
        if value <= 2:
            continue
        nums_Counter[key] = 2

    # 앞에 있는 for가 먼저 작동한다.
    nums = [k for k, v in nums_Counter.items() for _ in range(v)]

    result = 0
    for i, j in combinations(nums, 2):
        temp = i * j
        result = max(result, func(temp))

    print(result)


main()
