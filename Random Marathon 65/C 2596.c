
#include <stdio.h>

// A ~ H. 6자리지만 \0널문자 저장을 위해 7로 설정
const char codes[8][7] = {
    "000000", "001111", "010011", "011100",
    "100110", "101001", "110101", "111010" 
};
// 마찬가지로, 8자이지만 \0을 위해 9로 설정
const char letters[9] = "ABCDEFGH";

// 문자열끼리 다르면 cnt + 1
int compare_code(const char *a, const char *b) {
    int cnt = 0;
    for (int i = 0; i < 6; i++) {
        if (a[i] != b[i]) cnt++;
    }
    return cnt;
}

int main() {
    int N;
    scanf("%d", &N);

    // 코드 + \0 입력받기
    char input[(N * 6) + 1];
    scanf("%s", input);

    // 정답 누적용 문자열\0 만들어두기
    char answer[N + 1];

    for (int i = 0; i < N; i++) {
        // input[i * 6 :]부터 읽는 포인터 만들기
        const char *chunk = input + i * 6;

        // 코드 입력 오류 확인용 스위치
        int ok = 0;

        // A ~ H 8회 반복해서 코드 비교, 찾으면 이번 반복 종료
        for (int j = 0; j < 8; j++) {
            if (compare_code(chunk, codes[j]) <= 1) {
                answer[i] = letters[j];
                ok = 1;
                break;
            }
        }

        // 코드 입력 오류 시 현재 순서 + 1 출력 후 종료
        if (! ok) {
            printf("%d", i + 1);
            return 0;
        }
    }

    // 문제가 생기지 않았다면 누적된 정답을 출력한다.
    answer[N] = '\0'; // 굉장히 중요한 부분.
    printf("%s", answer);

    return 0;
}

// 나쁘진 않았다에용.