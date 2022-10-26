let foo  // 선언 : 변수를 생성하는 행위 또는 시점
console.log(foo)  // undefined

foo = 11  // 할당 : 선언된 변수에 값을 저장하는 행위 또는 시점
console.log(foo)  // 11

let bar = 0  // 선언 + 할당
console.log(bar)  // 0

/////////////////////////////////////////////////////////////////////////////

let number = 10  // 1. 선언 및 초기값 할당
number = 10  // 2. 재할당 가능 ... 이런 특징 때문에 반복문에서 자주 씀
console.log(number)  // 10

const number = 10  // 1. 선언 및 초기값 할당
number = 10  // 2. 재할당 불가능 (아래와 같은 에러 발생)
// Uncaught TypeError: Assignment to constant variable.

/////////////////////////////////////////////////////////////////////////////

let number = 10  // 1. 선언 및 초기값 할당
let number = 50  // 2. 재선언 불가능 (아래와 같은 에러 발생)
// Uncaught SyntaxError: Identifier 'number' has already been declared.

const number = 10  // 1. 선언 및 초기값 할당
const number = 50  // 2. 재선언 불가능 (아래와 같은 에러 발생)
// Uncaught SyntaxError: Identifier 'number' has already been declared.

/////////////////////////////////////////////////////////////////////////////

/* 
let, const 공통점 : if, for, 함수 등 중괄호를 갖는 변수는 
중괄호 바깥에서 접근 불가능
*/
let x = 1
if (x === 1) {
  let x = 2
  console.log(x)  // 2
}
console.log(x)  // 1