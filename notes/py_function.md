# ✅Python 함수

>1. 함수 기초
>2. 함수의 결과값(Output)
>3. 함수의 입력(Input)
>4. 함수의 범위(Scope)
>5. 함수 응용
>
>💡 [학습자료1: Python 자습서](https://docs.python.org/ko/3/tutorial/index.html)
>
>💡 [학습자료2: Python 표준 라이브러리](https://docs.python.org/ko/3/library/index.html)
>
>* 기타 추천 자료: 파이썬 코딩 도장, 점프 투 파이썬, MIT Python



## Intro.

* 내장함수 `len('happy!')` 의 기능

  ```python
  word = 'happy!'
  cnt = 0
  
  for char in word:
      cnt += 1
      
  print(cnt)
  ```

* 내장함수 `sum([1, 10, 100])` 의 기능

  ```python
  numbers = [1, 10, 100]
  result = 0
  
  for number in numbers:
  	result += number
  
  print(result)
  ```

* 함수를 사용하는 이유?

  ① Decomposition: 기능을 분해해서 재사용 할 수 있음

  ```python
  상황1)
  numbers = [1, 10, 100]
  result = 0
  cnt = 0
  
  for number in numbers:
  	result += number
  	cnt += 1
      
  print(result/cnt)
  
  상황2)
  print(sum(numbers)/len(numbers))
  
  # 상황1 과 상황2의 결과 값은 같다(그러나 상황2의 코드가 훨씬 간결!)
  ```

  ② Abstraction: 복잡한 내용을 숨기고 기능에 집중하여 사용할 수 있음(블랙박스처럼)

  * 재사용성, 가독성, 생산성

  ```python
  name = '파이썬'
  # 파이썬이라는 문자열을 name 에 할당하고 있음
  # 수많은 데이터 중에 어떤 것을 선택해 이름을 부여해 쓰고 있음
  
  print('happy hacking!')
  # 문자열 'happy hacking!' 을 넣으면, 이걸 출력해준다는게
  # print() 함수가 보장해주는 약속!
  ```

  

* 위의 Intro 내용을 종합했을때, 

​		함수란 **'블랙박스에 Input 을 넣으면 Output 을 줄게!'** 하는 약속



---



## 1. 함수 기초

* 함수의 정의

  * 함수(Function)
    * 특정 기능을 하는 코드의 조각(묶음)
    * 특정 명령을 수행하는 코드를 매번 다시 작성하지 않고, 필요 시에만 호출하여 간편히 사용


  * 사용자 함수(Custom Function)
    * 구현되어 있는 함수가 없는 경우, 사용자가 직접 함수를 작성 가능
    
    ```python
    def function_name
    	# code block
        return returning_value
    ```

  * 함수를 사용해야 하는 이유
    * 코드 중복 방지 / 재사용 용이
    * 다양한 내장함수(Built-in Function) 지원
    * `pstdev` 함수 (파이썬 표준 라이브러리 - `statistics`)
      * [statistics & pstdev 상세 설명](https://python.flowdas.com/library/statistics.html)
    
    ```python
    import statistics
    values = [100, 75, 85, 90, 65, 95]
    statistics.pstdev(values) 
    # 모집단의 표준 편차(모집단 분산의 제곱근)를 반환하는 함수
    ```

* 함수 기본 구조
  * 선언과 호출(define & call)
    * 함수의 선언은 def 키워드를 활용함
    * 들여쓰기를 통해 실행될 코드 블록(Function body)을 작성함
      * [Docstring](https://en.wikipedia.org/wiki/Docstring)은 함수 body 앞에 선택적으로 작성 가능
        * 작성할 땐 반드시 첫 번째 문장에 문자열 ''' ''' 사용
    * 함수는 parameter 를 넘겨줄 수 있음
    * 함수는 함수명()으로 호출
      * parameter 가 있는 경우, 함수명(값1, 값2,  ... )로 호출
    * 함수는 호출되면 동작(코드 실행) 후에 리턴을 통해 결과값을 전달함
  
  ```python
  # 함수를 활용하는 코드의 구조
  
  # 1. def 
  # 2. 함수 이름 : add
  # 3. Input : a, b
  def add(a, b):
      # 4. return : 값을 반환
      return a + b
  
  def minus(a, b):
      return a - b
  
  # 호출
  print(add(5, 10))
  print(minus(10, 5))
  
  # 내장 함수 호출
  print(sum([1, 2, 3]))
  
  +++++++++++++++++++++++++++++++
  
  def foo():           # 소괄호를 쓰는 것 = 함수 호출
      return True
  def add(x, y):       # add(2, 3) <- 직접 호출
      return x + y
  
  +++++++++++++++++++++++++++++++
  
  [직접 해보기]
  
  def add(a, b):       # add: 함수 이름 짓기, Input: a, b
      return a + b     # return: 값을 반환
  
  def add(a, b):      
      return a + b
  print(add(5, 10))    # 위와 같이 정의한 다음, 5+10 결과를 얻고 싶을때
  
  def minus(a, b):      # minus: 함수 이름 짓기, Input: a, b
      return a - b
  print(minus(10, 5))   # 호출
  
  print(sum([1, 2, 3]))   # 내장함수 호출
  
  +++++++++++++++++++++++++++++++
  
  [예시]
  
  num1 = 0
  num2 = 1
  
  def func1(a, b):                      # ③ func1 이 뭔지 확인
      return a + b
  
  def func2(a, b):                      # ④ func2 가 뭔지 확인
      return a - b
  
  def func3(a, b):                       # ② func3 이 뭔지 확인
      return func1(a, 5) + func2(5, b)
  
  result = func3(num1, num2)             # ① 호출
  print(result)                          # 결과값 5 + 4 = 9
  ```
  
  

---



## 2. 함수의 결과값(Output)

* return

  * 함수는 반드시 값을 하나만 return
  * 명시적인 return이 없는 경우에도 None을 반환
    * 값이 없으면 None

  * 함수는 return 과 동시에 실행이 종료됨
  * 아래 코드의 문제점은 뭘까?

  ```python
  def minus_and_product(x, y):
      return x - y       # 여기서 return 하며 실행이 종료되므로
  	return x * y       # 이 부분은 평 ~~~ 생 동작하지 않음!
  
  # x - y 연산만 출력되고 종료
  ```

  * 위에서 return문을 한번만 사용하면서 두 개 이상 값을 반환하고 싶다면?
    * 튜플 반환을 이용하자!

  ```python
  def minus_and_product(x, y):
      return x - y, x * y
  
  minus_and_product(4, 5)
  
  # (-1, 20)
  ```



* return vs. print
  * return은 함수 안에서 값을 반환하기 위해 사용되는 키워드
  * print는 출력을 위해 사용되는 함수

```python
def foo():
    return 1, 2

result = foo()
print(result, type(result))   # 이렇게 프린트해보면 하나로 묶은 튜플만
                              # 반환된 것을 확인할 수 있음

+++++++++++++++++++++++++++++++
    
def no():
    a = 1
    
result = no()
print(result, type(result))   # 이렇게 프린트해보면 
                              # <class 'Nonetype'>
    						  # 즉 return 없이 print문만 사용하면 'Nonetype'
    
+++++++++++++++++++++++++++++++

# 초반에 많이 하는 실수
# print() 함수는 출력이라는 '행위'만 하기 때문에
# return 값은 없다! (=None)

a = print('hi')
print(a)             
= 이런식으로 코드를 짜면 안됨
```



---



## 3. 함수의 입력(Input)

* parameter vs. argument
  * parameter : 함수를 실행할 때, 함수 내부에서 사용되는 식별자
  * argument : 함수를 호출할 때, 넣어주는 값

```python
def function(ham):  # parameter: ham
    return ham

function('spam')    # argument: 'spam'
```



* argument 
  * argument 란?
    * 함수 호출 시 함수의 parameter 를 통해 전달되는 값
    * argument 는 소괄호 안에 할당 func_name(argument)
      * 필수 argument : 반드시 전달되어야 하는 argument 
      * 선택 argument : 값을 전달하지 않아도 되는 경우는 기본 값이 전달




* positional arguments

  * 위치로 파악하기(기본)
  * 기본적으로 함수 호출 시 argument 는 위치에 따라 함수 내에 전달됨

  ```python
  def add(x, y):     add(2, 3)
      return x + y
  ```



* keyword arguments

  * 직접 변수의 이름으로 특정 argument를 전달할 수 있음
  * keyword argument 다음에 positional argument 를 활용할 수 없음

  ```python
  def add(x, y):        add(x=2, y=5)
      return x + y      add(2, y=5)
  
  +++++++++++++++++++++++++++++++
  
  print('hi', 'hello', sep='-')
  # hi-hello 도출
  # 이때, sep= 가 keyword argument !
  ```



* Default Argument Values

기본값을 지정하여 함수 호출 시 argument 값을 설정하지 않도록 함

```python
def add(x, y=0):         add(2)
	return x + y

+++++++++++++++++++++++++++++++

print('hi', 'hello')
# hi hello 도출
# print() 에 설정된 sep= 의 기본값(Default)이 스페이스 한 칸 이므로 !
```



* 정해지지 않은 개수의 arguments

  * 여러 개의 positional argument 를 하나의 필수 parameter 로 받아서 사용
    * 몇 개의 positional argument 를 받을지 모르는 함수를 정의할 때 유용
  * argument 들은 튜플로 묶여 처리되며, parameter에 *를 붙여 표현

  ```python
  def add(*args):            add(2)
      for arg in args:       add(2, 3, 4, 5)
          print(arg)
  
  +++++++++++++++++++++++++++++++
  
  # 정해지지 않은 갯수의 인자
  
  def my_add(*numbers):
      # 내부적으로 numbers가 tuple
      return numbers
  
  result = my_add(1, 2, 3)
  print(result, type(result))
  # (1, 2, 3) <class 'tuple'>
  # result 는 내부적으로 tuple 이라고 출력!
  ```

  * 함수가 임의의 개수 argument 를 묶어 keyword argument로 호출될 수 있도록 지정

  * argument 들은 딕셔너리로 묶여 처리되며, parameter 에 ** 를 붙여 표현

  ```python
  def family(**kwargs):
      for key, value in kwargs:
          print(key, ":", value)
  
  family(father='John', mother='Jane', me='John Jr.')
  
  +++++++++++++++++++++++++++++++
  
  def my_func(**kwargs):
      return kwargs
  
  result = my_func(name='홍길동', age='100', gender='M')
  print(result, type(result))
  
  # {'name': '홍길동', 'age': '100', 'gender': 'M'}
  # <class 'dict'>
  # result 는 키-값이 묶여있는 형태기에 내부적으로 dict 이라고 출력!
  ```

  

---



## 4. 함수의 범위(Scope)

* 함수는 코드 내부에 local scope를 생성하며, 그 외의 공간인 global scope 로 구분

* score

  * global scope: 코드 어디에서든 참조할 수 있는 공간
  * local scope: 함수가 만든 scope. 함수 내부에서만 참조 가능

* variable

  * global variable: global scope에 정의된 변수
  * local variable: local scope에 정의된 변수

  ```python
  def foo():
      a = 1
      
  foo()
  print(a)
  
  # 오류가 난다!
  # a는 코드 내부 local scope 에서만 정의되고
  # 그 외 공간인 global scope 에서 정의되지 않았기 때문
  # 들여쓰기 / 내어쓰기의 중요성
  ```

  

* 객체 수명주기

  * 객체는 각자의 생명주기(lifecycle)가 존재

    * (B) built-in scope
      * print, sum, len ... 파이썬이 처음부터 만들어둔 스코프
      * 파이썬이 실행된 이후부터 영원히 유지


    * (G) global scope
      *  a=3 처럼 사용자가 직접 지정
      * 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
    * (L) local scope
      * def 로 함수를 만들어서, 그 안에서 유지되는 스코프
      * 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지

  ```python
  def func():
      a = 20
      print('local', a)
      
  func()
  print('global', a)
  
  # local 20 <<<<< 이 부분 한 줄만 출력되고 그 아래 코드는 에러!
  # a는 Local scope에서만 존재하기 때문에
  # NameError: name 'a' is not defined 라고 에러 발생
  ```

  

* 이름 검색 규칙(Name Resolution)

  * 파이썬에서 사용되는 이름(식별자)들은 이름공간(namespace)에 저장되어 있음
  * LEGB Rule: 파이썬은 L -> E -> G -> B 순서로 읽음
    * Local scope: 함수
    * Enclosed scope: 특정 함수의 상위 함수
    * Global scope: 함수 밖의 변수, Import 모듈
    * Built-in scope: 파이썬 안에 내장되어 있는 함수 또는 속성

  * 즉 함수 내에서는 바깥 스코프의 변수에 접근 가능하나 수정은 할 수 없음

  ```python
  print(sum)
  print(sum(range(2)))
  sum = 5
  print(sum)
  print(sum(range(2)))
  
  # <built-in function sum>
  # 1
  # 5
  # ----------------------------
  # Type Error 발생!
  # sum = 5 지정해준 코드까지만 정상 작동하고
  # 나머지는 에러 발생 (이유는 하단 참조)
  
  +++++++++++++++++++++++++++++++
  
  sum = 5
  print(sum([1, 2, 3]))
  # 빌트인 스코프에 sum 함수가 있는데
  # 글로벌 스코프에 sum 이라는 이름의 변수를 새로 만들었음
  # 파이썬은 L -> E -> G -> B 순서로 읽으니까 결국 오류가 난다!
  *E는 생략하고 나중에 설명!
  
  +++++++++++++++++++++++++++++++
  
  name = '홍길동'                   # 이걸 쓰고 싶다면
  
  def add(a, b, c, name):          # 이렇게 넣거나
      return
  
  def add(a, b, c):
      name = '홍길동'               # 이렇게 넣자
      return 
  ```



---



## 5. 함수 응용

* map(function, iterable)
  * 순회 가능한 데이터구조(iterable)의 모든 요소에 함수(function) 적용하고, 
  
    그 결과를 map object로 반환
  
  ```python
  numbers = ['1', '2', '3']
  # 위 안에 있는 모든 것을 숫자로 바꿔서 쓰고 싶다면?
  
  n = int(numbers)
  # 이러면 오류가 남
  # 형 변환할 때, 리스트를 숫자로 바꾸는 것은 불가능!
  # 다만, 숫자 형태의 문자를 변환하는 것은 가능!
  
  a = int(numbers[0])
  b = int(numbers[1])
  c = int(numbers[2])
  new_numbers = [a, b, c]
  # 이런 식으로 하나하나 지정하면, 1(int), 2(int), 3(int)이 저장됨
  # 그러나 그 개수가 100개, 1000개라면..?
  
  new_numbers = []
  for number in numbers:
      new_numbers.append(int(numbers))
  print(new_numbers)
  # 반복문 활용하는 방법
  # int 함수를 '1', '2', '3'에 각각 적용하고 싶은게 사용자의 의도
  
  # 위의 과정을 쉽게 만들어 주는 것이 map !
  numbers = ['1', '2', '3']
  new_numbers2 = map(int, numbers)
  print(new_numbers2)       # 이렇게 보면 map 객체로 저장되어 있다고 뜸
  print(list(new_numbers2)) # map 객체를 list 로 형 변환해서 보기
  print(new_numbers2, type(new_numbers2)) # type map 이라고 뜸
  # 반드시 list 로 바꿔야 하는 것은 아니에요 ~
  
  +++++++++++++++++++++++++++++++
  
  map 의 활용 방식
  사용자에게 input 을 받았을 때 국룰임
  
  [예제]
  직사각형의 넓이를 구하시오
  직사각형의 세로는 n, 가로는 m
  input 예시: 10, 20
  
  n, m = map(int, input().split())
  print(n*m)
  # 위 코드에 대한 해설은 하단 첨부 이미지 참조
  ```

![py_function](py_function.assets/py_function.png)



* map 응용

  ```python
  # 각 요소에 10씩 더해주는 함수를 선언했을 때,
  
  def plus10(n):
      return n + 10
  
  numbers = [10, 20, 30]
  new_numbers = list(map(plus10, numbers))
  print(new_numbers)
  
  # [20, 30, 40] 출력
  ```

  
