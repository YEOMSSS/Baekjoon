# def main() -> None:
#     N, K = input().split()
#     nums = set(map(int, input().split()))

#     # 전 단계에서 작은 숫자를 사용했을 때 켜짐
#     flag = False

#     def func(t: int):
#         nonlocal flag

#         # 앞에서 작은거 썼으면 뒤는 최대로 박는다.
#         if flag:
#             return max(nums)

#         # 앞에서 동일하게 갔으면 뒤도 동일할 수 있는지 확인한다.
#         if t in nums:
#             return t

#         # 동일할 수 없으면 가능한 것 중에서 가장 큰 걸 찾는다.
#         temp = 0
#         for num in nums:
#             if num > t:
#                 continue
#             temp = max(temp, num)

#         # 앞에걸 동일하게 하면 뒤가 불가능해질 경우 한번 되돌린다.
#         if not temp:
#             prev = result.pop()
#             if prev < min(nums):
#                 result.append(0)
#                 if not t:
#                     flag = True
#                     return max(nums)
#                 return 0
#             result.append(func(prev - 1))
#             temp = max(nums)

#         flag = True
#         return temp

#     result = [0]
#     for n in N:
#         result.append(func(int(n)))

#     print(int("".join(map(str, result))))


# main()

# 브루트포스로 풀걸...


def main() -> None:
    N, K = map(int, input().split())
    nums = set(input().split())

    for i in range(N, 0, -1):
        for t in str(i):
            if t not in nums:
                break
        else:
            print(i)
            return


main()


# 좀 더 맛있는 버전. product를 써보자.
# product로 쓰는 숫자만 조합해서 만들고 역순으로 정렬해 돌린다.

# from itertools import product

# N, k = map(int, input().split())
# box = list(input().split())
# r = len(str(N))
# while True:
#     found = False
#     for i in sorted(list(map(int, map("".join, product(box, repeat=r)))), reverse=True):
#         if N >= i:
#             print(i)
#             found = True
#             break
#     if found:
#         break
#     else:
#         r -= 1
