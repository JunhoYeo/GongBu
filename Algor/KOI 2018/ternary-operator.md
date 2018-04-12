# 삼항연산자 (Ternary operator)
기출문제 봤는데 삼항연산자에 대한 지식이 좀 많이 심각하게 없는 것 같아서 훑어보려고 한다.

## 위키피디아에는
삼항 연산에 대한 한글 항목이 없었다.

대신 영어 항목이 있길래 읽어보니

> In computer science, a ternary operator is an operator that takes three arguments.[1] The arguments and result can be of different types. Many programming languages that use C-like syntax[2] feature a ternary operator, `?:`, which defines a conditional expression. Since this operator is often the only existing ternary operator in the language, it is sometimes simply referred to as "the ternary operator". In some languages, this operator is referred to as "the conditional operator". Another example for a ternary operator is `between`, as used in SQL.

뭐라는거지.. 번역기를 돌려보니

> 에서 컴퓨터 과학 하는 삼항 연산자는 이다 운영자 세 개의 인수를 취합니다. [1] 논쟁과 결과는 다른 유형이 될 수 있습니다. C와 유사한 문법 [2] 을 사용하는 많은 프로그래밍 언어 `?:`는 조건식 을 정의하는 삼항 연산자를 특징으로 합니다 . 이 연산자는 종종 언어에서 유일하게 기존의 삼항 연산자이기 때문에, 때로는 단순히 "라고 삼항 연산자". 일부 언어에서는이 연산자를 "조건부 연산자"라고합니다. 삼원 연산자에 대한 또 다른 예는 `사이` 에 사용 된 바와 같이, SQL .

?????그냥 영어로 ~~해독~~읽어봐야겠다...

삼항연산자라는 녀석은 아마도 아래 같은 특징을 가지는 것으로 추정된다.

- 삼항연산자(Ternary operator)는 세 개의 인수를 가지는 연산자이다.
- `?:`를 사용한다.
- `the ternary operator`(삼항 연산자), `the conditional operator`(조건부 연산자)라고 한다.
- SQL 등에서는 `between`을 쓴다.

## 사용법
<h1><code>(조건) ? (참일 때) : (거짓일 때)</code></h1>
조건, 조건이 참일 때 값, 거짓일 때 값을 argument로 받아서 조건이 참이면 참일 때 값을, 거짓이면 거짓일 때 값을 사용하게 해준다.

## 문제
KOI 2016 지역대회 중고등부 32번 문제

`다음 중 f(1) + f(3) + f(5) + ... + f(2n-1)을 구하기 위해 필요한 식은?`

1. `f(n)`
2. `f(n+1)`
3. `f(2*n-1)`
4. `f(2*n)`
5. `f(2*n+1)`

사실 공부하기 전에는 주어진 코드가 뭔 코드인지도 모르고 걍 그래프 그리면서 하나하나 계산해 봤다.

그랬더니 5번이 나왔다. 답안지는 내게 틀렸다고 했다.

```C
int f(int a){
  return a <= 1 ? a : f(a-1) + f(a-2);
}
```

위 코드에서 `a <= 1`는 `조건`, `a`는 조건이 참일 때 값, `f(a-1) + f(a-2)`는 조건이 거짓일 때 값이다.

따라서 함수 `f`는 `a <= 1`이 `true`면 `a`를 리턴하고 `false면` `f(a-1) + f(a-2)`를 리턴하는 함수인 것이다.

즉 삼항연산자를 사용하지 않고 아래처럼도 표현이 가능하다.

```C
int f(int a){
  if (a <= 1) return a;
  else return f(a-1) + f(a-2);
}
```

정수 n을 입력받고 n번째 피보나치 수를 구하는 함수다.

```C
#include <stdio.h>
int f(int a){
  return a <= 1 ? a : f(a-1) + f(a-2);
}
int main(){
  int a;
  scanf("%d", &a);
  printf("%d", f(a));
  return 0;
}
```

위와 같은 소스코드를 돌려서 테스트할 수 있다.

<!-- 뭐 문제를 풀어보기 위해서 `n`을 내 맘대로 잡아볼 것이다. 7이라고 해야지~!
`n = 7` -->
<!-- 그러면 `f(2n-1)`은
`2n-1 = 2*7-1 = 13`
`f(2n-1) = f(13)` -->
<!-- 피보나치 수는 0과 1로 시작하고 바로 앞의 두 수의 합이 계속 이어지는 식이라니까 앞부분을 얼른 구해보면 다음과 같이 될 것이다.
`0, 1, 1, 2, 3, 5, 8, 13, 21 ...`
근데 이 함수에서는 1번째 피보나치 수가 1이니까 맨 앞의 0을 빼자.
`1, 1, 2, 3, 5, 8, 13, 21 ...`
그러면 '구해야 하는 것'인 `f(1) + f(3) + f(5) + ... + f(2n-1)`은
`f(1) + f(3) + f(5) + f(7) + f(9) + f(11) + f(13)`
각 선택지별로 보면
1. `f(n) = f(7)`<br>
2. `f(n+1) = f(7+1) = f(8)`<br>
3. `f(2*n-1) = f(2*7-1) = f(13)`<br>
4. `f(2*n) = f(2*7) = f(14)`<br>
5. `f(2*n+1) = f(15)`<br>
음??? 이거 어캐풀지? 친구들햔테 물어봐야겠다 ^_^
-----
>친구 : `f(n)`은 `f(1)`부터 시작.
`f(1)` 다음은 `f(3)`, `f(5)`, 즉 답은 `f(2*n)`
...??? 이거 뭔가 번역기돌린 삼항연산자가 설명된 영어위키피디아같은데 -->

아무말로 풀어보다가 말아먹고 친구햔테 물어봄

친구가 명쾌한 풀이를 알려줘서 주석처리해둠(마크다운 문서를 열면 확인할 수 있을거임)

친구가 알려준 대로 진행하겠음

문제를 직접 푸는 것은 둘째치고 답안지는 4번(`f(2*n)`)이라고 하는데 그게 이해 안되서 그거라도 이해하려고 함

- 함수 `f`는 정수 `a`를 입력받고 `a`가 1보다 크다면 `f(a-1) + f(a-2)`를 리턴함

- 따라서 `f(a) = f(a-1) + f(a-2)`라고 할 수 있음

- `f(2*n)`이 답이 맞는지를 확인하려고 하니까 `a` 대신 `2n`을 넣자

- `f(2n) = f(2n-1) + f(2n-2)`

- 이때 `f(2n-2) = f(2n-2-1) + f(2n-2-2)`이니까 `f(2n-2) = f(2n-3) + f(2n-4)`

- 그러면 `f(2n) = f(2n-1) + f(2n-2) = f(2n-1) + f(2n-3) + f(2n-4)`

- `f(2n-4)`도 위와 같은 방법으로 분해가 가능

- 이런 식으로 계속 반복하면 `f(2n) = f(2n-1) + f(2n-3) + f(2n-5) + ... + f(5) + f(3) + f(1)`

- 어? 어디서 많이 본 것 같네??

- 나온 식에서 순서만 바꾸면 `f(1) + f(3) + f(5) + ... + f(2n-1)`

- 따라서 답은 `f(2n)`, 즉 `f(2*n)`(4번)

헐... X나 어려운데 매우 재미있음

> Special Thanks to 김태현
