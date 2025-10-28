#include <stdio.h>

int main(void)
{
    int T;
    scanf("%d", &T);

    while (T--)
    {
        int n;
        scanf("%d", &n);

        // 100칸을 0으로 초기화해두기 (0을 열린 상태로 설정)
        int nums[100] = {
            0,
        };

        // 다 0이니까 i=1일때는 이미 지나감
        // 여기서 i는 회차가 된다.
        for (int i = 2; i <= n; i++)
        {
            // 인덱스니까 시작은 i-1
            int cur = i - 1;
            // 인덱스는 n-1까지 도달할 수 있다.
            while (cur < n)
            {
                // 열렸으면 닫고, 닫혔으면 열기
                nums[cur] = (nums[cur] + 1) % 2;
                // i칸만큼 이동해서 동일 실행
                cur += i;
            }
        }

        int result = 0;
        // 0으로 열린 방 개수 세기
        for (int i = 0; i < n; i++)
        {
            if (!nums[i])
                result += 1;
        }

        printf("%d\n", result);
    }

    return 0;
}