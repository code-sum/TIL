console.log('hello, js!')

alert('js 학습이 시작되었습니다.')

// h1 요소(element)를 만들고
const title = document.createElement('h1')

// 텍스트를 추가하고
title.innerText = 'JS 기초' 

// 선택자로 body태그를 가져와서
const body = document.querySelector('body')

// body태그에 자식 요소로 추가
body.appendChild(title)