
/*
#include <stdio.h>
#include <string.h> // strcat
#include <stdlib.h> // atoi

int main(void) {

    int X, Y;
    scanf("%d %d", &X, &Y);

    char result_X[10] = "";
    for (int i = 0; i < X; i++) {
        strcat(result_X, "1");
    }

    char result_Y[10] = "";
    for (int i = 0; i < Y; i++) {
        strcat(result_Y, "1");
    }

    int result = atoi(result_X) + atoi(result_Y);
    printf("%d", result);

    return 0;

}
*/

/*
#include <stdio.h>
#include <stdlib.h> // malloc free

int main(void) {

    int X, Y;
    scanf("%d %d", &X, &Y);

    char *res_X = malloc(X + 1);
    char *res_Y = malloc(Y + 1);

    for (int i = 0; i < X; i++) res_X[i] = '1';
    res_X[X] = '\0';
    
    for (int i = 0; i < Y; i++) res_Y[i] = '1';
    res_Y[Y] = '\0';

    int result = atoi(res_X) + atoi(res_Y);
    printf("%d", result);

    free(res_X);
    free(res_Y);

    return 0;

}
*/

/*
#include <stdio.h>
#include <stdlib.h>

int main(void) {

    int X, Y;
    scanf("%d %d", &X, &Y);

    for (int i = 0; i < abs(X - Y); i++) printf("1");

    if (X < Y) {
        for (int i = 0; i < X; i++) printf("2");
    } else {
        for (int i = 0; i < Y; i++) printf("2");
    }

    return 0;
}
*/

#include <stdio.h> // putchar
#include <stdlib.h> // abs

// 반복용 함수 만들기. putchar로 한 글자만 출력한다.
void print_repeat(char ch, int n) {
    for (int i = 0; i < n; ++i) putchar(ch);
}

int main(void) {

    int X, Y; 
    scanf("%d %d", &X, &Y);

    // X와 Y의 차만큼 1 반복
    print_repeat('1', abs(X - Y));

    // X가 Y보다 작으면 X만큼 2 반복, 아니면 Y만큼 2 반복
    print_repeat('2', (X < Y) ? X : Y);

    return 0;

}

// ? : 삼항연산자
// stdio : putchar, fgets 입출력
// stdlib : atoi, malloc, free, abs 유틸
// string : strcat 문자열