package pkg1;

import java.util.Scanner; // 스캐너라는 이름의 클래스를 불러온다. #include. 파이썬의 import와 동일.

public class EX02 {

    public static void main(String[] args) {

        // 자바에서 클래스 변수를 선언하는 방법. 여기서는 스캐너변수를 sc로 가져왔다. import as 같은건가?
        // System.in은 키보드로부터 입력받는 변수를 의미. std in같은거임
        Scanner sc = new Scanner(System.in);
        
        System.out.println("input here");
        
        String s = sc.nextLine(); // boolean 입력받은 후에 next는 되는데 nextLine은 왜 안됨??
        System.out.println("your input : " + s);
        
        // input이나 scanf같은 느낌으로 쓴다. 다만 ja va는 자료형마다 그게 달라.
        int x = sc.nextInt(); // 입력받은게 x에 바로 저장됨.
        System.out.println("your input : " + x); // 바로 출력.
        
        double y = sc.nextDouble();
        System.out.println("your input : " + y);
        
        boolean z = sc.nextBoolean();
        System.out.println("your input : " + z);

        
        
        /*
        int a, b;
        a = 23;
        b = 45;

        System.out.println("plus" + a + b); // 글자랑 숫자랑 더하면 글자가 된다.
        System.out.println("plus" + (a + b)); // 이렇게 계산을 먼저 해주면 됨.
        System.out.println("mult" + (a * b));
        */

        sc.close(); // malloc free같은 느낌인건가?
    }
}