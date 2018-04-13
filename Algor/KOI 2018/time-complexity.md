# 시간복잡도 (Time complexity)
프로그램 P에 의해 소요되는 시간 T(P)는 컴파일 시간 + 실행 시간

- 컴파일 시간은 인스턴트 특성에 의존 X, 검증되면 다시 컴파일할 필요 없이 여러 번 수행 가능<br>
=> 프로그램의 실행 시간만 염두에 두자

- 프로그램의 실행 시간 ![equation](https://latex.codecogs.com/gif.latex?T_%7Bp%7D%28n%29%3Dc_%7Ba%7DADD%28n%29&plus;c_%7Bs%7DSUB%28n%29&plus;c_%7Bl%7DLDA%28n%29&plus;c_%7Bst%7DSTA%28n%29)<br>
c는 각각의 연산을 수행하기 위해 필요한 시간을 나타내는 상수
ADD, SUB, LDA, STA는 덧셈/뺄셈/적재/저장 연산이 실행되는 횟수

## 나무위키에는
> 컴퓨터 공학 용어로, 컴퓨터 프로그램의 입력값과 연산 수행 시간의 상관관계를 나타내는 척도이다. 일반적으로 시간 복잡도는 점근 표기법을 이용하여 나타낸다.<br>
정의에서 알 수 있는 사실이지만, 시간 복잡도와 로직의 수행 시간은 비례하므로 시간 복잡도 수치가 작을수록 효율적인 알고리즘임을 뜻한다.

~~정의에서도 잘 모르겠는데요~~

## 테이블 방식 (Table method)

- 문장에 대한 단계수(`steps/execution`, `s/e`)
- 빈도수(Frequency)
- `총 단계수 = 빈도수 * s/e`
- 총계를 모두 합하면 전체 함수의 단계수가 됨

단계의 개념 자체가 부정확<br>
단계수는 두 프로그램을 비교하려는 목적에는 유용하지 않음

## 점근 표기법 (Asymptotic notation)
내가 만든 알고리즘이 얼마나 효율적인가? 의 지표<br>
입력의 크기가 커짐에 따라 소요 시간이 얼마나 빠르게 커지는가?

계산 복잡도는 하드웨어 사양에 관계없이 순수한(?) 알고리즘 그 자체를 대상으로 매겨짐

점근 표기법에는 빅 오(Big-O), 오메가, 세타 표기법 등이 있는데 빅 오만 다루고 넘어가자.

## 빅 오 표기법 (Big-O notation)


~~계속 Bing-O라고 치게 됬다~~

책에는 Big-Oh라고 나오고 위키피디아에서는 Big-O라고 나옴<br>
(표기가 제각각인 것 같아서 그냥 Big-O로 하는 걸로)

사실 어떻게 구하는 건지는 잘 모르겠음

오늘은 창체의 날인지 뭔지라서 4시간 동안 배드민턴 동아리로 강당에서 갇혀 있어서 2시간 동안 5번쯤 반복해서 읽었는데 그래도 이해가 안 되서 패스

- `O(1)` : 연산 시간이 상수(Constant)
- `O(n)` : 선형
- `O(n**2)` : 평방형
- `O(n**3)` : 입방형
- `O(2**n)` : 지수형(Exponential)<br>
입력 데이터가 커질 때마다 처리시간이 두 배씩 증가함<br>
보통 브루트포스(Brute Force) 알고리즘이 해당된다.
- `O(log n)` : 로그(Logarithmic) 형태<br>
데이터양이 커져도 시간이 조금씩 늘어남
- `O(n log n)` : 선형로그 형태<br>
데이터양이 n배 늘어나면 실행 시간은 n배보다 조금 더 많아짐(정비례 x)<br>
`O(n**2)`보다 조금 더 나음(참고 항목에 기재한 맨 아래 스택오버플로우 링크 참조)
- `O(n!)` : 팩토리얼 형태(Factorial), 좀 많이 끔찍함

## 예시
```C
#include <stdio.h>
int main(){
  printf("Hello World\n");
  return 0;
}
```
위 코드의 시간복잡도를 빅 오 표기법으로 나타내면 (당연히) `O(1)`이다.

-----

```Python
def function(n, q):
  for item in n:
    if item==q:
      return True
  return False
```
그냥 Python으로 얼른 예제를 만들었는데 시간복잡도를 구해보면 `O(n)`이 나올 것이다.<br>
n이라는 리스트를 받아서 q라는 항목이 있으면 참을, 없으면 거짓을 리턴하는 함수다.
```Python
>>> def function(list, q):
...   for item in list:
...     if item==q:
...       return True
...   return False
...
>>> list = [1, 2, 3, 4, 5]
>>> q = 4
>>> function(list, q)
True
>>>
```
ㅇㅇ 이렇게 실행되는 거임

> 어 잠만? 위 실행 결과를 보면 크기 5짜리 리스트에서 숫자 4가 3번째 인덱스에 있는데 q를 찾으면 바로 참이 리턴되니까 O(n) 아닌 거 아님??

- ㄴㄴ 빅 오 표기법은 대부분 최악의 경우(Worst case)를 표현!!

- 만약 위에서 최악의 경우에 속한다고 할 수 있는 `function(n, 5)`을 호출하면 O(n)으로 나오니까 그래서 O(n)이라고 할 수 있는 것!

- 아니 그것도 그런데 우리는 함수 부분만의 시간복잡도를 구하는거니까 당연히 O(n)이지

- 음?? 진짜 그렇네

> 사실 자문자답이므로 필자 수준이 들어나는 부분이였던거임

-----

```Python
def function(q, n, matrix):
  for i in range(0, n):
    for j in range(0, n):
      if matrix[i][j]==q:
        return True
  return False
```
자 역시 Python으로 급하게 만든 이 녀석은 위에 꺼랑 좀 비슷한데 다르다.

저번 껀 1차원 리스트였다면 이건 2차원 리스트다.

중첩 for 문을 사용해서 리스트를 탐색해서 q를 찾는 함수다.

matrix는 n*n 사이즈의 2차원 배열이라고 하자(즉, `n = len(matrix)`).

for 문이 중첩되었기 때문에 `matrix[i][j]==q`인지 확인하는 코드가 `n**2`번 실행되게 된다.

입력 데이터인 n의 거듭제곱 번 실행되므로 이 함수의 시간복잡도는 `O(n**2)`이라고 할 수 있다.

예제는 여기까지~!

## 문제
KOI 2016 지역대회 중고등부 31번 문제
```C
int check[101] = {0, }, m = 100;
int n = (a) ;
int a[100] = (b) ;
int i, j, p = 0;
for (i = 0; i < n; i++) {
  check[a[i]]++;
}
for (i = 1; i <= m; i++) {
  int cnt = 0;
  for (j = i; j <= m; j += i) {
    cnt += check[j];
  }
  if (cnt >= 2) p++;
}
```

`(2점) 이 프로그램의 시간복잡도로 가장 적합한 것은 무엇인가?`

1. `O(n)`
2. `O(n log(n))`
3. `O(n + m log(m))`
4. `O(n**2 + m)`
5. `O(n + m**2)`

5번인 줄 알았는데 자세히 보니까 두 번째 루프에서 중첩되는 부분이 i에서 시작되니까 `O(n + m**2)`보다 조금 더 나음

따라서 답은 `O(n + m log(m))`, 3번이다.

## 참고

- C로 쓴 자료구조론(Fundamentals of Data Structures in C / Horowitz Sahni Anderson-Freed)
- https://wayhome25.github.io/cs/2017/04/20/cs-26-bigO/
- http://www.mydiyworld.net/?p=440
- https://en.wikipedia.org/wiki/Big_O_notation
- https://ko.wikipedia.org/wiki/%EC%A0%90%EA%B7%BC_%ED%91%9C%EA%B8%B0%EB%B2%95
- https://namu.wiki/w/%EC%8B%9C%EA%B0%84%20%EB%B3%B5%EC%9E%A1%EB%8F%84
- https://namu.wiki/w/%EC%A0%90%EA%B7%BC%20%ED%91%9C%EA%B8%B0%EB%B2%95
- https://stackoverflow.com/questions/23329234/which-is-better-on-log-n-or-on2
