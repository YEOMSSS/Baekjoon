// 맨 앞부터 확인하면 된다.
// 셋 다 같으면 다음 인덱스로 넘어간다.
// 셋 다 다르면 HJS 쌉가능이다.
// 두개만 같은 경우는 다음을 확인해봐야 한다.

// HJH의 경우는 탈락.
// HJJ의 경우는 23이 같으면 계속 다음거를 확인한다.
// 다음이 가운데가 H고 마지막이 J던 S던 통과, 가운데가 J고 마지막이 H면 탈락, JS는 통과.
// 가운데가 S면 마지막이 J던 H던 통과.

// S는 조커같은 느낌이라 무조건 통과라고 보면 된다.

// 정리하면
// HHJ 이후 23이 HJ HS SJ SH JS 통과, JJ HH SS 다시, JH 탈락

// HHJ의 경우는 12로 이짓을 하면 된다.
// HHJ 이후 12가 HJ HS SJ SH JS 통과, JJ HH SS 다시, JH 탈락. 똑같다.

#include <stdio.h>

int main(void)
{
    int N;
    scanf("%d", &N);

    char P[N + 1], Q[N + 1], R[N + 1];
    scanf("%s", P);
    scanf("%s", Q);
    scanf("%s", R);

    int HHJ = 0, HJJ = 0;

    char H, J;

    // HJ HS SJ SH JS 통과, JJ HH SS 다시, JH 탈락
    for (int i = 0; i < N - 1; i++)
    {
        if (HHJ)
        {
            if (P[i] == Q[i])
            {
                continue;
            }
            else if (P[i] == J && Q[i] == H)
            {
                printf("Hmm...");
                return 0;
            }
            else
            {
                printf("HJS! HJS! HJS!");
                return 0;
            }
        }

        if (HJJ)
        {
            if (Q[i] == R[i])
            {
                continue;
            }
            else if (Q[i] == J && R[i] == H)
            {
                printf("Hmm...");
                return 0;
            }
            else
            {
                printf("HJS! HJS! HJS!");
                return 0;
            }
        }

        if (P[i] == Q[i] && Q[i] == R[i])
        {
            continue;
        }
        else if (P[i] == R[i])
        {
            printf("Hmm...");
            return 0;
        }
        else if (P[i] == Q[i])
        {
            HHJ++;
            H = Q[i];
            J = R[i];
        }
        else if (Q[i] == R[i])
        {
            HJJ++;
            H = P[i];
            J = Q[i];
        }
        else
        {
            printf("HJS! HJS! HJS!");
            return 0;
        }
    }

    if (HHJ && P[N - 1] != Q[N - 1])
    {
        printf("HJS! HJS! HJS!");
        return 0;
    }
    if (HJJ && Q[N - 1] != R[N - 1])
    {
        printf("HJS! HJS! HJS!");
        return 0;
    }

    if (P[N - 1] != Q[N - 1] && Q[N - 1] != R[N - 1] && P[N - 1] != R[N - 1])
    {
        printf("HJS! HJS! HJS!");
        return 0;
    }

    printf("Hmm...");
    return 0;
}

// HJS HHJ HJJ HJH HHH