/*
조건문 기본
- if, else if, else 구조
- 조건은 소괄호(condition) 안에 작성
- 실행할 코드는 중괄호{} 안에 작성
*/

if (condition) {
  // do something
} else if (condition) {
  // do something
} else {
  // do something
}

const nation = 'Korea'
if (nation === 'Korea') {
    console.log('안녕하세요!')
} else if (nation === 'France') {
    console.log('Bonjour!')
} else {
    console.log('Hello!')
}

// if문 사례
const numOne = 5
const numTwo = 10
let operator = '+'

if (operator === '+') {
    console.log(numOne + numTwo)
} else if (operator === '-') {
    console.log(numOne - numTwo)
} else if (operator === '*') {
    console.log(numOne * numTwo)
} else if (operator === '/') {
    console.log(numOne / numTwo)
} else {
    console.log('유효하지 않은 연산자입니다.')
}
// 15

/////////////////////////////////////////////////////////////////////////////

switch(expression) {
  case 'first value': {
       // do something
      [break]
  }
  case 'second value': {
      // do something
      [break]
  }
  [default: {
       // do something
   }]
}

const nation = 'Korea'

switch(nation) {
    case 'Korea': {
        console.log('안녕하세요!')
    }
    case 'France': {
        console.log('Bonjour!')
    }
    default: {
        console.log('Hello!')
    }
}

/* 
위의 경우 출력값이 아래와 같음
(Fall-through, 이 경우에는 모두 출력)

안녕하세요!
Bonjour!
Hello!
*/

// switch문 사례
const numOne = 5
const numTwo = 10
let operator = '+'

switch(operator) {
    case '+': {
        console.log(numOne + numTwo)
        break
    }
    case '-': {
        console.log(numOne - numTwo)
        break
    }
    case '*': {
        console.log(numOne * numTwo)
        break
    }
    case '/': {
        console.log(numOne / numTwo)
        break
    }
    default: {
        console.log('유효하지 않은 연산자입니다.')
    }
}
// 15