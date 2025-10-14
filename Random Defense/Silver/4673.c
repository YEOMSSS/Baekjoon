/*
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
*/

#include <stdio.h>

int func(int n)
{
    int result = n;
    while (n)
    {
        result += n % 10;
        n /= 10;
    }
    return result;
}

int main(void)
{
    int nums[10001] = {
        0,
    };

    for (int i = 1; i <= 10000; i++)
    {
        int temp = func(i);
        if (temp <= 10000)
            nums[temp] = 1;
        if (!nums[i])
            printf("%d\n", i);
    }
    return 0;
}