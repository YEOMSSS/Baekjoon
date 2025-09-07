
package pkg1; // 패키지는 항상 맨 위에 있어야 한다.

import java.util.Scanner; // 자동으로 생기긴 하는데, 잘 챙기자.

public class EX03 {

    public static void main(String[] args) {
        
        // final로 선언하면 상수가 되어 바꿀 수 없다. const?
        // final 한 번 입력하면 다음번엔 바꿀 수 없다는 의미. 차이점이라는데. 다른거였어? 나눠서 할 수 있다가 뭔뜻이지?
        final double PI = 3.141592;
        System.out.println("pi : " + PI);


        Scanner sc = new Scanner(System.in);
        int num1, num2;

        System.out.println("input two numbers : ");
        num1 = sc.nextInt();
        num2 = sc.nextInt();

        int result = maxValue(num1, num2);
        System.out.println("bigger : " + result);

        sc.close(); // free???
    }
    
    // 큰 수 찾는 함수를 만들어볼까?
    // 이거는 c언어랑 똑같은 거 같은데? int형 반환.
    // main에 static이 붙어있으니 define한 함수에도 static을 붙여주자.
    static int maxValue(int n, int m) {
        if (n >= m) return n;
        else return m;
    }
}

// 자바 존나 어려운데??