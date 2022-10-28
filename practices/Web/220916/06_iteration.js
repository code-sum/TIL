// 1. while

while (condition) {
  // do something
}

let i = 0
while (i<6) {
    console.log(i)
    i += 1
}

/*
위 코드 작성시 출력값은 아래와 같음

0
1
2
3
4
5
*/

/////////////////////////////////////////////////////////////////////////////

// 2. for ... in

for (variable in object) {
  // do something
}

const capitals = {
  korea: 'seoul',
  france: 'paris',
  USA: 'washington D.C.'
}

for (let capital in capitals) {
  console.log(capital)
}

/*
korea
france
USA
*/

/////////////////////////////////////////////////////////////////////////////

// 3. for ... of

for (variable of iterables) {
  // do something
}

const fruits = ['딸기', '바나나', '메론']

for (let fruit of fruits) {
    fruit = fruit + '!'
    console.log(fruit)
}

/*
딸기!
바나나!
메론!
*/

/////////////////////////////////////////////////////////////////////////////

// for ... in (객체 순회에 적합)

// array
const fruits = ['딸기', '바나나', '메론']

for (let fruit in fruits) {
    console.log(fruit)
}
/*
0
1
2
*/

// object
const capitals = {
    Korea: '서울',
    France: '파리',
    USA: '워싱턴 D.C.'
}

for (let capital in capitals) {
    console.log(capital)
}
/*
Korea
France
USA
*/

/////////////////////////////////////////////////////////////////////////////

// for ... of (배열 순회에 적합)

// array
const fruits = ['딸기', '바나나', '메론']

for (let fruit of fruits) {
    console.log(fruit)
}
/*
딸기
바나나
메론
*/

// object
const capitals = {
    Korea: '서울'
    France: '파리'
    USA: '워싱턴 D.C.'
}

for (let capital of capitals) {
    console.log(capital)
}
// Uncaught TypeError: capitals is not iterable