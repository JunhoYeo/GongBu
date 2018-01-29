# Python Interpreter
이번에는 파이썬 인터프리터에 대해 다뤄볼 것이다.

# Interpreter

## What is the Interpreter?
인터프리터란 무엇일까?</br>
인터프리터의 뜻을 검색엔진에 검색해 보면 '통역사'라고 나온다.</br>
북한어로는 '해석기'라고 나오는데, 인터프리터는 바로 그러한 역할을 한다.</br>
고급 프로그래밍 언어로 작성된 프로그램을 한 줄씩 입력받아서 실행하는 것이다.

## How does it works?
인터프리터는 보통 아래와 같은 방법을 사용하여 실행된다.

- 소스 코드를 직접 실행한다.
- 소스 코드를 다른 언어로 변환하고 이를 실행한다.
- 미리 컴파일된 코드를 호출한다.

# Python Interactive Interpreter
파이썬의 인터프리터를 Terminal에서 실행할 경우 대화형 모드로 동작하게 할 수 있다.
```
C:\Users\JunhoYeo>python
Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Hello World")
Hello World
>>>
```
이번 기회에 필자도 Python2에서 Python3으로 업그레이드했다.

## 대화형 인터프리터를 사용하면...
```
C:\Users\JunhoYeo>python
Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 1+1
2
>>> a=0
>>> a+=1
>>> print(a)
1
>>> hex(a)
'0x1'
>>> exit()

C:\Users\JunhoYeo>
```
대화형 인터프리터를 사용하면 바로 Terminal에서 간단한 코드를 실행하면서 대화하듯이 프로그래밍할 수 있다.

## 대화형 인터프리터에서...
```
C:\Users\JunhoYeo>python
Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> a=True
>>> if a is True:
...     print("Hello World")
...
Hello World
>>>
```
위와 같은 방법으로 if/elif/else, for, while 등의 구문을 사용할 수 있다.
```
C:\Users\JunhoYeo>python
Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> def helloworld():
...     print("Hello World")
...
>>> helloworld()
Hello World
>>>
```
요렇게 함수 사용도 가능하다.</br>
파이썬은 들여쓰기를 통해서 블럭을 구분하므로 꼭 화이트스페이스를 이용하자.

# 마지막으로
```python
#C:\Users\JunhoYeo\Desktop\hello.py
print("Hello World")
```
```
C:\Users\JunhoYeo>cd desktop

C:\Users\JunhoYeo\Desktop>python hello.py
Hello World

C:\Users\JunhoYeo\Desktop>
```
대규모 프로그램이나 프로젝트나 뭐 그런 작업을 할 때는 인터프리터에서 실행하는 것보다 ~~당연한 건데~~ 따로 스크립트를 짜는 것이 좋다.</br>
위처럼 Terminal에서 파일이 있는 디렉토리로 이동해서 실행하면 바로 실행할 수 있다.</br>
뭐 물론 왠만한 IDE에선 바로 열어주지만...
