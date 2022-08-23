# ✅Python 에러/예외 처리(Error/Exception Handling)

> 1. 디버깅
> 2. 에러와 예외
> 3. 예외 처리
> 4. 예외 발생 시키기
>
> 💡여러 줄의 소스 코드 한꺼번에 주석(#) 처리하기 `ctrl + /`



- 디버깅 오류 해결하기
  - 제어가 되는 시점에서 내가 원하는대로 제어가 되고 있는지 확인하자



---



## 1. 디버깅

- 디버깅이란?
  - 벌레 죽이기! 컴퓨터 오류를 찾아서 해결하기!
  - **branches** 모든 조건이 원하는대로 동작하는지
  - **for loops** 반복문에 진입하는지, 원하는 횟수만큼 실행되는지
  - **while loops** for loops와 동일, 종료조건이 제대로 동작하는지
  - **function** 함수 호출시, 함수, 파라미터, 함수 결과



- 디버깅 방법

  > "코드의 상태를 신중하게 출력해가며 심사숙고하는 것보다 효과적인 디버깅 도구는 없습니다."
  >
  > ㅡ 브라이언 커니핸, Unix for Beginners

  - `print` 함수 활용
    - 특정 함수 결과, 반복/조건 결과 등 나눠서 생각, 코드를 bisection으로 나눠보기
  - 개발 환경(text editor, IDE) 등에서 제공하는 기능 활용
    - [VS Code] breakpoint, 변수 조회 등
  - Python tutor 활용 (단순 파이썬 코드인 경우)
  - 뇌컴파일, 눈디버깅



- [VS Code] breakpoint 활용하여 디버깅하는 법
  - [파일 읽기를 통한 입력 처리 & 디버그 (notion.so)](https://www.notion.so/hphk-edu/cffd699a97f045d98da99e37b3e1d905) 확인하면서 노트정리 다시 보완



---



## 2. 에러와 예외

- 문법 에러 (`Syntax Error`)

  * 발생하면 쉽게 고칠 수 있음. 파이썬 프로그램은 실행이 되지 않음

  * 파일이름, 줄번호, `^` 문자를 통해 파이썬 코드를 읽어 나갈 때(parser) 문제가 발생한 위치를 표현(코드에 힌트가 있으니 그 라인 시점을 보고 고치기)

  * 줄에서 에러가 감지된 가장 앞의 위치를 가리키는 캐럿(caret)기호(`^`)를 표시
  * 문법 에러의 다양한 사례 ▽

  ```python
  [invalid syntax]
  if else
  # File "<ipython-input-1-f8a097d0a685>", line 1
  # if else ^
  # Syntax Error: invalid syntax
  
  [EOL (End of Line)]
  print('hello
  # File "<ipython-input-6-2a5f5c6b1414>", line 1
  # print('hello
  #     ^
  # SyntaxError: EOL while scanning string literal
        
  [EOF (End of File)]
  print(
  # File "<ipython-input-4-424fbb3a34c5>", line 1
  # print(
  #     ^
  # SyntaxError: unexpected EOF while parsing
      
  [assign to literal]
  5 = 3
  # File "<ipython-input-28-9a762f2c796b>", line 1
  # 5 = 3
  # ^
  # SyntaxError: cannot assign to literal
  ```



- 예외 (`Exception`)

  * 실행 도중 예상치 못한 상황을 맞이하면, 프로그램 실행을 멈춤
    * 문장이나 표현식이 문법적으로 올바르더라도 발생하는 에러

  * 실행 중에 감지되는 에러들을 예외라고 부름
  * 예외는 여러 타입(type)으로 나타나고, 타입이 메시지의 일부로 출력됨
    * `NameError`, `TypeError` 등은 발생한 예외 타입의 종류(이름)

  * 모든 내장 예외는 Exception Class를 상속받아 이뤄짐

  * 사용자 정의 예외를 만들어 관리할 수 있음



- 예외의 다양한 종류

  - `ZeroDivision Error` 0으로 나누고자 할 때 발생
  - `NameError` namespace 상에 이름이 없는 경우
  - `TypeError` 타입 불일치 / arguments 부족 / argument 개수 초과
  - `ValueError` 타입은 올바르나 값이 적절하지 않거나 없는 경우
  - `IndexError` 인덱스값이 범위를 벗어났을 경우
  - `KeyError` 특정 딕셔너리에 존재하지 않는 키값을 입력했을 경우
  - `ModuleNotFoundError` 존재하지 않는 모듈을 import 하는 경우
  - `ImportError` Module은 있으나 존재하지않는 클래스/함수를 가져오는 경우
  - `IndentationError` 들여쓰기가 적절하지 않은 경우
  - `KeyboardInterrupt` 임의로 프로그램을 종료하였을 때

  ```python
  while True:
      print(1)
      
  # 위의 결과값이 무한하게 반복될 때, 터미널에서 ctrl+c 누르면 작업종료 가능!
  ```



💡`with base 10` == 10진수로 봤을 때

💡[파이썬 내장 예외의 클래스 계층 구조](https://docs.python.org/ko/3/library/exceptions.html#exception-hierarchy)



---



## 3. 예외처리

- 예외처리
  - 가장 중요한 개념이 예외 처리를 할 수 있는 구문이 따로 있다는 점!
  - 파이썬에서는 `try`문(statement), `except`절(clause) 2가지
  - 지금은 출력으로 예외 처리를 공부하고 있지만, 실제 현업에서는 예외 처리 부분에 특정한 기능들이 들어가게 됨



- `try`문 & `except`절

  - `try`문
    - 오류가 발생할 가능성이 있는 코드를 실행
    - 예외가 발생되지 않으면, `except` 없이 실행 종료
  - `except`절
    - 예외가 발생하면, `except`절이 실행됨
    - 예외 상황을 처리하는 코드를 받아서 적절한 조치를 취함
  - [주의] `try`문은 반드시 한 개 이상의 `except`절이 필요
  - 작성 방법 ▽

  ```python
  try:
      <try 명령문> : 검증하고 싶은 코드를 실행하는 부분
  except 예외그룹-1 as 변수-1 :
      <예외처리 명령1> - try 문에서 예외가 발생했을 때 실행
  except 예외그룹-2 as 변수-2 :
      <예외처리 명령2> - try 문에서 또 다른 예외가 발생했을 때 실행
  # 하단의 finally: 이하는 선택사항
  finally:
      <finally 명령문> - 예외 발생 여부와 관계없이 항상 실행
  ```



- 단일 예외 처리 예시

  ```python
  num = input('숫자입력 : ')
  print(int(num))
  
  # 위와 같은 코드를 작성했을 때, 
  # 입력 값에 '3'을 넣으면 정상적으로 '3'이 출력되지만,
  # 입력 값에 '안녕'을 넣으면 int 변환이 될 수 없기 때문에
  # ValueError 발생
  
  # 따라서 아래와 같이 예외 처리 코드를 작성
  try:
      num = input('숫자입력 : ')
      print(int(num))
  except:
      print('숫자가 아닙니다')
      
  try:
      num = input('숫자입력 : ')
      print(int(num))
  except ValueError:
      print('숫자가 아닙니다')
  ```

  

- 복수의 예외 처리 실습

  - Q: 100을 사용자가 입력한 값으로 나누고 출력하는 코드를 작성해보시오

    (먼저, 발생 가능한 에러가 무엇인지 예상해보기)

  ```python
  num = input('100으로 나눌 값을 입력하시오 : ')
  print(100/int(num))
  
  # 발생 가능한 에러: num에 문자를 입력할 때, num에 0을 입력할 때
  # 따라서 아래와 같이 예외 처리 코드를 작성
  
  # 발생 가능한 에러를 모두 명시
  try:
      num = input('100으로 나눌 값을 입력하시오 : ')
  	100/int(num)
  except (ValueError, ZeroDivisionError):
      print('제대로 입력해줘')
      
  # 각각의 에러에 따라 별도의 에러 처리
  try:
      num = input('100으로 나눌 값을 입력하시오 : ')
  	100/int(num)
  except ValueError:
      print('숫자를 넣어주세요')
  except ZeroDivisionError:
      print('0으로 나눌 수 없습니다')
  except:
      print('무슨 에러인지 모르지만 에러가 발생하였습니다')
  ```

  

- 예외 처리의 실제 예시

  - 파일을 열고 읽는 코드를 작성하는 경우
    - 파일 열기 시도
      - 파일 없는 경우 → '해당 파일이 없습니다' 출력 `except`
      - 파일이 있는 경우 → 파일 내용을 출력 `else`
    - 해당 파일 읽기 작업 종료 메시지 출력 `finally`

  ```python
  try:
      f = open('nooofile.txt')
  except FileNotFoundError:
      print('해당 파일이 없습니다')
  else:
      print('파일을 읽기 시작합니다')
      print(f.read())
      print('파일을 모두 읽었습니다')
      f.close()
  finally:
      print('파일 읽기를 종료합니다')
  ```

  

---



## 4. 예외 발생 시키기

- `raise` statement

  - `raise`를 통해 예외를 강제로 발생 ▽

  ```python
  raise <표현식> (메시지)
  # 위 <표현식> 자리에 예외 타입을 지정
  # 예외 타입이 주어지지 않을 경우
  # 현재 스코프에서 활성화된 마지막 예외를 다시 일으킴
  
  raise
  # -------
  # RuntimeError Traceback (most recent call last)
  # ----> 1 raise
  # RuntimeError: No active exception to reraise
  ```

  - 어떤 코드를 입력해도 그 다음 줄에 `raise` 를 넣으면 무조건 에러 코드가 뜸
  - 파이썬 실제 소스 코드에 엄청 많이 들어있음
  - 파이썬을 쓰는 사람들에게 잘못된 코드들이 오류라는 것을 알려주기 위한 용도
  - 다만, 지금은 에러 메세지를 잘 해석하는데 집중해서 공부하자!
  - 파이썬에 기본적으로 내장되어 있는 안내문도 같이 프린트 해보고 싶다면?
    - `err` 활용!

