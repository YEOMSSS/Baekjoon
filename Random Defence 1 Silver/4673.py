def func(n):
    result = n
    while n:
        result += n % 10
        n //= 10

    return result


def main():
    nums = [True] * 10001

    for i in range(1, 10000):
        temp = func(i)
        if temp <= 10000:
            nums[temp] = False

    for i, b in enumerate(nums):
        if not i:
            continue
        if b:
            print(i)


main()
