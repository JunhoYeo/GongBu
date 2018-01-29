# Variables
```python
Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> a = 1 #a라는 변수에 1을 할당
>>> print(a)
1
>>> a+=1 #파이썬에는 증감연산자가 없으므로 축약형을 사용
>>> print(a)
2
>>> type(a) #자료형을 확인해보자
<class 'int'>
>>> hex(a) #16진수
'0x2'
>>> b=64; chr(b) #두 가지 연산을 한 줄에
'@'
>>> b+=1; chr(b) #chr()로는 아스키 코드 번호의 문자를 출력할 수 있다
'A'
>>> b='A'
>>> ord(b) #문자를 아스키 코드로
65
>>> type(b)
<class 'str'>
>>> c="Hello World"
>>> print(c)
Hello World
>>> type(c)
<class 'str'>
>>> d=0.2345675435 #막친겁니다
>>> type(d) #실수(float)
<class 'float'>
>>>
```

## I love Korean
부재 : Python3을 다운받고 해보고 꼭 해보고 싶었던 것
```python
Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> #한글코딩은 불편하고 메모리도 많이 먹지만 재미있다
...
>>> 일=1; 이=2; 삼=3; 사=4; 오=5
>>> print(일)
1
>>> print(일+이)
3
>>> print(일+이/삼+사**오/이+(일+이)/삼+사) #뭐래
518.6666666666666
>>>
```

# Operators

## 수학
```python
Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 1 + 1 #답은 귀요미입니다
2
>>> 1 - 1 #뺄셈
0
>>> 2 * 9 #아나
18
>>> 6 * 3 #빌딩
18
>>> 10 / 5 #나눗셈
2.0
>>> 1 / 0 #0으로 나누기(이것도 너프해 보시지!)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> 4 % 2 #나머지
0
>>> 3 // 2 #몫
1
>>> 2**2 #지수연산
4
>>>
```

## 비교 연산자
```python
Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 1 > 0
True
>>> 1 >= 0
True
>>> 1 >= 1
True
>>> 1 < 0
False
>>> 1 <= 0
False
>>> 1 <= 1
True
>>> True == False
False
>>> True == True
True
>>> True != False
True
>>> True != True
False
>>>
```

## 논리 연산자
```python
Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> True or True
True
>>> True or False
True
>>> False or False
False
>>> True and True
True
>>> True and False
False
>>> False and False
False
>>> True is not False
True
>>> True is not True
False
>>> True is False
False
>>> True is True
True
>>>
```
여기까지만 하는걸로!!
