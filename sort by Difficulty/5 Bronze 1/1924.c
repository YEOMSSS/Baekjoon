#include <stdio.h>

int main(void) {

    int X, Y;
    scanf("%d %d", &X, &Y);

    int month_days_arr[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

    // 현재 달의 일수
    int days = Y;
    // 현재 달 이전까지 일수의 함
    for (int m = 0; m < X - 1; m++) {
        days += month_days_arr[m];
    }

    // 포인터 배열로 char 배열 편하게 저장하기
    const char *day_name_arr[7] = {"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};
    printf("%s", day_name_arr[days % 7]);

    return 0;
}