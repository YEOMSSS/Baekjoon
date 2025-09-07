package pkg1;

public class EX01 {

     public static void main(String[] arg){

        int a = 100;

        // println은 \n이 포함된 printf라고 생각하면 편함
        // println은 무조건 한 개만 출력한다.
        // 여러개를 출력하고 싶다면 +를 쓰면 된다. 물론 덧셈이 우선되니, 문자열로 만들어서 합칠것
        System.out.println(a);

        double b = 12.345;
        System.out.println(a + " " + b); // 자바에서 여러데이터를 하나로 출력하는 법.
        // 문자열로 바꿔서 출력하는 것. 문자열과 변수가 합쳐지면 변수를 문자열로 바꾼 후 합친다.

        char c = 'C';
        System.out.print(c); // 그냥 print로 쓰면 \n없이 출력됨

        byte d = 120; // 한바이트면 127까지 저장가능 8비트 11111111
        System.out.printf("%d\n", d); // 세상에, printf도 지원하네요.

        boolean e = true;
        System.out.println(e);

        String s = "HONG";
        System.out.println(s);

        
    }
}