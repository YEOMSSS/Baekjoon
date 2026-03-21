# 이차함수 (x - 3) ** 2 + 2의 최솟값을 찾는 코드.
def f(x):
    # 예시 함수: x=3에서 최솟값 2를 가짐
    return (x - 3) ** 2 + 2


# int 삼분탐색 예시
def ternary_search(low, high):
    # 둘 다 정수를 유지하기 위해 low <= m1 < m2 <= high 구조 유지
    while high - low >= 3:
        # 셋으로 나눠 m1, m2를 지정하자.
        m1 = (2 * low + high) // 3
        m2 = (low + 2 * high) // 3

        # f(m1)이 f(m2)보다 작으면 단봉은 low-m2 사이에 있다.
        if f(m1) < f(m2):
            high = m2
        # f(m1)이 f(m2)보다 크면 단봉은 m1-high 사이에 있다.
        else:
            low = m1

    # 범위 내 후보를 전부 검사해서 뱉어주자.
    return min(f(t) for t in range(low, high + 1))


# float 삼분탐색 예시
def ternary_search(low, high):

    # 정밀도를 위해 반복 횟수(약 100번)를 지정하거나 오차 범위를 설정함
    for _ in range(100):
        m1 = low + (high - low) / 3
        m2 = high - (high - low) / 3

        # f(m1)이 f(m2)보다 작으면 단봉은 low-m2 사이에 있다.
        if f(m1) < f(m2):
            high = m2
        # f(m1)이 f(m2)보다 크면 단봉은 m1-high 사이에 있다.
        else:
            low = m1

    return (low + high) / 2


# -10에서 10 사이 구간에서 최솟값 x 찾기
result_x = ternary_search(-10, 10)
print(f"최솟값 지점 x: {result_x:.6f}")
print(f"최솟값 f(x): {f(result_x):.6f}")
