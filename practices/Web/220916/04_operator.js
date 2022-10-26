// 연산자 기본
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

/////////////////////////////////////////////////////////////////////////////

// 비교 연산자
const numOne = 1
const numTwo = 100
console.log(numOne < numTwo)   // true
const charOne = 'a'
const charTwo = 'z'
console.log(charOne > charTwo)  // false

// 일치 비교 연산자
const a = 1004
const b = '1004'
console.log(a === b)  // false
const c = 1
const d = true
console.log(c === d)  // false

/////////////////////////////////////////////////////////////////////////////

/*
논리 연산자
- and 연산은 '&&' 연산자를 이용
- or 연산은 '||' 연산자를 이용
- not 연산은 '!' 연산자를 이용
*/

// and 연산
console.log(true && false)   // false
console.log(true && true)    // true
console.log(1 && 0)          // 0 
console.log(4 && 7)          // 7 
console.log('' && 5)         // '' 

// or 연산
console.log(true || false)   // true
console.log(false || false)  // false
console.log(1 || 0)          // 1
console.log(4 || 7)          // 4
console.log('' || 5)         // 5

// not 연산
console.log(!true)           // false
console.lod(!'Bonjour!')     // false