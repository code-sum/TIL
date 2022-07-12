# ✅Python 기초

> PDF 참조해서 내용을 보충할 예정입니다.
>
> 1. 파이썬 개발 환경
> 2. 기초 문법
> 3. 파이썬 기본 자료형(Python Datatype)
> 4. 컨테이너
>
> [변수 이름] =  [타입 값]으로 도식화할 때,
> [변수 이름] 은 2. 기초 문법 파트에서 설명하고 있으며 
> [타입 값] 은 3. 파이썬 기본 자료형, 4. 컨테이너 파트에서 설명합니다.



## 1. 파이썬 개발 환경

* 컴퓨터 프로그래밍 언어
  * 컴퓨터(Computer)의 정의: ①Calculation + ②Remember
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

  
  
* 파이썬 개발환경

  * 파이썬이란?

    * 배우기 정말 쉽다
      ex) 변수에 별도의 타입 지정이 필요 없음
    * 문법 표현이 매우 간결하여 짧은 시간 내에 마스터 가능
      ex) 문장을 구분할 때 중괄호({,}) 대신 띄어쓰기
    * 크로스 플랫폼 언어
      ex) Windows, macOS, Linux, Unix 등 다양한 OS에서 실행가능
    * 인터프리터 언어(Interpreter)

    ```python
    >>> 2+2     # 사용자가 입력(input)
    4           # 컴퓨터가 대답(output)
    
    # 위와 같이 컴파일(소스코드를 기계어로 변환) 과정 없이 바로 실행 가능
    # 대화하듯 코드를 한 줄 입력하고 실행한 후, 바로 확인 가능
    ```

    * 객체 지향 프로그래밍(Object Oriented Programming)
      파이썬은 객체지향 언어이며, 모든 것이 객체로 구현되어 있음
      객체(object): 숫자, 문자, 클래스 등 값을 가지고 있는 모든 것
                             물건, 대상, ~것(쉽게 이해하기), '파이썬에 있는 어떤 것들'

  * 파이썬 개발환경

    * 파이썬 기본 인터프리터: IDLE

    * Python 스크립트 실행
    
    ```python
    print('hello world')
    ```



---



## 2. 기초 문법

* 코드 스타일 가이드
  * 코드를 어떻게 작성할지에 대한 가이드라인
  * 파이썬에서 제안하는 스타일 가이드
    PEP8
  * 기업, 오픈소스 등에서 활용

* 들여쓰기(Identation)
  * Space Sensitive
    VS Code 에서 tab 하면 스페이스 4회로 알아서 바꿔줌

* 변수(Variable)
  * 변수란?
    * 컴퓨터 메모리 어딘가에 저장되어 있는 객체를 참조하기 위해 
      사용되는 이름
      ex) a = 8
    * 동일 변수에 다른 객체를 언제든 할당할 수 있기 때문에,
      즉, 참조하는 객체가 바뀔 수 있기 때문에 '변수' 라고 불림
    * 변수는 할당 연산자(=)를 통해 값을 할당(assignment)
    * ⭐ type() :변수에 할당된 값의 타입
    * id() :변수에 할당된 값의 고유한 아이덴티티 값이며, 메모리주소

```python
2+3
print(2+3)

위 두 줄의 명렁어를 파이썬에 입력하면 모두 5를 출력하지만
Terminal 에서 $ python 파일명 을 입력했을 때
5가 Terminal 에 5가 출력되는 것은 print(2+3) 뿐이다.

print(2+3)
print(2+3)
print(2+3)
print(2+3)
print(2+3)

이렇게 5회 연속으로 명령어를 입력해 두면 
$ python 파일명 입력해서 Terminal 에서 실행할 때
5 가 5회 연속으로 출력된다.

# hello 라는 이름의 변수에
# 'Happy Coding' 값을 할당
hello = 'Happy Coding'
print(hello)
print(hello)
print(hello)
print(hello)
print(hello)
이때도 $ python 파일명 입력해서 Terminal 에서 실행하면
Happy Coding 가 5회 연속으로 출력된다.

a = 5
b = 3
print(a + b)
이때 $ python 파일명 입력해서 Terminal 에서 실행하면
8이 출력된다.

# (기본원칙) 코드는 위에서부터 아래로 실행된다.
위와 같이 a = 5 라고 지정했다가,
a = 'hello'
print(a)
이때 $ python 파일명 입력해서 Terminal 에서 실행하면
hello 가 출력된다.

# (기본원칙2) 코드는 오른쪽에서 왼쪽으로 적용된다.
a = 5
a = a + 1
print(a)
```

* 실습 문제
  x = 10, y = 20 일 때,
  각각 값을 바꿔서 저장하는 코드를 작성하시오

  ```python
  # 풀이: 임시적인 변수가 필요하다
  tmp = x
  x = y
  y = tmp
  print(x, y)
  
  # 다른 풀이: pythonic!
  y, x = x, y
  print(x, y)
  ```

* 식별자

  * 파이썬 객체를 식별하는데 사용하는 이름
  * 규칙
    * 식별자의 이름은 영문 알파벳, 언더스코어, 숫자로 구성
    * 첫 글자에 숫자가 올 수 없음
    * 길이제한이 없고, 대소문자를 구별
    * 다음의 키워드는 예약어로 사용할 수 없음
      (pdf 보고 정리)

* 사용자 입력

  * input([prompt])

    ```python
    name = input('이름을 입력해주세요')
    print(name)
    ```

* 주석
  * 한 줄 주석
    주석으로 처리될 내용 앞에 '#' 을 입력



---



## 3. 파이썬 기본 자료형(Python Datatype)

* 자료형 분류

  * 변수 이름 = 타입(숫자, 문자, 불린, None)

  * 불린형(Boolean Type) : True / False 값을 가진 것

    * 비교/논리 연산을 수행함에 있어서 활용됨

    * bool() 함수: 특정 데이터가 True 인지 False 인지 검증

    * 연산자

      * 논리 연산자: 논리식을 판단하여 참(True)과 거짓(False)를 반환
  
        | 연산자  | 내용                       |
        | ------- | -------------------------- |
        | A and B | A 와 B 모두 True시, True   |
        | A or B  | A 와 B 모두 False시, False |
        | Not     | 참 거짓의 반대의 결과      |

  * 수치형(Numeric Type)
  
    * 정수(int) : 파이썬에서 모든 정수의 타입은 int
                       수가 아무리 커져도 오버플로우가 발생하지 않음
    * 실수(float) : 정수가 아닌 모든 실수는 float
                           알고리즘 처리할 땐 안쓰지만, 확률 처리할 땐 실수를 씀
                           부동소수점 - 실수를 연산할 때는 조심하자
    * 복소수 : pass
    * 산술 연산자 : %, /, //, ** 4가지에 유의(나머지, 나눗셈, 몫, 거듭제곱)
                             나머지(%) 연산은 정말 생각보다 많이 쓰임
                                              ex) 짝수인지, 홀수인지 확인할 때
  * 복합 연산자 : 초반에는 오른쪽처럼 쓰다가 왼쪽으로 코드를 바꿔가기
    * 비교연산자 : (pdf 보고 정리)

  * 문자열(Stiring Type)

    * 따옴표가 중요하다

    * 문자열음 작은 따옴표나 큰 따옴표를 활용하여 표기

    * 둘 중에 하나를 선택해서, 일관성 유지하며 쓰기만 하면 됨

    * 중첩따옴표, 삼중따옴표 직접 입력해보기
  
  * 인덱싱: 인덱스를 통해 특정 값에 접근할 수 있음
      s[1] => 'b'
  
    * 슬라이싱: 문자열을 잘라낼 수 있다 (예제 pdf 보고 추가)
      s[2:5:2] => 'ce'
      s[5:2:-1] => 'fed' 
      s[:3] 처음부터 3미만
      s[5:] 마지막부터 5까지
      s[::] 처음부터 끝까지 1씩 (=그대로)
      s[::-1] 처음부터 끝까지 -1씩 (=뒤집기, 거꾸로)
  
  ``` python
  a = 5     #int
  b = "5"   #str(문자열, 스트링)
  print(a)
  print(b)
  이때 $ python 파일명 입력해서 Terminal 에서 실행하면?
      
  print(a, type(a))
  print(b, type(b))
  이때 $ python 파일명 입력해서 Terminal 에서 실행하면
  각기 다른 타입이라는 것을 확인할 수 있다.
      
  # 길이
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

* None

  * 파이썬에서는 값이 없음을 표현하기 위해 None 타입이 존재

* 문자열의 활용

  * Escape Sequence
  * String Interpolation
  * 문자열의 특징: 추후 배워나갈 부분

  ```python
  # \ : 역슬래시 활용
  # 개행, 줄바꿈
  print('안녕하세요,\n반갑습니다.')
  이때 $ python 파일명 입력해서 Terminal 에서 실행하면
  안녕하세요,
  반갑습니다.
  위와 같이 줄 바꿈 처리가 됨
  
  # 따옴표
  print("따옴표를 '씁니다'")
  print('따옴표를 \'씁니다\'')
  # 출력결과 필기에 넣기
  
  # 역슬래시는 어떻게 쓰나요..????
  print('escape sequence는 역슬래시 \\를 활용합니다.')
  # 출력결과 필기에 넣기
  
  # 문자열 안에 변수 넣기: f-string 활용
  score = 100
  내 점수는 100이야 <- 이걸 출력하고 싶을 때
  print('내 점수는' + score + '이야.')
  위와 같이 입력하면 타입 에러가 발생
  따라서, 아래와 같이 수정
  print(f'내 점수는 {score}이야.')
  위와 같이 입력하면 '내 점수는 100이야.' 라고 정상 출력
  앞에 f를 붙이고, 중괄호에 변수를 직접 넣어주면 모두 해결됨
  
  pi = 3.14
  r = 2
  print(f'원주율은 {pi}고, 원 넓이는 {pi*2*2}')
  # 출력결과 필기에 넣기

* 형 변환(Typecasting)
  * 파이썬에서 데이터 형태는 서로 변환할 수 있음
    * 암시적 형 변환
      사용자가 의도하지 않고, 파이썬 내부적으로 자료형을 변환
    * 명시적 형 변환
      형식만 일치한다면 사용자가 직접 바꿔줌

```python
# 숫자와 문자는 더할 수 없어서, 따옴표 찍어서 숫자를 직접 문자열로 변환
score = 100
print('내 점수는 ' + str(score) + ' 이야.')
```



---



## 4. 컨테이너

* 컨테이너 정의
  * 컨테이너란? 여러 개를 담는 것
* 컨테이너 분류
  * 시퀀스
  * 비시퀀스

* 시퀀스

  * 문자열, 리스트, 튜플, 레인지

  * 순서가 있다 <- 인덱스로 접근

  * 시퀀스형 주요 공통 연산자
    x in s : s 안에 x 가 있니? 하고 물어보는 것
    s not in s : s 안에 x 가 없니? 하고 물어보는 것

  * 리스트

    * 변경 가능한 값들의 나열된 자료형

    * 순서를 가지며, 서로 다른 타입의 요소를 가질 수 있음
    * 리스트 값 추가/삭제: .append(), .pop()

  * 튜플
    * 소괄호() 혹은 tuple() 로 생성
    * 리스트랑 비교할 때, 변경 불가능하다는 특징이 있음
    * 직접 만들어서 쓰는 일은 없음

  * 레인지
    * 파이썬만의 특징
    * 숫자의 순서를 독특하게 나타냄(숫자의 통이라고 이해)
    * 변경 불가능하며(immutable), 반복 가능함(iterable)

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



* 컬렉션/비시퀀스형 컨테이너

  * 세트(유일한 값들의 모음), 딕셔너리(키-값의 모음)
    * 세트(Set): 유일한 값들의 모음
      * 순서가 없고 중복된 값이 없음
      * 변경 가능하며(mutable), 반복 가능함(iterable)
      * 세트 생성: 중괄호, 혹은 set()  *빈 중괄호는 딕셔너리 이용
      * 세트 추가/삭제: .add() .remove()
      * 세트를 활용하면 다른 컨테이너에서 중복된 값을 쉽게 제거
    * 딕셔너리: 키와 값의 쌍으로 이뤄진 모음
      * 딕셔너리 접근
      * 딕셔너리 키-값 추가 및 변경:
        키는 하나밖에 존재할 수 없기 때문에 기존 값을 변경하는 식으로
        키-값이 추가됨
        딕셔너리 키-값 삭제: .pop()   *키가 없으면 KeyError 발생

  * 세트, 딕셔너리 모두 순서가 없다

```python
# 세트
set_a = {1, 2, 3, 1, 1}
set_b = {'hi', 1, 2}
print(set_a)  : 이때 {1, 2, 3} 출력
print(set_b)  : 이때 {1, 2, 'hi'} 출력
# 즉, 순서가 없다

# 세트를 활용해 중복된 값 제거하기
location = ['서울', '서울', '대구', '제주', '부산', '부산', '대구', '광주', '인천']
print(set(locations)) :{'광주', '대구', '서울', '부산', '인천', '제주'} 처럼 중복된 값이 모두 제거된 것을 확인할 수 있음
print(len(set(locations))) :6 출력
```
