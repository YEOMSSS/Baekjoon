
// 선택 정렬이란?
// 배열중 최소값을 찾아 맨 앞자리와 스왑하기.
// 찾으면 맨 앞을 제외한 다음칸부터 끝까지 반복한다.
// 그걸 정렬될때까지 한다. 위에서부터 순서대로 정렬된다.

#include <stdio.h>
#include <stdlib.h> // malloc

// 원본 값을 직접 바꿔야 하므로 포인터를 사용
void swap(int *x, int *y)
{
    int temp = *x;
    *x = *y;
    *y = temp;
}

// 선택 정렬. *arr로 배열을 받아준다. n은 상수니 const
void selection_sort(int *arr, const int n)
{
    // 처음부터 끝까지 위에서부터 순서대로 정렬하기
    for (int i = 0; i < n; i++) // n-1까지만 돌려도 됨. 어차피 마지막은 하나밖에 없으니
    {
        // 현재 인덱스 저장해두고 더 작은게 나올때까지 밑으로 쭉 훑기
        int min_idx = i;
        for (int k = i + 1; k < n; k++)
        {
            // 더 작은게 나오면 바꾸기
            if (arr[k] < arr[min_idx])
                min_idx = k;
        }

        // arr[i]보다 작은게 있으면 바꿔준다.
        if (i != min_idx)
            // &를 붙여서 주소를 보내줄 것
            swap(&arr[i], &arr[min_idx]);
    }
}

// main함수는 정상종료시 0, 비정상종료시 1을 반환. 그래서 int main
// main함수는 아무런 매개변수도 받지 않으므로 main(void)
int main(void)
{
    int N;
    scanf("%d", &N);

    // malloc으로 큰 배열도 받을 수 있게 하기
    int *nums = malloc(N * sizeof(int));
    for (int i = 0; i < N; i++)
        scanf("%d", &nums[i]);

    selection_sort(nums, N);

    for (int i = 0; i < N; i++)
        printf("%d\n", nums[i]);

    free(nums);
    return 0;
}