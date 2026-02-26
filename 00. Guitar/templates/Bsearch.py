# 삼각형 넓이찾기
def b_search(base: int, heights: list, R: int) -> int:
    left = 0
    right = len(heights) - 1

    result = -1
    while left <= right:
        mid = (left + right) // 2

        curr = heights[mid] * base

        # 더 넓힐 수 있으면 넓혀도 된다.
        if curr <= R:
            result = curr
            left = mid + 1
        # 더 넓힐 수 없다면 줄여야만 한다.
        else:
            right = mid - 1

    return result
