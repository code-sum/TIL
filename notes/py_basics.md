# ✅Python 기초

> 1. 파이썬 개발 환경(Python Environment)
>2. 기초 문법
> 3. 파이썬 기본 자료형(Python Datatype)
> 4. 컨테이너(Container)
> 
> [변수 이름] =  [타입 값]으로 도식화할 때,
>[변수 이름] 은 2. 기초 문법 파트에서 설명하고 있으며 
> [타입 값] 은 3. 파이썬 기본 자료형, 4. 컨테이너 파트에서 설명합니다.



## 1. 파이썬 개발 환경(Python Environment)

* 컴퓨터 프로그래밍 언어
  * 컴퓨터(Computer): ① Calculation + ② Remember
  * 프로그래밍(programming): 명령어의 모음(집합)
  * 언어: 자신의 생각을 전달하기 위해 사용하는 체계
    문법적으로 맞는 말의 집합
  * 프로그래밍 언어란? 컴퓨터에게 명령하는 말
                                      컴퓨터에게 명령하기 위한 약속들을 배운다!

  
  
* 프로그래밍 언어를 공부할 때 생각해볼 부분
  * 선언적 지식(declarative knowledge): 사실에 대한 내용
    *이를 공부하는 것은 매우 쉽다
  * 명령적 지식(imperative knowledge): How-to, 어떻게 할 것인가?
    ※ 코드의 함정에 빠지지 말고, 
        내가 지금 어떤 명령을 하고 있는지 생각하면서 코딩하자

  
  
* 파이썬 개발 환경(Python Environment)

  * 파이썬(Python)이란?

    * 다른 언어보다 문법이 간단하고 엄격하지 않아서 배우기 쉬움
      ex) 변수에 별도의 타입 지정이 필요 없음
    * 문법 표현이 매우 간결하여 짧은 시간 내에 마스터 가능
      ex) 문장을 구분할 때 중괄호({,}) 대신 들여쓰기를 사용
    * Expressive Language
      * 같은 작업에 대해, C나 Java보다 더 간결하게 작성 가능
  
    ```java
    public class HelloPython {
        public static void main(String[] args) {
            System.out.println("Hello Python!");
    	    }
    	}
    ```
  
    ```python
    print('Hello Python!')
    ```
  
    * 크로스 플랫폼 언어
      ex) Windows, macOS, Linux, Unix 등 다양한 OS에서 실행가능
  
    
  
  * 파이썬의 특징
  
    * 인터프리터(Interpreter) 언어
      * 소스코드를 기계어로 변환하는 컴파일 과정 없이 바로 실행 가능
      * 코드를 대화하듯 한 줄 입력하고 실행한 후, 바로 확인할 수 있음
  
    ```python
    >>> 2+2     # 사용자가 입력(input)
    4           # 컴퓨터가 대답(output)
    
    # 위와 같이 컴파일(소스코드를 기계어로 변환)과정 없이 바로 실행 가능
    # 대화하듯 코드를 한 줄 입력하고 실행한 후, 바로 확인 가능
    ```
  
    * 객체 지향 프로그래밍(Object Oriented Programming)
  
      * 파이썬은 객체지향 언어이며, 모든 것이 객체로 구현되어 있음
  
      * 객체(object): 숫자, 문자, 클래스 등 값을 가지고 있는 모든 것
  
        물건, 대상, ~것(쉽게 이해하기), '파이썬에 있는 어떤 것들'
  
        
  
  * 파이썬 개발환경
  
    * 파이썬 기본 인터프리터: IDLE
  
      * IDLE(Intergrated Development and Learning Environment)
  
        (1) 내장 프로그램으로 파이썬 설치 시 기본적으로 설치
  
        (2) (1)로 인해 인터프리터가 대화형 모드로 동작함
  
        (3) 여러 줄의 코드가 작성되는 경우 프롬프트(...)가 사용됨
  
        (4) 프롬프트(>>>)에 코드를 작성하면 해당 코드가 실행됨
  
      *  Python이 설치된 환경에서는 기본적으로 활용 가능하나 디버깅 및 코드 편집, 반복 실행이 어려움
  
  
  
  
  * Python 스크립트 실행
  
    * IDE(예시: Pycharm), Text editor(예시: Visual Studio Code)등에서 작성한 파이썬 스크립트 파일을 직접 실행
  
    ```python
    print('hello world')
    ```





---



## 2. 기초 문법

* 코드 스타일 가이드
  * 코드를 '어떻게 작성할지'에 대한 가이드라인
  * 파이썬에서 제안하는 스타일 가이드
  
    * PEP8 (https://peps.python.org/pep-0008/)
  * 기업, 오픈소스 등에서 사용되는 스타일 가이드
  
    * Google Style guide (https://google.github.io/styleguide/pyguide.html)
  
     
  
* 들여쓰기(Identation)
  * Space Sensitive
    
    * 문장을 구분할 때, 들여쓰기(indentation)를 사용
    
    * VS Code 에서 tab 하면 space 4회로 알아서 바꿔줌
    * [주의] 한 코드 안에선 반드시 한 종류의 들여쓰기 사용!
      * Tab 으로 들여쓰기 시작했으면 계속 Tab 으로
      * PEP8에서 권장하는 원칙은 공백(빈칸, space)이긴 함



* 변수(Variable)
  * 변수란?
    * 컴퓨터 메모리 어딘가에 저장된 객체를 참조하기 위해 사용되는 이름
    * 동일 변수에 다른 객체를 언제든 할당할 수 있기 때문에(=참조하는 객체가 바뀔 수 있기 때문에) '변수' 라고 불림
    * 변수는 할당 연산자(=)를 통해 값을 할당(assignment)
    * ⭐ type() :변수에 할당된 값의 타입
    * id() :변수에 할당된 값의 고유한 아이덴티티(identity) 값, 메모리주소
    
  * 변수 할당

    * 같은 값을 동시에 할당할 수 있음
    * 다른 값을 동시에 할당할 수 있음(multiple assignment)

    ```python
    1) 같은 값 동시에 할당하기
    x = y = 1004
    print(x, y)
    # 1004
    
    2) 다른 값 동시에 할당하기
    x, y = 1, 2
    print(x, y)
    # 1, 2
    
    +++++++++++++++++++++++++++++++
    
    에러 사례1)
    x, y = 1
    print(x, y)
    # TypeError
    
    에러 사례2)
    x, y = 1, 2, 3
    print(x, y)
    # Value Error
    ```



* 파이썬 기초 문법 응용 사례

```python
2+3
print(2+3)

위 두 줄의 명렁어를 파이썬에 입력하면 모두 5를 출력하지만
Terminal 에서 $ python 파일명 을 입력했을 때
5가 Terminal 에 5가 출력되는 것은 print(2+3) 뿐이다.

+++++++++++++++++++++++++++++++

print(2+3)
print(2+3)
print(2+3)
print(2+3)
print(2+3)

이렇게 5회 연속으로 명령어를 입력해 두면 
$ python 파일명 입력해서 Terminal 에서 실행할 때
5가 5회 연속으로 출력된다.

# hello 라는 이름의 변수에
# 'Happy Coding' 값을 할당
hello = 'Happy Coding'
print(hello)
print(hello)
print(hello)
print(hello)
print(hello)
이때도 $ python 파일명 입력해서 Terminal 에서 실행하면
Happy Coding 이 5회 연속으로 출력된다.

a = 5
b = 3
print(a + b)
이때 $ python 파일명 입력해서 Terminal 에서 실행하면
8이 출력된다.

+++++++++++++++++++++++++++++++

# [기본원칙] 코드는 위에서부터 아래로 실행된다.
위와 같이 a = 5 라고 지정했다가,
a = 'hello'
print(a)
이때 $ python 파일명 입력해서 Terminal 에서 실행하면
hello 가 출력된다.

# [기본원칙2] 코드는 오른쪽에서 왼쪽으로 적용된다.
a = 5
a = a + 1
print(a)
# 6
```



* 실습 문제: x = 10, y = 20 일 때, 각각 값을 바꿔서 저장하는 코드를 작성하시오

  ```python
  x = 10
  y = 20
  
  # 접근방법: 임시적인 변수(tmp)가 필요하다
  tmp = x
  x = y
  y = tmp
  print(x, y)
  # 파이썬 튜터로 소스 코드 돌리고 결과 확인!
  
  # 다른 풀이: pythonic!
  y, x = x, y
  print(x, y)
  ```



* 식별자(Identifiers)

  * 파이썬 객체(변수, 함수, 모듈, 클래스 등)를 식별하는데 사용하는 이름(name)

  * 규칙
    * 식별자의 이름은 영문 알파벳, 언더스코어(_), 숫자로 구성
    * 첫 글자에 숫자가 올 수 없음
    * 길이 제한이 없고, 대소문자를 구별
    * 몇 가지 키워드는 예약어(reserved words)로 사용할 수 없음
    
      ```python
      # 식별자로 사용할 수 없는 단어들 확인해보기
      import keyword
      print(keyword.kwlist)
      ```
    
    * 내장함수, 모듈 등의 이름도 식별자로 사용할 수 없음
    
      ```python
      print(5)
      print = 'hi'
      print(5)
      # 위의 경우, 내장함수 print 의 기능은 사라지고
      # 식별자(변수명)가 print인 문자열 'hi'로 활용
      # TypeError 발생
      ```
    
      

* 사용자 입력

  * input([prompt])

    * 사용자로부터 값을 즉시 입력 받을 수 있는 내장함수
    * 괄호 부분에 문자열을 넣으면 입력 시, 해당 문자열을 출력할 수 있음
    * 반환값은 항상 문자열(str) 형태로 반환
    
    ```python
    name = input('이름을 입력해주세요 : ')
    print(name)
    # 이름을 입력해주세요 : 파이썬
    type(name)
    # str
    ```



* 주석(Comment)

  * 코드에 대한 설명
    * 중요한 점이나 다시 확인하여야 하는 부분을 표시
    * 컴퓨터는 주석을 인식하지 않음! 사용자만을 위한 것
  * 가장 중요한 습관
    * 개발자에게 주석을 작성하는 습관은 매우 중요
    * 쉬운 이해와 코드의 분석 및 수정이 용이
      * 주석은 코드 실행에 영향을 미치지 않음
      * 프로그램 속도를 느리게 하지 않으며, 용량도 늘리지 않음

  * 한 줄 주석
    
    * 주석으로 처리될 내용 앞에 '#' 을 입력
    
      * 여러 줄을 드래그하고 `Ctrl + /` 누르면 드래그 영역 모두 주석 처리
      * 한 줄을 온전히 사용할 수도 있고, 그 줄 코드 뒷부분에 작성할 수 있음
    
      ```python
      # 주석(Comment)입니다.
      
      # print('hello')
      print('world') # 주석
      ```
    





---



## 3. 파이썬 기본 자료형(Python Datatype)

* 자료형 분류

  * 불린형(Boolean Type)
  * 수치형(Numeric Type)
    * int (정수, integer)
    * float (부동소수점, 실수, floating point number)
    * complex (복소수, complex number)
  * 문자열(String Type)
  * None

  


* None

  * 파이썬에서는 값이 없다는 것을 표현하기 위해 None 타입이 존재
  * 일반적으로 반환 값이 없는 함수에서 사용하기도 함

  ```python
  print(type(None))
  # <class 'NoneType'>
  a = None
  print(a)
  # None
  ```

  

* 불린형(Boolean Type)

  * True / False 값을 가진 것
  * 비교 / 논리 연산을 수행함에 있어서 활용됨
  * 다음은 모두 False로 반환
    * 0, 0.0, (), {}, [], '', None

    * bool() 함수: 특정 데이터가 True 인지 False 인지 검증
      * bool(0), bool([1, 2, 3]) 이런 식으로 검증

  

* 연산자(Operator)

  * 논리 연산자(Logical Operator)

    * 논리식을 판단하여 참(True)과 거짓(False)을 반환

      | 연산자  | 내용                           |
      | ------- | ------------------------------ |
      | A and B | A와 B 모두 True시, True        |
      | A or B  | A 와 B 모두 False시, False     |
      | Not     | True를 False로, False를 True로 |

      
      
    * and : 모두 참인 경우 참, 그렇지 않으면 거짓
    
      | 논리연산자 and  | 내용  |
      | --------------- | ----- |
      | True and True   | True  |
      | True and False  | False |
      | False and True  | False |
      | False and False | False |
    
      
    
    * or : 둘 중 하나만 참이라도 참, 그렇지 않으면 거짓
    
      | 논리연산자 or  | 내용  |
      | -------------- | ----- |
      | True or True   | True  |
      | True or False  | True  |
      | False or True  | True  |
      | False or False | False |
    
      
    
    * not : 참-거짓 반대의 결과
    
      | 논리연산자 not | 내용  |
      | -------------- | ----- |
      | not True       | False |
      | not False      | True  |
    
      
    
    * 연산자 예제
    
      ```python
      num = 100
      num >= 100 and num % 3 == 1
      # True
      ```
    
      


​     

  * 수치형(Numeric Type)

    * 정수(int)
    
         * 파이썬에서 모든 정수의 타입은 int
         * 수가 아무리 커져도 오버플로우가 발생하지 않음
    
              * 오버플로우: 데이터 타입별 가용 메모리 크기를 넘는 상황
    
              
    
    * 실수(float) 
    
         * 정수가 아닌 모든 실수는 float
    
         * 알고리즘 처리할 땐 안쓰지만, 확률 처리할 땐 실수를 씀
    
         * 부동소수점
    
           * 실수를 컴퓨터가 표현하는 방법: 2진수 비트
           * floating point rounding error 발생하니 실수 연산할 땐 조심
    
           
    
    * 산술 연산자(Arithmetic Operator)
    
         * 기본적인 사칙연산 및 수식 계산
    
           |      | 연산자 | 내용     |
           | ---- | ------ | -------- |
           |      | +      | 덧셈     |
           |      | -      | 뺄셈     |
           |      | *      | 곱셈     |
           | ⭐    | %      | 나머지   |
           | ⭐    | /      | 나눗셈   |
           | ⭐    | //     | 몫       |
           | ⭐    | **     | 거듭제곱 |
    
           ※ 나머지 연산 활용 >> 짝수인지, 홀수인지 확인할 때
    
           
    
    * 복합 연산자
    
      * 연산과 할당이 함께 이뤄짐
    
        | 연산자  | 내용       |
        | ------- | ---------- |
        | a += b  | a = a + b  |
        | a -= b  | a = a - b  |
        | a *= b  | a = a * b  |
        | a /= b  | a = a / b  |
        | a //= b | a = a // b |
        | a %= b  | a = a % b  |
        | a **= b | a = a ** b |
    
        
    
    * 비교 연산자(Comparison Operator)
    
      * 값을 비교하며, True / False 값을 리턴
    
        | 연산자 | 내용     |
        | ------ | -------- |
        | <      | 미만     |
        | <=     | 이하     |
        | >      | 초과     |
        | >=     | 이상     |
        | ==     | 같음     |
        | !=     | 같지않음 |
    





  * 문자열(Stiring Type)

    * 모든 문자는 str 타입

    * 따옴표가 중요하다

    * 문자열은 작은 따옴표(')나 큰 따옴표(")를 활용하여 표기

      * 둘 중에 하나를 선택해서, 일관성 유지하며 쓰기만 하면 됨

    * 중첩따옴표, 삼중따옴표

      ```python
      print("문자열 안에 '작은 따옴표' 쓸 때 큰 따옴표로 묶기.")
      print('문자열 안에 "큰 따옴표" 쓸 때 작은 따옴표로 묶기.')
      
      print('''문자열 안에 '작은 따옴표'나
      "큰 따옴표"를 사용할 수 있고
      여러 줄을 사용할 때도 편리하다.''')
      ```

      

  * 문자열 연산자

    * 인덱싱

      * 인덱스를 통해 특정 값에 접근할 수 있음

      * s[1] => 'b'

        | "     | a    | b    | c    | d    | e    | "    |
        | ----- | ---- | ---- | ---- | ---- | ---- | ---- |
        | index | 0    | 1    | 2    | 3    | 4    |      |

        

    * 문자열 슬라이싱(Slicing) 예제
      
      * s[2:5:2] => 'ce'
      * s[5:2:-1] => 'fed' 
      * s[:3] 처음부터 3미만 => 'abc'
      * s[5:] 5부터 마지막까지 => 'fghi'
      * s[::] 처음부터 끝까지 1씩 (=그대로) => 'abcdefghi' => s[0:len(s):1]과 동일
      * s[::-1] 처음부터 끝까지 -1씩 (=뒤집기) => 'ihgfedcba' => s[-1:-(len(s)+1):-1]과 동일
      
      | "     | a    | b    | c    | d    | e    | f    | g    | h    | i    | "    |
      | ----- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
      | index | 0    | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    |      |
      | index | -9   | -8   | -7   | -6   | -5   | -4   | -3   | -2   | -1   |      |
      
      
      
    * 기타 문자열 연산자

      * 결합(Concatenation)

        ```python
        'Hello, ' + 'python!'
        # 'Hello, python!'
        ```

      * 반복(Repetition)

        ```python
        'Hi!' * 3
        # 'Hi!Hi!Hi!'
        ```

      * 포함(Membership)

        ```python
        'a' in 'apple'
        # True
        
        'app' in 'apple'
        # True
        
        'b' in 'apple'
        # False
        ```

      

    * Escape sequence

      * 문자열 내에서 특정 문자나 조작을 위해 역슬래시(\\\)를 활용하여 구분

        | 예약문자 | 내용(의미)        |
        | -------- | ----------------- |
        | \n       | 줄 바꿈           |
        | \t       | 탭                |
        | \r       | 캐리지리턴        |
        | \0       | 널(Null)          |
        | \\\      | `\`               |
        | \\'      | 단일인용부호(`'`) |
        | \\"      | 이중인용부호(`"`) |

        ```python
        print('철수 \'안녕\'')
        # 철수 '안녕'
        print('이 다음은 엔터. \n그리고 탭\t탭')
        # 이 다음은 엔터.
        # 그리고 탭    탭
        ```

        

    * String Interpolation

      * 변수를 활용하여 문자열 만드는 법

        * %-formatting

          ```python
          name = 'Kim'
          score = 4.5
          
          print('Hello, %s' % name)
          print('내 성적은 %d' % score)
          print('내 성적은 %f' % score)
          
          # Hello, Kim
          # 내 성적은 4
          # 내 성적은 4.500000
          ```

        * f-string

          ```python
          name = 'Kim'
          score = 4.5
          print(f'Hello, {name}! 성적은 {score}')
          # Hello, Kim! 성적은 4.5
          
          pi = 3.141592
          print(f'원주율은 {pi:.3}. 반지름이 2일때 원의 넓이는 {pi*2*2}')
          # 원주율을 3.14. 반지름이 2일때 원의 넓이는 12.566368
          ```

          

    * 문자열 특징

      * Immutable: 변경 불가능함

        ```python
        a = 'my srting?'
        a[-1] = '!'
        
        # TypeError 발생
        ```

      * Iterable: 반복 가능함

        ```python
        a = '123'
        for char in a:
            print(char)
        ```

        

    💡문자열 파트 추가 학습

    ```python
    # 문자열의 길이 구하기
    fruit = 'apple'
    print(len(fruit))
    이때 $ python 파일명 입력해서 Terminal 에서 실행하면
    길이인 5가 출력
          
    # 접근/인덱싱
    # 컴퓨터에서는 숫자를 0부터 셈
    print(fruit[1]) # fruit 변수는 값이 'apple'
    따라서 $ python 파일명 입력해서 Terminal 에서 실행하면
    p 가 출력
          
    # 슬라이싱
    fruit = 'abcde'
    print(fruit[1:3])
    이때 $ python 파일명 입력해서 Terminal 에서 실행하면
    bc 가 출력 (인덱싱 1이상, 3미만)
    # a b c d e
    # 0 1 2 3 4
          
    # 마지막 값은? : 길이 -1
    # 파이썬은 음의 인덱스도 가지고 있다
    print(fruit[-1])   # 이렇게만 입력해도 마지막 값이 출력됨!
    ```






* 형 변환(Typecasting)
  * 파이썬에서 데이터 형태는 서로 변환할 수 있음
    * 암시적 형 변환(Implicit)
      * 사용자가 의도하지 않고, 파이썬 내부적으로 자료형을 변환
    * 명시적 형 변환(Explicit)
      * 형식만 일치한다면 사용자가 특정 함수를 활용해 자료형 직접 변환
    
    ```python
    1) 암시적 형 변환(Implicit Typecasting)
       - bool
       - Numeric type (int, float, complex)
       ex)  True + 3    # 4
            3 + 5.0     # 8.0
            3 + 4j + 5  # (8+4j)
            
    2) 명시적 형 변환(Explicit Typecasting)
       *표시는 형식에 맞는 문자열만 가능
       - int: str*, float => int
       - float: str*, int => float
       - str: int, float, list, tuple, dict => str
       ex) '3' + 4       # TypeError: 문자열은 암시적 타입 변환이 안됨
           int('3') + 4  # 7 : 따라서 이와 같이 명시적 타입 변환이 필요
           int('3.5') + 5  # ValueError: 정수 형식 아니면 타입 변환 불가
           float('3.5') + 5  # 8.5
            
    ++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
    # 숫자와 문자는 더할 수 없어서, 따옴표 찍어서 숫자를 직접 문자열로 변환
    score = 100
    print('내 점수는 ' + str(score) + ' 이야.')
    ```





---



## 4. 컨테이너(Container)

* 컨테이너 정의
  * 컨테이너란? 여러 개를 담는 것(객체). 서로 다른 자료형을 저장할 수 있음
    * 예시: List, tuple
* 컨테이너 분류
  * 순서가 있는 데이터(Ordered) vs. 순서가 없는 데이터(Unordered)
    * 순서가 있으면 인덱스로 접근
  * 순서가 있다 != 정렬되어 있다.
  * 시퀀스
    * 문자열(immutable): 문자들의 나열
    * 리스트(mutable): 변경 가능한 값들의 나열
    * 튜플(immutable): 변경 불가능한 값들의 나열
    * 레인지(immtuble): 숫자의 나열
  * 컬렉션/비시퀀스
    * 세트(mutable): 유일한 값들의 모음
    * 딕셔너리(mutable): 키-값들의 모음



* 시퀀스형 컨테이너(Sequence Container)

  * 시퀀스형 주요 공통 연산자

    | 연산             | 결과                                                         |
    | ---------------- | ------------------------------------------------------------ |
    | s[i]             | s의 i번째 항목, 0에서 시작                                   |
    | s[i:j]           | s의 i에서 j까지의 슬라이스                                   |
    | s[i:j:k]         | s의 i에서 j까지 스텝k의 슬라이스                             |
    | s + t            | s와 t의 이어 붙이기                                          |
    | s * n 또는 n * s | s를 그 자신에 n번 더하는 것                                  |
    | x in s           | s의 항목 중 하나가 x와 같으면 True, 그렇지 않으면 False (s 안에 x 가 있니? 하고 물어보는 것) |
    | x not in s       | s의 항목 중 하나가 x와 같으면 False, 그렇지 않으면 True (s 안에 x 가 없니? 하고 물어보는 것) |
    | len(s)           | s의 길이                                                     |
    | min(s)           | s의 가장 작은 항목                                           |
    | max(s)           | s의 가장 큰 항목                                             |


​    

  * 리스트(List)

    * 리스트 정의

      * 변경 가능한 값들의 나열된 자료형
      * 순서를 가지며, 서로 다른 타입의 요소를 가질 수 있음
      * 변경 가능하며(mutable), 반복 가능함(iterable)
      * 리스트 값 추가/삭제: .append(), .pop()
      * 항상 대괄호 형태로 정의하며, 요소는 콤마로 구분
        * [0, 1, 2, 3, 4, 5]

    * 생성과 접근

      * 리스트는 대괄호([]) 혹은 list() 를 통해 생성
      * 순서가 있는 시퀀스로, 인덱스를 통해 접근 가능
        * 값에 대한 접근은 list[i]

      |                | 객체1 | 객체2 | 객체3 | 객체4 | 객체5 | 객체6 | 객체7 |
      | -------------- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
      | Positive index | 0     | 1     | 2     | 3     | 4     | 5     | 6     |
      | Negative index | -7    | -6    | -5    | -4    | -3    | -2    | -1    |

      ```python
      1) 리스트 생성
      # 생성
      my_list = []
      another_list = list()
      type(my_list)       # <class 'list'>
      type(another_lisr)  # <class 'list'>
      
      2) 리스트 접근과 변경
      # 값 접근
      a = [1, 2, 3]
      print(a[0])   # 1
      
      # 값 변경
      a[0] = '1'
      print(a)   # ['1', 2, 3]
      
      3) 리스트 값 추가/삭제
         값 추가는 .append()를 활용하여 추가하고자 하는 값을 전달
         ex) even_numbers = [2, 4, 6, 8]
             even_numbers.append(10)
             even_numbers   # => [2, 4, 6, 8, 10]
              
         값 삭제는 .pop()을 활용하여 삭제하고자 하는 인덱스를 전달
         ex) even_numbers = [2, 4, 6, 8]
             even_numbers.pop(0)
             even_numbers   # => [4, 6, 8]
          
      ++++++++++++++++++++++++++++++++++++++++++++++++++++++
      
      [예제]
      
      boxes = ['apple', 'banana']
      len(boxes)   # 2
      boxes[1]     # 'banana'
      boxes[1][0]  #'b'
      ```

      

  * 튜플(tuple)
    * 튜플 정의
      * 불변한 값들의 나열
      * 순서를 가지며, 서로 다른 타입의 요소를 가질 수 있음
      * 변경 불가능하며(immutable), 반복 가능함(iterable)
      * 항상 소괄호 형태로 정의하며, 요소는 콤마로 구분
        * (0, 1, 3)
      
    
    * 생성과 접근
    
      * 소괄호(()) 혹은 tuple()을 통해 생성
      * 인덱스로 특정 값에 접근한다는 점에서 리스트와 동일
      * 그러나 리스트와 비교할 때, 변경 불가능하다는 특징이 있음
        * 값 변경은 불가능하여 추가/삭제도 불가능함
      * 직접 만들어서 쓰는 일은 잘 없음 
    
      ```python
      ※ 튜플 값 접근과 변경
      # 값 접근
      a = (1, 2, 3, 1)
      a[1]
      
      # 값 변경 => 불가능
      a[1] = '3'  # TypeError 발생
      ```
    
      

  * 레인지(Range)
    * 파이썬만의 특징
    * 숫자의 순서(sequence)를 독특하게 나타냄(숫자의 통이라고 이해하자)
      * 기본형: range(n)
        * 0부터 n-1까지 숫자의 시퀀스
      * 범위 지정: range(n, m)
        * n부터 m-1까지 숫자의 시퀀스
      * 범위 및 스텝 지정: range(n, m, s)
        * n부터 m-1까지 s만큼 증가시키며 숫자의 시퀀스
    * 변경 불가능하며(immutable), 반복 가능함(iterable)
    
    ```python
    range(4)
    # range(0, 4)
    
    list(range(4))    # 담겨있는 숫자를 확인하기 위해 리스트로 형 변환
    # [0, 1, 2, 3]    # 실제 활용시에는 형 변환 필요 없음
    
    type(range(4))
    # <class 'range'>
    
    ++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
    [예제]
    
    # 0부터 특정 숫자까지
    list(range(3))
    # [0, 1, 2]
    
    # 숫자의 범위
    list(range(1, 5))
    # [1, 2, 3, 4]
    
    # step 활용
    list(range(1, 5, 2))
    # [1, 3]
    
    # 역순
    list(range(6, 1, -1))
    # [6, 5, 4, 3, 2]
    
    list(range(6, 1, 1))
    # []
    ```



* 비시퀀스형 컨테이너(Associative Container): 세트&딕셔너리

  * 세트(Set)

    * 유일한 값들의 모음(collection)
    * 순서가 없고 중복된 값이 없음
      * 수학에서의 집합과 동일한 구조를 가지며, 집합 연산도 가능
    * 변경 가능하며(mutable), 반복 가능함(iterable)
      * 단, 셋은 순서가 없어 반복의 결과가 정의한 순서와 다를 수 있음

  * 세트 생성

    * 중괄호({}) 혹은 set()을 통해 생성
      * 비어있는 Set을 만들기 위해서는 set()을 반드시 활용해야 함
    * 순서가 없기 때문에 별도의 값에 접근할 수 없음

  * 세트 추가/삭제

    * 값 추가는 .add()를 활용하여 추가하고자 하는 값을 전달
    * 값 삭제는 .remove()를 활용하여 삭제하고자 하는 값을 전달

  * 세트 활용

  * **세트를 활용하면 다른 컨테이너에서 중복된 값을 쉽게 제거할 수 있음**

    * 단, 이후 순서가 무시되기 때문에 순서가 중요한 경우 사용할 수 없음

    ```python
    1) 세트 생성
    {1, 2, 3, 1, 2}
    # {1, 2, 3}          <= 중복 값 제거
    type({1, 2, 3})
    # <class 'set'>
    
    blank_set = set()
    
    {'hi', 1, 2}
    # => {1, 2, 'hi'}
    
    {1, 2, 3}[0]
    # TypeError 발생: 순서가 없어서 인덱스 접근 등 특정 값에 접근할 수 없음
    
    2) 세트 추가/삭제
    numbers = {1, 2, 3}
    numbers.add(5)
    numbers
    # => {1, 2, 3, 5}
    
    numbers.add(1)
    numbers
    # => {1, 2, 3, 5}
    
    numbers = {1, 2, 3}
    numbers.remove(1)
    numbers
    # => {2, 3}
    numbers.remove(5)
    # => 세트 내에 5가 존재하지 않으므로, 에러 발생!
    
    3) 세트 활용
    my_list = ['서울', '서울', '대전', '광주', '서울', '대전', '부산', '부산']
    len(set(my_list))
    # 4
    set(my_list)
    # {'광주', '대전', '부산', '서울'}
    
    ++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
    [추가 수업내용]
    
    # 세트
    set_a = {1, 2, 3, 1, 1}
    set_b = {'hi', 1, 2}
    print(set_a)  # {1, 2, 3}
    print(set_b)  # {1, 2, 'hi'}
    # 즉, 순서가 없다
    
    # 세트를 활용해 중복된 값 제거하기
    location = ['서울', '서울', '대구', '제주', '부산', '부산', '대구', '광주', '인천']
    print(set(locations)) :{'광주', '대구', '서울', '부산', '인천', '제주'} 
    # 중복된 값이 모두 제거된 것을 확인할 수 있음
    print(len(set(locations)))   # 6 
    ```



* 딕셔너리: 키-값(key-value) 쌍으로 이뤄진 모음(collection)

  * 키(key)
    * 불변 자료형만 가능(리스트 등은 불가능함)
  * 값(values)
    * 어떤 형태든 관계 없음
  * 키와 값은 :로 구분. 개별 요소는 ,로 구분
  * 변경 가능하며(mutable), 반복 가능함(iterable)
    * 딕셔너리를 반복하면 키가 반환됨

  * 딕셔너리 생성

    * key와 value가 쌍으로 이뤄진 자료구조
    * key는 변경 불가능한 데이터(immutable)만 활용 가능
      * string, integer, float, boolean, tuple, range
    * value는 모든 값으로 설정 가능(List, Dictionary 등)

  * 딕셔너리 키-값 추가 및 변경

    * 딕셔너리에 키와 값의 쌍을 추가할 수 있고, 이미 해당하는 키가 있다면 기존 값이 변경됨
    * 즉, 키는 하나밖에 존재할 수 없기 때문에 기존 값을 변경하는 식으로 키-값이 추가됨
    * 딕셔너리 키-값 삭제: .pop()   *키가 없으면 KeyError 발생

    ```python
    1) 딕셔너리 키 반환
    students = {'홍길동': 30, '김철수': 25}
    students['홍길동']
    # 30
    
    2) 딕셔너리 생성 안되는 경우
    dict_c = {[1, 2, 3]: 'hi'}
    # TypeError: key는 변경 불가능한 데이터만 활용되는데, 위에선 변경 가능한 리스트 들어감
    
    3) 딕셔너리 접근
    movie = {
        'title': '설국열차',
        'genres': ['SF', '액션', '드라마'],
        'open_date': '2013-08-01',
        'time': 126,
        'adult': False,
    }
    
    movie['genres']
    # ['SF', '액션', '드라마']
    
    movie['actors']
    # Traceback 에러 발생!
    
    4) 딕셔너리 키-값 추가 및 변경
    students = {'홍길동': 100, '김철수': 90}
    students['홍길동'] = 80
    # {'홍길동': 80, '김철수': 90}    <= 기존의 데이터를 즉시 변경
    students['박영희'] = 95
    # {'홍길동': 80, '김철수': 90, '박영희': 95}    <= 새로운 데이터 즉시 추가
    
    5) 딕셔너리 키-값 삭제
    students = {'홍길동': 30, '김철수': 25}
    students.pop('홍길동')
    students
    # {'김철수': 25}
    
    students = {'홍길동': 30, '김철수': 25}
    students.pop('jane')
    # jane 은 원래 없던 키기 때문에 에러 발생!
    ```

    

💡**4. 컨테이너 파트 최종 정리 및 활용**

```python
name = '동현'
name1 = '효근'
name2 = '수경'
name3 = '나영'
name4 = '다겸'
name5 = '예지'

# 리스트(값들의 나열이므로, 인덱스 즉 순서로 접근)
위의 상황에서 모든 값을 하나로 묶어서 저장할 때 활용
students = ['동현', '효근', '수경', '나영', '다겸', '예지']

# 동현에 접근해서 사용하기
print(students[0])
이때 $ python 파일명 입력해서 Terminal 에서 실행하면
'동현'이 출력됨

# 마지막 사람에 접근해서 사용하기
print(students[-1])
이때 $ python 파일명 입력해서 Terminal 에서 실행하면
'예지'가 출력됨

동현, 효근 1회차, 수경, 나영 2회차, 다겸, 예지 3회차로 저장하고 싶을 때
students_1 = ['동현', '효근']
students_2 = ['수경', '나영']
students_3 = ['다겸', '예지']
이렇게 하면 복잡하니까 아래와 같이 다시 정리

students = [['동현', '효근'], ['수경', '나영'], ['다겸', '예지']]
여기서 무슨 회차인지에 대한 정보까지 넣고 싶다면?
# 딕셔너리(=키-값의 쌍) 활용하면 됨
students = {
    '1회차' : ['동현', '효근'],
    '2회차' : ['수경', '나영'],
    '3회차' : ['다겸', '예지']
}

여기서 1회차 학생들만 따로 뽑아보고 싶다면?
print(student['1회차'])
# 딕셔너리는 키-값의 쌍이므로, 접근할 때 키로 접근
# 종합 비유: 단순한 약통이 리스트라면, 요일별 약통은 딕셔너리

# 시퀀스
numbers = [1, 100, 20, 50]
print(sum(numbers)) : 다 더하기
print(max(numbers)) : 최대값
print(min(numbers)) : 최소값
print(len(numbers)) : 길이
    
# 응용
print([1, 2]+[3]) : [1, 2, 3] 으로 출력됨

# 레인지
range(3) : 0, 1, 2 로 출력
range(1,4) : 1, 2, 3 로 출력(1이상 4미만)
numbers = range(5)
print(numbers) : 이때, range(0, 5) 로 출력
    따라서, 안에 들어가 있는 숫자들이 궁금하다면
    숫자들의 나열인 리스트를 이용해서 확인(아랫줄 코드 참조)
print(list(numbers)) : [0, 1, 2, 3, 4] 로 출력
```

