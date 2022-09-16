# ✅ ECMA Script

> 1. Introduction
> 1. 변수와 식별자
> 1. 데이터 타입
> 1. 연산자
> 1. 조건문
> 1. 반복문
> 1. 함수
> 1. Arrow Function
> 1. 문자열 (String)
> 1. 배열 (Array)
> 1. 객체 (Objects)
>
> 💡 JavaScript 는 브라우저를 조작하려는 목적으로 시작된 언어기 때문에, 레거시 코드가 많습니다 (레거시 코드: **개발자가 변경하기 두려워하는 코드**)



## 1. Introduction

- 코딩 스타일 가이드
  - 코딩 스타일의 핵심은 합의된 원칙과 일관성
    - 절대적인 하나의 정답은 없으며, 상황에 맞게 원칙을 정하고 일관성 있게 사용하는 것이 중요
  - 코딩 스타일은 코드의 품질에 직결되는 중요한 요소
    - 코드의 가독성, 유지보수 또는 팀원과의 커뮤니케이션 등 개발 과정 전체에 영향을 끼침
  - (참고) 다양한 자바스크립트 코딩 스타일 가이드
    - 처음 습관을 잘 들이는게 좋으니까, **스타일 가이드 보면서 문법 익히기**
    - [Airbnb JavaScript Style Guide](https://github.com/airbnb/javascript)
    - [Google JavaScript Style Guide](https://google.github.io/styleguide/jsguide.html)
    - [standardjs](https://standardjs.com/#javascript-style-guide-linter-and-formatter)



---



## 2. 변수와 식별자

- 변수와 식별자

  - 식별자(identifier)는 변수를 구분할 수 있는 변수명을 말함

  - 식별자는 반드시 문자, 달러($) 또는 밑줄(_)로 시작

  - 대소문자를 구분하며, 클래스명 외에는 모두 소문자로 시작

  - 예약어 사용 불가능

    - 예약어 예시: for, if, function 등

  - (참고) 선언, 할당, 초기화

    ```javascript
    let foo           // 선언
    console.log(foo)  // undefined
    
    foo = 11          // 할당
    console.log(foo)  // 11
    
    let bar = 0       // 선언 + 할당
    console.log(bar)  // 0
    ```
    
    - 선언 (Declaration)
      - 변수를 생성하는 행위 또는 시점
    - 할당 (Assignment)
      - 선언된 변수에 값을 저장하는 행위 또는 시점
    - 초기화 (Initialization)
      - 선언된 변수에 처음으로 값을 저장하는 행위 또는 시점
  



- 변수 선언 [(link)](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Grammar_and_types#%EB%B3%80%EC%88%98_%EC%84%A0%EC%96%B8)

  - `let`, `const` 차이점

    - `let` (재할당 가능)

      ```javascript
      let number = 10      // 1. 선언 및 초기값 할당
      number = 10          // 2. 재할당 가능
      
      console.log(number)  // 10
      ```

    - `const` (재할당 불가능)

      ```javascript
      const number = 10  // 1. 선언 및 초기값 할당
      number = 10        // 2. 재할당 불가능(아래 에러 발생)
      // Uncaught TypeError: Assignment to constant variable.
      ```

  - `let`, `const` 공통점1 (vs. `var`)

    - `let` (재선언 불가능)

      ```javascript
      let number = 10  // 1. 선언 및 초기값 할당
      let number = 50  // 2. 재선언 불가능(아래 에러 발생)
      // Uncaught SyntaxError: Identifier 'number' has already been declared.
      ```

    - `const` (재선언 불가능)

      ```javascript
      const number = 10  // 1. 선언 및 초기값 할당
      const number = 50  // 2. 재선언 불가능(아래 에러 발생)
      // Uncaught SyntaxError: Identifier 'number' has already been declared.
      ```
  
      ⚠️유의: 크롬 콘솔창에서는 `let` 과 `const` 재선언 가능 [(link)](https://stackoverflow.com/questions/64582489/why-can-let-be-re-declared-in-the-devtools-console-in-chrome-other-browsers)
  
      ![js_ecma](js_ecma.assets/js_ecma.png)

      ![js_ecma_1](js_ecma.assets/js_ecma_1.png)

  - `let`, `const` 공통점2 (vs. `var`)

    - 블록 스코프(block scope)
      - if, for, 함수 등의 중괄호 내부를 가리킴
      - 블록 스코프를 가지는 변수는 블록 바깥에서 접근 불가능
      
      ```javascript
      let x = 1
      
      if (x === 1) {
          let x = 2
          console.log(x)  // 2
      }
      
      console.log(x)      // 1
      ```
  
  - `var` 
  
    - ES6 이전에 변수를 선언할 때 사용되던 키워드
  
    - `var` 로 선언한 변수는 **재선언 및 재할당 모두 가능**
  
      ```javascript
      var number = 10  // 1. 선언 및 초기값 할당
      var number = 50  // 2. 재할당
      
      console.log(number)  // 50
      ```
  
    - 함수 스코프(function scope)
  
      ```javascript
      function foo() {
          var x = 5
          console.log(x)  // 5
      }
      
      console.log(x)  // ReferenceError: x is not defined
      ```
  
      - 함수 스코프는 함수의 중괄호 내부를 가리킴
      - 함수 스코프를 가지는 변수는 함수 바깥에서 접근 불가능
  
    - **호이스팅(hoisting)** 특성으로 인해 예기치 못한 문제 발생 가능
  
      ```javascript
      console.log(username)  // undefined
      var username = '홍길동'
      
      console.log(email)     // Uncaught ReferenceError
      let email = 'abc@gmail.com'
      
      console.log(age)       // Uncaught ReferenceError
      const age = 50
      ```
  
      - 변수 선언 이전에 참조(`console.log()`)를 할 수 있는 현상
      - 변수 선언 이전의 위치에서 접근 시 `undefined` 반환
      - JavaScript 는 모든 선언을 호이스팅함
      - 즉, `var`, `let`, `const` 모두 호이스팅이 발생하지만, `var`는 선언과 초기화가 동시에 발생하여 일시적인 사각지대가 존재하지 않음
      - 이러한 이유 때문에 **ES6 이후부터는 var 대신 const 와 let 사용을 권장**
  
  - `let`, `const`, `var` 비교
  
    | 키워드  | 재선언 | 재할당 | 스코프      | 비고  |
    | ------- | ------ | ------ | ----------- | ----- |
    | `let`   | X      | O      | 블록 스코프 | ES6 ~ |
    | `const` | X      | X      | 블록 스코프 | ES6 ~ |
    | `var`   | O      | O      | 함수 스코프 | 비추👎 |
  
    

---



## 3. 데이터 타입

- 데이터 타입
  - 자바스크립트의 모든 값은 특정한 데이터 타입을 가짐
  - 크게 원시 타입(Primitive type)과 참조 타입(Reference type) 으로 분류됨



- 원시 타입(Primitive type)

  - Number, String, Boolean, undefined, null, Symbol
  - 객체(object)가 아닌 기본 타입
  - 변수에 해당 타입의 값이 담김
  - 다른 변수에 복사할 때 실제 값이 복사됨

  ```javascript
  let message = '안녕하세요!'  // 1. message 선언 및 할당
  
  let greeting = message     // 2. greeting 에 message 복사
  console.log(greeting)      // 3. '안녕하세요!' 출력
  
  message = 'Hello, world!'  // 4. message 재할당
  console.log(greeting)      // 5. '안녕하세요!' 출력
  
  // 즉, 원시 타입은 실제 해당 타입의 값을 변수에 저장함
  ```



- 참조 타입(Reference type) 

  - Array, Function, ... etc. ⊂ Objects ⊂ Reference type
  - 객체(object) 타입의 자료형
  - 변수에 해당 객체의 참조 값이 담김
  - 다른 변수에 복사할 때 참조 값이 복사됨

  ```javascript
  const message = ['안녕하세요!']  // 1. message 선언 및 할당
  
  const greeting = message       // 2. greeting 에 message 복사
  console.log(greeting)          // 3. ['안녕하세요!'] 출력
  
  message[0] = 'Hello, world!'   // 4. message 재할당
  console.log(greeting)          // 5. ['Hello, world!'] 출력
  
  // 즉, 참조 타입은 해당 객체를 참조할 수 있는 참조 값을 저장함
  ```

  

- [Primitive] 숫자 타입(Number)
  
  - 정수, 실수 구분 없는 하나의 숫자 타입
  - 부동소수점 형식을 따름
  - (참고) NaN (Not-A-Number)
    - 계산 불가능한 경우 반환되는 값
      - ex) 'Angel' / 1004 => NaN
  
  ```javascript
  const a = 13         // 양의 정수
  const b = -5         // 음의 정수
  const c = 3.14       // 실수
  const d = 2.998e8    // 거듭제곱
  const e = Infinity   // 양의 무한대
  const f = -Infinity  // 음의 무한대
  const g = NaN        // 산술 연산 불가
  ```
  
  

- [Primitive] 문자열 타입(String)
  
  - 텍스트 데이터를 나타내는 타입
  - 16비트 유니코드 문자의 집합
  - 작은따옴표 또는 큰따옴표 모두 가능
  - 템플릿 리터럴(Template Literal)
    - ES6부터 지원
    - 따옴표 대신 backtick(``)으로 표현
    - ${expression} 형태로 삽입 가능
  
  ```javascript
  const firstName = 'Brandan'
  const lastName = 'Eich'
  const fullName = '${firstName} ${lastName}'
  
  console.log(fullName)  // Brandan Eich
  ```
  
  

- [Primitive] undefined

  - 변수의 값이 없음을 나타내는 데이터 타입
  - 변수 선언 이후 직접 값을 할당하지 않으면, 자동으로 undefined 가 할당됨

  ```javascript
  let firstName
  console.log(firstName)  // undefined
  ```

  

- [Primitive] null
  
  - 변수의 값이 없음을 의도적으로 표현할 때 사용하는 데이터 타입
  - (참고) null 타입과 typeof 연산자 (세부 내용은 중요하지 않음)
    - typeof 연산자: 자료형 평가를 위한 연산자
    - null 타입은 [ECMA 명세의 원시 타입 정의](https://tc39.es/ecma262/#sec-primitive-value)에 따라 원시 타입에 속하나, typeof 연산자 결과는 객체(object)로 표현됨 [(link)](https://2ality.com/2013/10/typeof-null.html)
  
  ```javascript
  let firstName = null
  console.log(firstName)  // null
  
  typeof null  // object
  ```
  
  

- [Primitive] Boolean 타입

  - 논리적 참 또는 거짓을 나타내는 타입
  - true 또는 false 로 표현됨
  - 조건문 또는 반복문에서 유용하게 사용
    - (참고) 조건문 또는 반복문에서 boolean이 아닌 데이터 타입은 [자동 형변환 규칙](https://tc39.es/ecma262/#sec-type-conversion)에 따라 true 또는 false로 변환됨

  ```javascript
  let isAdmin = true
  console.log(isAdmin)  // true
  
  isAdmin = false
  console.log(isAdmin)  // false
  ```

  

- (참고) [ToBoolean Conversions (자동 형변환)](https://tc39.es/ecma262/#sec-toboolean) 정리

  | 데이터 타입 | 거짓       | 참               |
  | ----------- | ---------- | ---------------- |
  | `undefined` | 항상 거짓  | X                |
  | `null`      | 항상 거짓  | X                |
  | Number      | 0, -0, NaN | 나머지 모든 경우 |
  | String      | 빈 문자열  | 나머지 모든 경우 |
  | Object      | X          | 항상 참          |

  

---



## 4. 연산자

- 할당 연산자
  - 오른쪽에 있는 피연산자의 평가 결과를 왼쪽 피연산자에 할당하는 연산자
  - 다양한 연산에 대한 단축 연산자 지원
  - (참고) Increment 및 Decrement 연산자
    - 파이썬이랑 다른 부분!
    - Increment(++): 피연산자 값을 1 증가시키는 연산자
    - Decrement(--): 피연산자 값을 1 감소시키는 연산자
    - [Airbnb Style Guide](https://github.com/airbnb/javascript#variables--unary-increment-decrement) 에서는 '+=' 또는 '-=' 와 같이 더 분명한 표현으로 적을 것을 권장
  
  ```javascript
  let x = 0
  
  x += 10
  console.log(x)  // 10
  
  x -= 3
  console.log(x)  // 7
  
  x *= 10
  console.log(x)  // 70
  
  x /= 10
  console.log(x)  // 7
  
  x++             // += 1 연산과 동일
  console.log(x)  // 8
  
  x--             // -= 1 연산과 동일
  console.log(x)  // 7
  ```



- 비교 연산자

  - 피연산자를 비교하고 결과값을 boolean으로 반환하는 연산자
  - 문자열은 유니코드 값을 사용하며 표준 사전 순서를 기반으로 비교
    - ex) 알파벳끼리 비교할 경우
      - 알파벳 순서상 후순위가 더 크다
      - 소문자가 대문자보다 더 크다

  ```javascript
  const numOne = 1
  const numTwo = 100
  console.log(numOne < numTwo)   // true
  
  const charOne = 'a'
  const charTwo = 'z'
  console.log(charOne > charTwo)  // false
  ```

  

- 동등 비교 연산자(==)

  - 두 피연산자가 같은 값으로 평가되는지 비교 후 boolean 값을 반환

  - 비교할 때 [암묵적 타입 변환](https://262.ecma-international.org/5.1/#sec-11.9.3)을 통해 타입을 일치시킨 후 같은 값인지 비교

  - 두 피연산자가 모두 객체일 경우 메모리의 같은 객체를 바라보는지 판별

  - 예상치 못한 결과가 발생할 수 있으므로 [특별한 경우](https://google.github.io/styleguide/jsguide.html#features-equality-checks-exceptions)를 제외하고 사용하지 않음

    ![js_ecma_2](js_ecma.assets/js_ecma_2.png)

  ```javascript
  const a = 1004
  const b = '1004'
  console.log(a == b)  // true
  
  const c = 1
  const d = true
  console.log(c == d)  // true
  
  // 자동 타입 변환 예시
  console.log(a + b)   // 10041004
  console.log(c + d)   // 2
  ```

  

- 일치 비교 연산자(===)
  - JS에서는 이퀄 기호를 무조건 === 로 쓴다는 사실을 기억하자!



- 논리 연산자
  - and 연산은 '&&' 연산자를 이용
  - or 연산은 '||' 연산자를 이용



- 삼항 연산자(Ternary Operator)
  - 세 개의 피연산자를 사용하여 조건에 따라 값을 반환하는 연산자
  - if 문까지 짤 필요는 없을 것 같을 때 활용
  - 가장 왼쪽의 조건식이 참이면 



---



## 5. 조건문

- 조건문의 종류와 특징
  - 'if' statement
    - if, else if, else 구조
    - 파이썬이랑 다르게 들여쓰기(인덴테이션) 기반으로 동작하는게 아니기 때문에 위 구조를 정확하게 써주는게 중요
  - 'switch' statement
    - 표현식의 결과값을 이용한 조건문
    - 표현식의 결과값과 case 문의 오른쪽 값을 비교



---



## 6. 반복문

- 반복문의 종류와 특징
  - while
  - for
  - for ... in
  - for ... of



---



## 7. 함수

> JS에서는 특히나 함수가 중요! **콜백함수** 패턴이 특히 중요!



- 함수 in JavaScript
  - 참조 타입 중 하나로써 function 타입에 속함
  - JavaScript 에서 함수를 정의하는 방법은 주로 2가지로 구분
    - 함수 선언식
    - 함수 표현식
  - 일급 ~  이건 파이썬과도 동일!



- 함수의 정의
  - 함수의 이름과 함께 정의하는 방식
  - 3가지 부분으로 구성



---



## 8. Arrow Function



- Q. 모든 함수를 Arrow Function 으로 써도 되나요?
  - A. 지금 여러분이 쓰는 문법 수준에서는 크게 문제가 될게 없습니다.



---



## 9. 문자열 (String)

> 메서드 다 외울 필요는 없고 파이썬이랑 비교해보면서 익혀둡시다



---



## 10. 배열 (Array)

> 여기도 메서드 다 외울 필요는 없습니다



- join
  - 파이썬에서는 join 이 문자열의 매서드였는데, JS는 배열의 메서드라는 점 기억!



- 콜백지옥 img
  - https://velog.io/@ko1586/Callback%ED%95%A8%EC%88%98%EB%9E%80-%EB%AD%94%EB%8D%B0 글이랑 같이 보기



---



## 11. 객체 (Objects)



04_event.html 코드 복습해보면, addeventlistener click 안에 들어가있던 function() 이 콜백함수!