# ✅ ECMA Script 심화

> 1. Callback function
> 2. 배열 관련 주요 메서드 목록(2) - 심화편 (Array Helper Methods)



## 1. Callback function

> 하단 코드 복습해보면, `addEventListener` 구문 안에 있던 function() 이 콜백함수!

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .blue {
      color: blue;
    }
  </style>
</head>
<body>
  <button id="btn1">클릭</button>
  <input type="text">

  <script>
    // btn1
    const btn1 = document.querySelector('#btn1')
    // btn1이 클릭되면 함수실행
    btn1.addEventListener('click', function() {
      // h1 태그를 잡아서
      const h1 = document.querySelector('h1')
      // 클래스 blue를 토글하자. 
      h1.classList.toggle('blue')
    })

    // input
    const input = document.querySelector('input')
    input.addEventListener('input', function(e) {
      console.log(e.target.value)
    })
  </script>
</body>
</html>
```



- Callback function 이란? [(link)](https://developer.mozilla.org/en-US/docs/Glossary/Callback_function)

  - 특정한 함수가 어떤 조건에 따라 호출하는 함수

    - 어떤 조건의 예시 : 이벤트 발생, 특정 시점에 도달 ...

  - 고유한 문법 특징은 없고, 함수를 호출하는 방식에 따라 콜백인지 아닌지로 구분

  - 즉각적으로 실행되는 **동기적 콜백**과 나중에 실행되는 **비동기적 콜백**으로 구분

    - 동기적 콜백의 예시 [(link)](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous/Introducing)
      - Here, `makeGreeting()` is a **synchronous function** because the caller has to wait for the function to finish its work and return a value before the caller can continue.

    ```javascript
    function makeGreeting(name) {
      return `Hello, my name is ${name}!`;
    }
    
    const name = 'Miriam';
    const greeting = makeGreeting(name);
    console.log(greeting);
    // "Hello, my name is Miriam!"
    ```

    - 비동기적 콜백의 예시 [(link)](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous/Introducing#a_long-running_synchronous_function)
      - Event handlers are really a form of asynchronous programming: you provide a function (the event handler) that will be called, not right away, but whenever the event happens.
      - 이벤트 핸들러 : 이벤트 리스너에 등록된 콜백함수, 코드에 등록된 이벤트가 발생하면 이벤트 리스너가 이를 듣고 이벤트 핸들러를 실행시킴
      - 하단 예시에서 이벤트는 `'click'`

    ```javascript
    const btn1 = document.querySelector('#btn1')
    
    btn1.addEventListener('click', function() {
        const h1 = document.querySelector('h1')
        h1.classList.toggle('blue')
    })
    ```

    

---



## 2. 배열 관련 주요 메서드 목록(2) - 심화편 (Array Helper Methods)

> 배열을 순회하며 특정 로직을 수행하는 메서드
>
> 메서드 호출 시 인자로 callback 함수를 받는 것이 특징

| 메서드    | 설명                                                     | 비고         |
| --------- | -------------------------------------------------------- | ------------ |
| `forEach` | 배열의 각 요소에 대해 콜백함수를 한 번씩 실행            | 반환 값 없음 |
| `map`     | 콜백함수의 반환 값을 요소로 하는 새로운 배열 반환        |              |
| `filter`  | 콜백함수의 반환 값이 참인 요소만 모아서 새로운 배열 반환 |              |
| `reduce`  | 콜백함수의 반환 값을 하나의 값(acc)에 누적 후 반환       |              |
| `find`    | 콜백함수의 반환 값이 참이면 해당 요소를 반환             |              |
| `some`    | 배열 요소 중 하나라도 판별 함수를 통과하면 참을 반환     |              |
| `every`   | 배열의 모든 요소가 판별 함수를 통과하면 참을 반환        |              |



- `array.forEach(callback(element[, index[, array]]))`

  - 배열의 각 요소에 대해 콜백함수를 한 번씩 실행
  - 콜백함수는 3가지 매개변수로 구성
    - element : 배열의 요소
    - index : 배열 요소의 인덱스
    - array : 배열 자체
  - 반환 값(return)이 없는 메서드

  ```javascript
  array.forEach((element, index, array) => {
      // do something
  })
  ```

  ```javascript
  const fruits = ['딸기', '수박', '사과', '체리']
  
  fruits.forEach((fruit, index) => {
      console.log(fruit, index)
      // 딸기 0
      // 수박 1
      // 사과 2
      // 체리 3
  })
  ```

  
