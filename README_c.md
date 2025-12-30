C언어를 시자아아아아아악 하겠습니다아아아

# Baekjoon

2025.08.12 Hello World!

# 궁금사항

scanf는 엔터로 구분된 입력도 그냥 일자로 받아버리네? 어떻게?  
python은 그런 거 못하잖아. 줄바꿈 해서 따로 입력받아야되는데.

# 00. 기타

## 실버 랜덤 디펜스

#### 제곱하기
pow(밑, 지수); 형태로 작성.  
math.h를 가져와야 한다.  

#### 배열 0으로 초기화하기

int nums[정적 변수] = { 0, }; 이러면 모든 요소가 0으로 초기화된다.

## 난이도별 정리

#### '0'으로 숫자 문자 변환하기

1. 문자 → 숫자 변환할 때 (빼기)
   char c = '7';
   int n = c - '0'; // n = 7

'7'의 아스키 코드 = 55
'0'의 아스키 코드 = 48

55 - 48 = 7
👉 문자 '7'을 정수 7로 바꿀 때는 - '0'.

2. 숫자 → 문자 변환할 때 (더하기)
   int n = 7;
   char c = '0' + n; // c = '7'

'0' = 48

48 + 7 = 55 → 아스키 코드 55는 '7'
👉 정수 7을 문자 '7'로 바꿀 때는 + '0'

#### <string.h> strcspn

`string[strcspn(string, "\n")] = '\0';`
strcspn(string, "\n") → string에서 처음 \n이 나오는 위치의 인덱스를 반환.  
그 자리를 '\0'로 바꿔버림. 결과적으로 문자열에서 개행 문자가 잘려나감.

strcspn은 왼쪽부터 확인하는 놈이다.  
어차피 한줄을 읽을 때 \n은 마지막에 한번만 들어오니 rstrip처럼 쓸 수 있다.

#### 포인터 배열

브1 1924.c

포인터 배열은 "주소"를 원소로 가지는 배열이다.  
각 원소는 문자열(또는 데이터)이 저장된 위치를 가리킨다.  
따라서 길이가 다른 문자열들도 함께 저장할 수 있다.

    #include <stdio.h>
    int main(void) {
        const char *wname[3] = {"SUN","MOND","WE"};
        for (int i=0;i<3;i++) printf("%s\n", wname[i]);
        return 0;
    }

## 랜덤 마라톤 74

#### switch-case문
파이썬에 매치케이스가 있다면 c언어에는 스위치케이스가 있다.  
다만 정수형에 대해서만 가능. char는 정수형이므로 쌉가능.  

    switch(x)
    {
    case 'a':
        break;
    default:
        break;
    }
이런 느낌.

#### INT_MAX, INT_MIN, LLOMG_MIN 등등
<limits.h>에 있다. inf, -inf를 의미함.  

## 랜덤 마라톤 70

#### `%*d, %*f`
저런 느낌으로 쓰면 값을 읽되 버리는 형식. 중복으로 들어올 때 사용하자.   

## 랜덤 마라톤 65

#### <stdlib.h> qsort

qsort는 배열을 정렬하는 c언어의 소중한 내장함수.  
`qsort(arr, size, sizeof(int), compare);`  
여기서 compare는 직접 짜줘야한다.

    void qsort(
        void *base,            // 정렬할 '배열의 시작 주소'
        size_t nmemb,          // 원소(칸) 개수
        size_t size,           // 원소 하나의 바이트 크기(예: int면 sizeof(int))
        int (*compar)(const void*, const void*) // '두 원소를 비교'하는 함수
    );

compare는 배열에서 임의로 2개의 원소를 집어 비교한다.  
qsort는 어떤 타입의 배열이든 정렬할 수 있어야 합니다.  
그래서 원소 타입을 모르니까 → 매개변수 타입을 (const void*)로 통일해둡니다.  
비교 함수 안에서 다시 (int*)로 바꿔야 정수 값을 꺼낼 수 있습니다.  
(int*)a는 주소를 가리키고 있으니, *를 붙여 값으로 꺼낸다.  
(int\*)는 그냥 이 포인터가 int형이라는 것일 뿐이지롱.

    int compare(const void *a, const void *b) {
        int num1 = *(int*)a; // (1) a를 int*로 캐스팅 → 역참조(*)로 값 획득
        int num2 = *(int*)b; // (2) b도 동일
        if (num1 < num2) return -1; // (3) num1이 더 작으면 '앞으로'(-1)
        else if (num1 > num2) return 1; // (4) num1이 더 크면 '뒤로'(+1)
        else return 0; // (5) 같으면 0
    }

return (x > y) - (x < y); 이거로 (3, 4, 5)단계 날먹도 가능하다. (오름차순)

#### 투 포인터

두 개의 정렬된 배열을 합쳐 정렬하려면 배열마다 0에서 시작하는 포인터를 만들어주고,  
포인터가 가리키는 값이 작은 걸 출력 후 그 포인터를 한 칸 앞으로 보내는 것을 반복하는 것이다.

#### 포인터와 const

일단 const가 앞에 붙으면, 기본적으로 그 데이터가 수정 불가능하다는 의미이다.  
주소가 바뀌지 않아서가 아니라, 데이터를 건드리지 않기 때문에 `const char *`를 쓰는 것.

const char *p; // (1) "데이터"가 const: *p 수정 불가, p는 다른 곳을 가리키게 변경 가능  
char * const p; // (2) "포인터"가 const: p 재지정 불가, *p 수정 가능  
const char * const p; // (3) 둘 다 const: p 재지정 불가, *p 수정 불가

#### 포인터

`char *p = string;`
string[0]을 가리키는 포인터. p는 string[0]의 주소, \*p는 그 값. 즉 string[0] 자체

주소를 입력받는다.

    // (1) 배열과 포인터가 같은 결과인지 확인
    int a[3] = {10,20,30};
    int *p = a;
    printf("%d %d %d\n", a[2], *(a+2), p[2]); // 모두 30

    // (2) 문자열 이동
    char s[] = "HELLO";
    char *q = s + 1; // 'E'부터
    printf("%c %c\n", s[1], q[0]); // E E

    // (3) 6글자 조각 비교
    const char *x = "011100001111"; // "011100" + "001111"
    const char *c1 = x;       // 첫 6글자
    const char *c2 = x + 6;   // 다음 6글자
    // c1[0..5], c2[0..5] 각각 비교해보기

## 랜덤 마라톤 64

#### size_t

size_t는 "메모리의 크기나 길이를 나타낼 때 쓰는 자료형"이다.  
printf로 출력할 때는 %zu를 사용한다.

#### <string.h> strlen

문자열의 내용 길이를 반환한다. 배열이 얼마나 차 있는지를 반환한다고 생각하면 됨.  
널문자 \0이 나올 때까지 읽는다.  
`char arr[256] = "Hello";`
`printf("%zu\n", strlen(arr));   // 5  ('H','e','l','l','o');`

#### <stdio.h> sizeof

문자열 길이와 상관 없이 배열의 메모리 크기를 반환한다.  
`char arr[256];`
`printf("%zu\n", sizeof(arr));   // 256  (배열 전체 크기)`

#### && "" !

and &&, or ||, not !

#### abs()

파이썬과 동일하게 작동한다는거임. 절댓값 반환

#### 삼항 연산자 (조건 연산자)

`printf("%d", (X < Y) ? X : Y)` 이런 느낌  
조건식 ? 값1 : 값2  
조건식이 참(≠0)이면 → 값1 반환  
조건식이 거짓(=0)이면 → 값2 반환

#### static

static (함수 앞) → 이 파일 안에서만 쓸 수 있는 함수.  
여러 .c 파일을 묶어서 컴파일할 때, 함수 이름 충돌을 막아준다.

#### void

void → 함수가 값을 반환하지 않는다는 의미. 함수의 반환형(return type)이다.

#### int(input()) 을 c언어로 구현해보자

    #include <stdio.h>
    #include <stdlib.h>

    int main(void) {
        // 동적 메모리로 입력 버퍼 준비 (파이썬 input()처럼 가변적이라 가정)
        char *arr = malloc(100);  // 최대 99글자 + '\0' 입력 가능

        // 문자열 입력 (개행\0 포함됨)
        fgets(arr, 100, stdin);

        // 문자열 → 정수 변환 (에러 체크 생략)
        int x = atoi(arr);

        printf("%d\n", x);

        free(arr);  // malloc으로 확보했으니 해제
        return 0;
    }

#### <stdio.h> fgets

`char arr[256];`  
`fgets(arr, sizeof(arr), stdin);`  
말 그대로 input()의 느낌이다. 문자열+개행까지 입력받는다.  
최대 size-1 글자만 읽고 마지막에 \0 자동 추가.

#### stdin이 뭐냐고?

stdin : Standard Input (표준 입력, 보통 키보드)  
stdout : Standard Output (표준 출력, 보통 화면)  
stderr : Standard Error (에러 메시지 출력, 보통 화면)

#### <stdlib.h> malloc

`char *s = malloc(n + 1);` // 문자 n개 + '\0'
`s[n] = '\0'; ` // 직접 문자열의 끝을 표시해줘야 한다.

`int *arr = malloc(n * sizeof(int));` // n칸짜리 int 배열 만들기

`free(arr)` // 사용한 메모리를 꼭 반납해야 한다.

#### "큰따옴표", '작은따옴표'

"큰따옴표"는 char배열. 문자열이다. 끝에 \0이 붙는 문자열이다.  
'작은따옴표'는 그냥 char. 문자. 1바이트 정수다. 끝에 \0이 붙지 않는 한 글자다.

char c = 'a'; // 문자 하나 (ASCII 97)  
char s[] = "a"; // 문자 배열 {'a','\0'}

#### <stdlib.h> atoi(str);

이건 파이썬의 int(str)과 똑같은 역할을 한다.

#### <string.h> strcat(arr, "str");

strcat은 문자열을 이어붙이는 역할을 한다. arr의 가장 끝에 str을 붙여준다.  
배열의 크기를 초과하면 오류가 날 수 있다.

# 01. 단계별로 풀어보기

## 01. 입출력과 사칙연산 250817 ~

#### 배열 입력받기

    int nums[3], temp;
    for (int i = 0; i < 3; i++){
        scanf("%d", nums + i);
    }

&nums[i] 로 직접 주소를 입력할 수도 있다. nums + i 역시 같은 의미다.

#### int main, void main

int main(){ }로 돌릴 코드를 만들어준다.  
int랑 void는 우리가 사용할 땐 차이가 없다. 컴퓨터 방식의 차이일 뿐.  
웬만하면 int로 사용하는 것이 권장된다고 한다.

#### scanf("%d", &A)

input의 역할을 한다. 주소 값을 전달해야 하므로 &를 꼭 붙이자.

    %d : 10진수 정수 자료형
    %c : 문자 자료형 char
    %f : 부동소수 자료형 float
    %s : 문자열 자료형

#### 코드의 끝에는 ;를 붙인다

이게 없으면 c언어는 인식을 못하고 오류가 터져버린다.

#### return 0;

함수의 마지막에 써준다. 에러 없이 정상적으로 함수가 종료되었다는 것을 알리기 위함이다.  
솔직히 파이썬에서도 return안해도 함수 끝나는데 그냥 쓰잖슴. 그런거임.

#### 변수 정의

`int a = 10;` 이건 생성과 동시에 대입  
`int a; a = 10;` 이건 생성 후에 대입  
정수형 변수와 실수형 변수로 나눠진다.  
정수형 변수: char, short, int, long  
실수형 변수: float, double, long double

#### #include <stdio.h>

일단 시작은 #include <stdio.h>로 간다. import하는거임.  
stdio.h는 표준입출력파일이며 scanf, printf등 기본적인 함수들이 정의되어 있다.
