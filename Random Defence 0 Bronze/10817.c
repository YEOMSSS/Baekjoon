/*
문제
세 정수 A, B, C가 주어진다. 이때, 두 번째로 큰 정수를 출력하는 프로그램을 작성하시오. 

입력
첫째 줄에 세 정수 A, B, C가 공백으로 구분되어 주어진다. (1 ≤ A, B, C ≤ 100)
*/

#include <stdio.h>

int main(void) {

    int nums[3], temp;

    for (int i = 0; i < 3; i++){
        scanf("%d", nums+i);
    }
    for (int i = 0; i < 3; i++){
        for (int j = i + 1; j<3; j++){
            if (nums[i] > nums[j]){
                temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
            }
        }
    }
    printf("%d", nums[1]);

    return 0;
}

// 지금 정렬을 한 거지? 그렇지?
// sort 딸깍이 이렇게 복잡하다 이거지???? ㅆㅃㅆㅃ