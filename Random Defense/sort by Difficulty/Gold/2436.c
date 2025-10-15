/*
Ǯ�� : �ִ� ������� �ּҰ����
���ϰ��� �ϴ� �� ���� �ִ�������, �ּҰ������ ������, �� �� ���� ������ ���� �ִ�.
�ּҰ������ � �μ� �� ���� ���� �Ϳ� �ִ������� ���� ���̱� �����̴�.

�������� �� 6 108�� 108 = (x*y)/6�� �ȴ�.
���⼭ �ִ������� �º����� �ű�� 108*6 = x*y�� �ȴ�.
�� x*y�� ���� �ִ����� * �ּҰ������ ������ �����ϴ� ��쿡��,
x�� ���� ���� �ø��� (y���� �ݺ���ϰ� ����) x�� y�� �ִ������� ó���� �Է¹��� �Ͱ� �������� �� ��
x+y���� �� ���� ������ x,y���� ��ü�� �ָ� ���� ���� ���, x,y�� ���� �� ���� ���� ���ؼ� ��ü�� �ش�.
*/

// �̰� �� �������ݾ�...

#include <stdio.h>

// ��Ŭ���� ȣ�������� �ִ����� ���ϱ�
long long euclid(long long a, long long b) {
    while (b) {
        long long r = a % b;
        a = b;
        b = r;
    }
    return a;
}

int main(void) {

    // �ּҰ����, �ִ�����
    long long gcd, lcm;
    scanf("%lld %lld", &gcd, &lcm);

    long long A, B, result_A, result_B;
    long long sum = 200000000; // A + B�� �������� ������ ���� ū ��

    // B = gcd * (lcm / A), A * B = gcd * lcm (A * B / gcd = lcm ���� ����)
    for (long long i = 1;   ; i++) {

        // gcd�� i�� ���ذ��� A�� Ű���.
        A = gcd * i;

        // A�� lcm���� Ŀ���� �ݺ� ����
        if (A > lcm) {
            break;
        }

        // lcm / A�� ����������� ������ continue
        if (lcm % A) {
            continue;
        }

        // B = gcd * (lcm / A)�� �̿� (lcm / A�� ��������� ����)
        B = gcd * (lcm / A);

        // A�� B�� gcd�� �Է°��� �ٸ��� continue
        if (euclid(A, B) != gcd) {
            continue;
        }

        // ���� �պ��� ���� ���� ������ ���� ����
        if (A + B < sum) {
            sum = A + B;
            result_A = A;
            result_B = B;
        }
    }

    printf("%lld %lld", result_A, result_B);

    return 0;
}