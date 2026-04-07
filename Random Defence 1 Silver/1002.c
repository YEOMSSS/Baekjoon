/*
# 원의 교점 개수를 찾는 거다.

# 두 점 사이의 거리가 r1+r2보다
# 크면 교점 0개
# 같으면 교점 1개 (외접)
# 작으면 교점 2개

# 또는 두 점 사이의 거리가 abs(r1-r2)보다
# 크면 교점 2개
# 같으면 교점 1개 (내접)
# 작으면 교점 0개

# 점이 같고 반지름이 같으면 동일한 점으로 무한의 교점을 갖는다.

# 정리하면 두 점 사이의 거리가
# 합보다 작고 차보다 크면 교점 2개,
# 합이랑 같거나 차랑 같으면 교점 1개,
# 합보다 크거나 차보다 작으면 교점 0개.

import sys

input = sys.stdin.readline


def func():
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    # ** 0.5 하지 않고 그냥 제곱한 상태로 비교
    distance = (x1 - x2) ** 2 + (y1 - y2) ** 2
    sum = (r1 + r2) ** 2
    diff = (r1 - r2) ** 2  # 굳이 abs 안해도 될듯.

    if distance == 0 and diff == 0:
        return -1
    elif diff < distance < sum:
        return 2
    elif diff == distance or sum == distance:
        return 1
    else:
        return 0


def main():
    T = int(input())

    for _ in range(T):
        print(func())


main()
*/

#include <stdio.h>
#include <math.h>

int func()
{
    int x1, y1, r1, x2, y2, r2;
    scanf("%d %d %d %d %d %d", &x1, &y1, &r1, &x2, &y2, &r2);

    int distance = pow(x1 - x2, 2) + pow(y1 - y2, 2);
    int sum = pow(r1 + r2, 2);
    int diff = pow(r1 - r2, 2);

    if (distance == 0 && diff == 0)
        return -1;
    else if (diff < distance && distance < sum)
        return 2;
    else if (diff == distance || sum == distance)
        return 1;
    else
        return 0;
}

int main(void)
{
    int N;
    scanf("%d", &N);

    while (N--)
        printf("%d\n", func());

    return 0;
}