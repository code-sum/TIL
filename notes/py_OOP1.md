# ✅객체지향 프로그래밍(OOP) 기본

> Python은 Java와 함께 OOP의 대표 주자
>
> Python 안에 있는 모든 것들이 객체!
>
> 
>
> 객체는 추상화된 레이어기 때문에, 특정 객체의 속성과 메서드를 적절히 활용해서 이걸 어떻게 조작해 나갈 수 있을지를 항상 생각해야 합니다.



## 1. 컴퓨터 프로그래밍 언어

- 파이썬은 모두 객체(object)로 이뤄짐
- 객체(object)는 특정 타입의 인스턴스(instance) 
  - 123, 900, 5는 모두 int의 인스턴스
  - 'hello', 'bye'는 모두 string의 인스턴스
  - [232, 89, 1], []은 모두 list의 인스턴스



---



## 2. 객체지향 프로그래밍

- 객체
  - 객체(object)의 특징
    - 타입(type): 어떤 연산자(operator)와 조작(method)이 가능한가?
    - 속성(attribute): 어떤 상태(데이터)를 가지는가?
    - 조작법(method): 어떤 행위(함수)를 할 수 있는가?
  - 객체지향 프로그래밍이란?
    - 프로그래밍 패러다임 중에 하나
    - 프로그램을 여러 개의 독립된 객체들과 그 객체들 간의 상호작용으로 파악하는 프로그래밍 방법
  - 객체지향의 장점(위키피디아)
    - 객체 지향 프로그래밍은 프로그램을 유연하고 변경이 용이하게 만들기 때문에 대규모 소프트웨어 개발에 많이 사용됨
    - 또한, 프로그래밍을 더 배우기 쉽게 하고 소프트웨어 개발과 보수를 간편하게 하며, 보다 직관적인 코드 분석을 가능하게 하는 장점이 있음



- 절차지향 프로그래밍과의 비교
  - 절차지향: 데이터와 함수로 인한 변화
  - 객체지향: 데이터와 기능(메소드) 분리, **추상화된 구조(인터페이스)**



- 현실 세계를 프로그램 설계에 반영(추상화)

  ```python
  class Person:
      def __init__(self, name, gender):
          self.name = name
          self.gender = gender
          
      def greeting_message(self):
          return f'안녕하세요, {self.name}입니다.'
  ```
  
  ```python
  jimin = Person('지민', '남')
  print(jimin.greeting_message())
  # 안녕하세요, 지민입니다.
  
  jieun = Person('지은', '여')
  print(jieun.greeting_message())
  # 안녕하세요, 지은입니다.
  ```
  
  - 예시: 사각형 넓이/둘레 구하기 코드
  
    - 사각형 R1(10 x 30), 사각형 R2(300 x 20) 넓이/둘레 구하기
  
    ```python
    [절차지향]
    
    a = 10
    b = 30
    square1_area = a * b
    square1_circumference = 2 * (a + b)
    
    c = 300
    d = 20
    square1_area = c * d
    square1_circumference = 2 * (c + d)
    
    ++++++++++++++++++++++++++++++++++++++++
    
    [절차지향2]
    
    def area(x, y):
        return x * y
    
    def circumference(x, y):
        return 2 * (x + y)
    
    a = 10
    b = 30
    c = 300
    d = 20
    
    square1_area = area(a, b)
    square1_circumference = circumference(a, b)
    square2_area = area(c, d)
    square2_circumference = circumference(c, d)
    
    ++++++++++++++++++++++++++++++++++++++++
    
    [객체지향]
    
    class Rectangle:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            
        def area(self):
            return self.x * self.y
        
        def circumference(self):
            return 2 * (self.x + self.y)
        
    r1 = Rectangle(10, 30)
    r1.area()
    r.circumference()
    
    r2 = Rectangle(300, 20)
    r2.area()
    r2.circumference()
    
    ```
  
    - 사각형 - 클래스(class)
    - 각 사각형(R1, R2) - 인스턴스(instance)
    - 사각형의 정보 - 속성(attribute)
      - 가로 길이, 세로 길이
    - 사각형의 행동/기능 - 메소드(method)
      - 넓이를 구한다. 높이를 구한다.



---



## 3. OOP 기초

- 기본 문법

  ```python
  # 클래스 정의
  class MyClass:
      pass
  
  # 인스턴스 생성
  my_instance = MyClass()
  
  # 매서드 호출
  my_instance.my_method()
  
  # 속성
  my_instance.my_attribute
  ```

  

복소수에서 .real 을 찍으면 실수를 볼 수 있음

리스트.정렬() : ~ 행위를 담당

타입이 정말 중요했고, 객체의 다양한 종류들이 타입으로 분류되고 있다



pdf 사례 모든 것이 리스트, 문자열이지만 각자의 실제 값이 존재한다

타입(종류) = class, 값(실제 사례) = instance



객체는 특정 타입의 인스턴스이다.

여기서 '특정 타입'이 바로 클래스!



CamelCase: 클래스를 의미할 때

snake_case: 변수, 함수 이름을 의미할 때

자바에서는 변수, 함수도 CamelCase 사용하는게 일반적이나,

파이썬에서는 위와 같이 구분됩니다!



이 세상에 있는 모든 클래스는 type 의 종류들

모든 인스턴스는 각자 개별적인 클래스로 표현됨

메소드는 클래스 내부에 정의된 함수!



객체 비교하기

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b, a is b)
# True ~~~~
```

```python
[추가 개념] 얕은 복사와 깊은 복사 개념!
아래 코드를 파이썬 튜더로 직접 돌려보기
(실제에서 많이 응용하지는 않음)

1) 얕은 복사의 기본 개념: 1차원상의 리스트가 나뉨(주소가 다름)

a = [1, 2, 3]
b = a
b[0] = 'hi'

print(a) # ['hi', 2, 3]
print(b) # ['hi', 2, 3]

++++++++++++++++++++++++++++++

2) 얕은 복사의 응용

a = [1, 2, 3]
b = a
b[0] = 'hi'

# list 형변환 결과: 사실은 list고 사실은 값도 같지만
# 다른 메모리 주소 결과를 받아냄
c = [3, 4, 5]
d = list(c)
d[0] = 'hi'

# 슬라이싱
e = [4, 5, 6]
f = e[::]
f[0] = 'hi'

++++++++++++++++++++++++++++++

3) 깊은 복사(deep copy)란?
copy.py 라는 내장 모듈을 활용하는 것!

예를 들어, 
a = [[1, 2], 2, 3]
b = list(a)
b[0][0] = 'hi'

print(a) # [['hi', 2], 2, 3]
print(b) # [['hi', 2], 2, 3]
이런 상황에서 

아래와 같이 코드를 바꾼다면,
import copy
a = [[1, 2], 2, 3]
b = copy.deepcopy(a)
b[0][0] = 'hi'

print(a) # [[1, 2], 2, 3]
print(b) # [['hi', 2], 2, 3]
```



인스턴스 메소드: 인스턴스를 조작하기 위한 메소드



코드 한줄~여러줄 위치 마우스 안대고 옮기기

원하는 코드 드래그하고, Alt+위/아래 방향키

