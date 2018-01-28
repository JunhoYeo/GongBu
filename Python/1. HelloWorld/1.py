#안녕세계..? 이건 한 줄 주석이다.
print "Hello World" #파이썬 2
print ("Hello World") #파이썬 3
'''
이건 여러 줄 주석(블럭 코멘트)이다(따옴표3개).
근데 print는 자동으로 뛰어쓰기랑 줄바꿈 등이 맘대로 되버린다.
그럴 땐 아래 메소드를 사용하면 된다.
'''
"""
이건 여러 줄 주석(블럭 코멘트)을 작성하는 또다른 방법이다(쌍따옴표3개).
print문으로는 화면에 데이터를 출력할 수 있다.
"""
import sys #sys 라이브러리를 사용할 수 있도록 데려온다.
sys.stdout.write("Hello World")
#이러면 C언어의 printf문처럼 줄바꿈 없이 사용이 가능하다.
sys.stdout.write("Hello World\n")
'''
이렇게 하면 끝에 줄바꿈이 된다. printf랑 똑같네...
한글 주석이 안 먹히기도 하는데 그럴 땐 IDE의 인코딩 설정을 수정해주면 된다.
Python3에서는 한글로 variable과 function을 define하여 한글코딩도 가능하다.
이는 모든 문자열을 내부적으로 유니코드로 취급하기 때문이다.
'''
