/*
Primitive type (원시타입)
- Number, String, Boolean, undefined, null, Symbol
- 다른 변수에 저장할 때 실제 해당 타입의 값을 저장
*/
let message = '안녕하세요!'
let greeting = message
console.log(greeting)  // '안녕하세요!' 출력
message = 'Hello, world!'
console.log(greeting)  // '안녕하세요!' 출력

// Number
const a = 13         // 양의 정수
const b = -5         // 음의 정수
const c = 3.14       // 실수
const d = 2.998e8    // 거듭제곱
const e = Infinity   // 양의 무한대
const f = -Infinity  // 음의 무한대
const g = NaN        // 산술 연산 불가

// String
const firstName = 'Brandan'
const lastName = 'Eich'
const fullName = '${firstName} ${lastName}'
console.log(fullName)  // Brandan Eich

// Boolean
let isAdmin = true
console.log(isAdmin)  // true
isAdmin = false
console.log(isAdmin)  // false

// undefined
let firstName
console.log(firstName)  // undefined

// null
let firstName = null
console.log(firstName)  // null
typeof null  // object

/////////////////////////////////////////////////////////////////////////////

/*
Reference type (참조타입)
- Array, Function, ... etc. ⊂ Objects ⊂ Reference type
- 다른 변수에 저장할 때 해당 객체를 참조할 수 있는 참조 값이 복사됨
*/
const message = ['안녕하세요!']
const greeting = message
console.log(greeting)  // ['안녕하세요!'] 출력
message[0] = 'Hello, world!'
console.log(greeting)  // ['Hello, world!'] 출력