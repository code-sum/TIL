# ✅ JavaScript INTRO

> 1. JavaScript Intro
> 2. History of JavaScript
> 3. DOM(Document Object Model)
> 4. DOM 조작
>
> 💡 개발자도구 찍었을 때 consol 창에 뜨는 내용은 JavaScript 로 작성한 것!
>
> 🗂️ [(참고서1)](https://developer.mozilla.org/ko/docs/Web/JavaScript) [(참고서2)](https://developer.mozilla.org/ko/docs/Learn/JavaScript)



#### 📂 새로운 프로그래밍 언어를 학습하는 마음가짐

```html
입사해서 새로운 언어를 공부한다고 해도 [변수, 데이터타입, 조건, 반복, 함수] 의 기본 구조는 동일하므로, 이에 따라 학습하면 금방 따라갈 수 있음!
```



#### 📂 JavaScript ES6+ 관련 교재

```html
아래로 내려갈수록 어려운 책(대략)

「초보자를 위한 Javascript 200제」
「모던 자바스크립트 Deep Dive」
「YOU DON'T KNOW JS」
「Node.js 디자인 패턴 바이블」
```

| [시작](https://developer.mozilla.org/ko/docs/Learn/JavaScript/First_steps/What_is_JavaScript) | [문법과 자료형](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Grammar_and_types) | [제어문](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Control_flow_and_error_handling) | [반복](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Loops_and_iteration) | [함수](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Functions ) | [표현식 연산자](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Expressions_and_Operators) |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |

- 온라인 자료(ENG)
  - https://eloquentjavascript.net/
  - https://exploringjs.com/
- 온라인 자료(KOR)
  - https://ko.javascript.info/
  - https://learnjs.vlpt.us/



---



## 1. JavaScript Intro

- 브라우저(browser)
  - URL로 웹(WWW)을 탐색하며 서버와 통신하고, HTML 문서나 파일을 출력하는 GUI 기반 소프트웨어
  - 인터넷 컨텐츠를 검색 및 열람하도록 함
  - "웹 브라우저"라고도 함
  - 주요 브라우저
    - Google Chrome, Mozilla Firefox, Microsoft Edge, Opera, Safari



- JavaScript 필요성
  - 브라우저를 조작할 수 있는 유일한 언어
  - 브라우저 화면을 '동적'으로 만들기 위함
    - 이렇게 동적 표현을 할 수 있는 유일한 프로그래밍 언어
    - 2021년 서베이 결과 가장 널리 쓰이는 프로그래밍 언어 1위
      - Stackoverflow 서베이 결과 [(link)](https://insights.stackoverflow.com/survey/2021#technology-most-popular-technologies)
      - Jetbrain 서베이 결과 [(link)](https://www.jetbrains.com/ko-kr/lp/devecosystem-2021/)



- JavaScript 탄생
  - 1994년 넷스케이프 커뮤니케이션스사의 Netscape Navigator(NN) 브라우저가 전 세계 점유율 80% 이상 독점하며 브라우저 표준 역할
  - 당시 넷스케이프에 재직하고 있던 브랜던 아이크가 HTML을 동적으로 표현하기 위해 회사 내부 프로젝트를 진행하다가 JS를 개발
  - JavaScript 이름의 변화
    - Mocha → LiveScript → JavaScript (1995)
  - 1995년 경쟁사 마이크로소프트에서 이를 커스터마이징한 JScript 만듦
    - 이걸 IE 1.0 에 탑재 → 1차 브라우저 전쟁 시작



---



## 2. History of JavaScript

> 💡 [브라우저 전쟁] 참조 https://www.wikiwand.com/en/Browser_wars



- 제1차 브라우저 전쟁
  - 넷스케이프 vs 마이크로소프트(이하 MS)
  - 1997년 MS에서 IE 4를 발표하며 시장을 장악하기 시작
    - 당시 윈도우OS 시장 점유율 90%
    - IE 3 에서 자체적인 JScript 를 지원해왔으나, 크로스 브라우징 이슈
  - 1차 전쟁이 MS의 승리로 끝나며 2001년부터 IE 점유율 90% 이상
  - 1998년 넷스케이프를 퇴사한 브랜던 아이크와 동업자들이 모질라 재단 설립
    - 파이어폭스를 개발해 IE 와 경쟁하며 시장 점유율을 꾸준히 높임



- 제2차 브라우저 전쟁
  - MS vs Google
  - 2008년 Google 에서 Chrome(이하 크롬) 브라우저 발표
  - 2011년 3년 만에 크롬이 파이어폭스 점유율 돌파하고, 2012년부터 전 세계 점유율 1위
  - 크롬의 성공 요인: 압도적인 속도, 강력한 개발자 도구 제공, 웹 표준



- 파편화와 표준화
  - 1차 브라우저 전쟁 이후 수많은 브라우저에서 자체 자바스크립트 언어를 사용하게 됨
  - 결국 서로 다른 자바스크립트가 만들어지면서 크로스 브라우징 이슈가 발생했고 웹 표준의 필요성이 제기
  - 크로스 브라우징(Cross Browsing)
    - W3C에서 채택된 표준 웹 기술을 채용하여 각각의 브라우저마다 다르게 구현되는 기술을 비슷하게 만들되, 어느 한쪽에도 치우치지 않도록 웹 페이지를 제작하는 방법론 (동일성이 아닌 동등성)
    - 브라우저마다 렌더링에 사용하는 엔진이 다르기 때문
  - 1996년부터 넷스케이프에서 표준 제정의 필요성을 주장
    - ECMA 인터네셔널(정보와 통신 시스템을 위한 국제적 표준화 기구)에 표준 제정 요청
  - 1997년 ECMAScript 1 (ES1) 탄생
  - 제1차 브라우저 전쟁 이후 제기된 언어의 파편화를 해결하기 위해 각 브라우저 회사와 재단은 표준화에 더욱 적극적으로 힘을 모으기 시작



- JavaScript ES6+
  - 2015년 ES2015 (ES6, 에크마스크립트6) 탄생
    - JavaScript 의 가장 현대적인 문법을 확인할 수 있음
    - JavaScript 의 고질적인 문제들을 해결
    - JavaScript 의 다음 시대라고 불릴 정도로 많은 혁신과 변화를 맞이한 버전
    - 이 때부터 출시 연도를 붙이는 것이 공식 명칭이지만, 통상적으로 ES6라 부름
    - 2022년 현재 표준의 대부분이 ES6+로 넘어옴



- Vanilla JavaScript 
  - 아이스크림의 기본이 바닐라인 것처럼, jQuery 같은 라이브러리 쓰지 말고 그냥 JavaScript 쓰자고 독려하는 밈
  - 크로스 브라우징, 간편한 활용 등을 위해 많은 라이브러리 등장(jQuery)
    - ES6 이후, 다양한 도구의 등장으로 순수 JavaScript 활용 증대

  - 수업에선 안다루지만, FE 업무를 수행하려면  **Node.js** 필수적으로 공부해야 함
    - Node.js 는 JavaScript 를 작성 언어로 활용하며, 웹 브라우저에서만 실행되던 JavaScript 가 서버(ex. 로컬의 윈도우OS)에서 실행될 수 있도록 돕는 소프트웨어 개발 플랫폼
    - Node.js 는 JavaScript 에 런타임(환경)을 제공해주는 도구(=JS를 실행할 수 있는 환경)
    - 파이썬 pip 처럼, Node.js 도 npm 이라는 오픈소스 패키지(모듈)가 있음
    - 이번 수업에서는 JavaScript가 브라우저에서 작동하는 수준까지만 배울 예정



---



## 3. DOM(Document Object Model)

> JavaScript 의 활용에 대해 학습하는 파트



- 브라우저에서 할 수 있는 일

  - DOM 조작
    - 문서(HTML) 조작


  - BOM 조작
    - navigator, screen, location, frames, history, XHR


  - JavaScript Core (ECMAScript)
    - JavaScript 핵심 문법을 의미
    - Data Structure(Object, Array), Conditional Expression, Iteration




- DOM 이란?
  - HTML, XML과 같은 문서를 다루기 위한 문서 프로그래밍 인터페이스
  - 문서를 구조화하고 구조화된 구성 요소를 하나의 객체로 취급하여 다루는 논리적 트리 모델
  - 문서가 구조화되어 있으며 각 요소는 객체(object) 취급
  - 단순한 속성 접근, 메서드 활용뿐만 아니라 프로그래밍 언어적 특성을 활용한 조작 가능
  - 주요 객체
    - window: DOM을 표현하는 창. 가장 최상위 객체 (작성 시 생략 가능)
    - document: 페이지 컨텐츠의 Entry Point 역할을 하며, `<body>` 등과 같은 수많은 다른 요소들을 포함
    - navigator, location, history, screen



- DOM - 해석
  - 파싱(Pasing)
    - 구문 분석, 해석
    - 브라우저가 문자열을 해석하여 DOM Tree로 만드는 과정



- BOM 이란?
  - Browser Object Model
  - 자바스크립트가 브라우저와 소통하기 위한 모델
  - 브라우저의 창이나 프레임을 추상화해서 프로그래밍적으로 제어할 수 있도록 제공하는 수단
    - 버튼, URL 입력창, 타이틀 바 등 브라우저 윈도우 및 웹 페이지 일부분을 제어 가능
  - window 객체는 모든 브라우저로부터 지원받으며 브라우저의 창(window)을 지칭



- BOM 조작

  - 개발자도구 Consol 창에서 아래 내용을 입력하며 브라우저를 조작

  ```javascript
  // 탭 창
  > window.open()
  
  // 인쇄 창
  > window.print()
  
  // 메세지 및 확인, 취소 버튼이 있는 대화상자 창
  > window.confirm()
  
  // document도 브라우저 내에 종속되어 있기 때문에 window 전역 객체에 포함
  > window.document
  // 이 경우 작성된 HTML 문서가 반환됨
  ```



- JavaScript Core

  - 위에서 언급되었듯, 프로그래밍 언어가 갖는 다양한 특징을 공유
  - 아래는 개발자도구 Consol 창에 JavaScript 로 작성된 반복문의 예시

  ```javascript
  > const numbers = [1, 2, 3, 4, 5]
  
  > for (let i=0; i < numbers.lenth; i++) {
      console.log(numbers[i])
  }
  
  // 위의 경우 아래와 같은 결과가 반환됨
  // 1
  // 2
  // 3
  // 4
  // 5
  ```

  

- DOM (`document`) ⊂ BOM (`window`) ⊂ ECMAScript

```html
💡 브라우저(BOM)과 그 내부의 문서(DOM)를 조작하기 위해 ECMAScript(JS)를 학습!
```



---



## 4. DOM 조작

> 매서드가 너무 많으니 다 기억할 필요는 없고 그때그때 적절히 활용하자



- DOM 조작 - 개념
  - Document 는 문서 한 장(HTML)에 해당하고 이를 조작
    - 이미지 자료 참조 [(link)](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Manipulating_documents)
  - DOM 조작 순서
    1. 선택 (Select)
    2. 변경 (Manipulation)



- DOM 객체의 상속 구조

  > 💡 참고자료 [(link)](https://developer.mozilla.org/ko/docs/Web/API/EventTarget)

  - HTMLElement ⊂ Document ⊂ Element ⊂ Node ⊂ EventTarget
  - EventTarget
    - Event Listener 를 가질 수 있는 객체가 구현하는 DOM 인터페이스
  - Node
    - 여러 DOM 타입들이 상속하는 인터페이스
  - Element
    - Document 안의 모든 객체가 상속하는 가장 범용적인 인터페이스
    - 부모인 Node 와 그 부모인 EventTarget 의 속성을 상속
  - Document
    - 브라우저가 불러온 웹 페이지를 나타냄
    - DOM 트리의 진입점(entry point) 역할을 수행
  - HTMLElement
    - 모든 종류의 HTML 요소
    - 부모 element의 속성 상속



- `01_js.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
    
    <!-- JS 코드를 작성하는 영역 -->
    <script>
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
  	</script>
</body>
</html>
```



- 위 코드에서 보이듯 JavaScript 는 변수를 선언할 때 아래 3가지 키워드가 필요

  - `var` : 변수를 선언. 추가로 동시에 값을 초기화. ES6+ 이전 문법!

  - `const` : 블록 스코프 읽기 전용 상수를 선언. 변경 불가능. 수업에서는 값을 바꿀 일이 없어서 `const` 계속 쓸 예정

  - `let` : 블록 스코프 지역 변수를 선언. 추가로 동시에 값을 초기화. 변경 가능(반복문에서는 `const` 보다 `let` 많이 씀)




- DOM 선택 - 선택 관련 메서드(1/2) [(link)](https://developer.mozilla.org/ko/docs/Web/API/Document#methods)
  - `document.querySelector(selector)`
    - 제공한 선택자와 일치하는 element 하나 선택
    - 제공한 CSS selector 를 만족하는 첫 번째 element 객체를 반환 (없다면 null)
  - `document.querySelectorAll(selector)`
    - 제공한 선택자와 일치하는 여러 element 를 선택
    - 매칭할 하나 이상의 셀렉터를 포함하는 유효한 CSS selector 를 인자(문자열)로 받음
    - 지정된 셀렉터에 일치하는 NodeList 를 반환



- DOM 선택 - 선택 관련 매서드(2/2) [(link)](https://developer.mozilla.org/ko/docs/Web/API/Document#methods)
  - `getElementById(id)`
  - `getElementsByTagName(name)`
  - `getElementsByClassName(names)`



- `querySelector()`, `querySelectorAll()` 을 사용하는 이유?
  - id, class 그리고 tag 선택자 등을 모두 사용 가능하고, 더 구체적이고 유연하게 선택 가능
    - ex) `document.querySelector('#id')` ◀️▶️`document.querySelectAll('.class')`



- DOM 선택 - 선택 메서드별 반환 타입
  1. 단일 element
     - 👍`querySelector()`
     - 👎`getElementById()`
  2. HTMLCollection
     - 👎`getElementsByTagName()`
     - 👎`getElementsByClassName()`
  3. NodeList
     - 👍`querySelectorAll()` 



- DOM 선택 - HTMLCollection & NodeList
  - 둘 다 배열과 같이 각 항목에 접근하기 위한 index를 제공 (유사 배열)
  - HTMLCollection
    - name, id, index 속성으로 각 항목에 접근 가능
  - NodeList
    - index로만 각 항목에 접근 가능
    - 단, HTMLCollection 과 달리 배열에서 사용하는 `forEach` 메서드 및 다양한 메서드 사용
  - 둘 다 Live Collection 으로 DOM의 변경사항을 실시간으로 반영하지만, **`querySelectorAll()`  으로 반환되는 NodeList는 Static Collection으로 실시간 반영되지 않음**



- DOM 선택 - Collection
  - Live Collection
    - 문서가 바뀔 때 실시간으로 업데이트 됨
    - DOM 변경사항을 실시간으로 collection 에 반영
    - ex) HTMLCollection, NodeList
  - Static Collection (non-live)
    - DOM 이 변경되어도 collection 내용에 영향을 주지 않음
    - `querySelectorAll()`의 반환 NodeList만 static collection



- `02_select.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1 id="title">JS 기초</h1>
  <h2>DOM 조작</h2>
  <p class="text">querySelector</p>
  <p class="text">querySelectorAll</p>

  <script>
    // 선택자를 활용해 선택할 때 
    // 하나를 선택한다. => querySelector
    // 모든 결과를 선택한다. => querySelectorAll

    console.log(document.querySelector('#title'))
    // <h1 id="title">JS 기초</h1>
    console.log(document.querySelectorAll('.text'))
    // NodeList(2) [p.text, p.text]
    console.log(document.querySelector('.text'))
    // <p class="text">querySelector</p>
  </script>
</body>
</html>
```



- DOM 변경 - 변경 관련 메서드 (Creation) [(link)](https://developer.mozilla.org/ko/docs/Web/API/Document#methods)
  - `document.createElement()`
    - 작성한 태그 명의 HTML 요소를 생성하여 반환



- DOM 변경 - 변경 관련 메서드 (append DOM) [(link)](https://developer.mozilla.org/ko/docs/Web/API/Document#methods)
  - `Element.append()`
    - 특정 부모 Node의 자식 NodeList 중 마지막 자식 다음에 Node 객체나 DOMString  삽입
    - 여러 개의 Node 객체, DOMString 을 추가할 수 있음
    - 반환 값이 없음
  - `Node.appendChild()`
    - 한 Node 를 특정 부모 Node 의 자식 NodeList 중 마지막 자식으로 삽입 (Node만 추가 가능)
    - 한번에 오직 하나의 Node만 추가할 수 있음
    - 만약 주어진 Node가 이미 문서에 존재하는 다른 Node를 참조한다면 새로운 위치로 이동



- `ParentNode.append()` ◀️▶️ `Node.appendChild()`
  - append()를 사용하면 DOMString 객체를 추가할 수도 있지만, appendChild()는 Node 객체만 허용
  - append()는 반환 값이 없지만, appendChild()는 추가된 Node 객체를 반환
  - append()는 여러 Node 객체와 문자열을 추가할 수 있지만, appendChild() 는 하나의 Node 객체만 추가할 수 있음



- DOM 변경 - 변경 관련 속성 (property) [(link)](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/innerText) [(link2)](https://developer.mozilla.org/ko/docs/Web/API/Element/innerHTML)
  - `Node.innerText`
    - Node 객체와 그 자손의 텍스트 컨텐츠(DOMString)를 표현 (해당 요소 내부의 raw text)
      - 사람이 읽을 수 있는 요소만 남김
    - 줄 바꿈을 인식하고 숨겨진 내용을 무시하는 등 최종적으로 스타일링이 적용된 모습으로 표현
  - `Element.innerHTML`
    - 요소(element) 내에 포함된 HTML 마크업을 반환
    - [주의] XSS 공격에 취약하므로 사용 시 유의해야 함
      - XSS (Cross-site Scripting) 이란?
        - 공격자가 입력요소를 사용하여 웹 사이트 클라이언트 측 코드에 악성 스크립트를 삽입해 공격하는 방법
        - 피해자(사용자)의 브라우저가 악성 스크립트를 실행하며 공격자가 엑세스 제어를 우회하고 사용자를 가장할 수 있도록 함



- DOM 삭제 - 삭제 관련 메서드 [(link)](https://developer.mozilla.org/en-US/docs/Web/API/Node/removeChild)
  - `ChildNode.remove()`
    - Node가 속한 트리에서 해당 Node를 제거
  - `Node.removeChild()`
    - DOM에서 자식 Node를 제거하고 제거된 Node를 반환
    - Node는 인자로 들어가는 자식 Node의 부모 Node



- DOM 속성 - 속성 관련 메서드
  - `Element.setAttribute(name, value)`
    - 지정된 요소의 값을 설정
    - 속성이 이미 존재하면 값을 갱신, 존재하지 않으면 지정된 이름과 값으로 새 속성을 추가
  - `Element.getAttribute(attributeName)`
    - 해당 요소의 지정된 값(문자열)을 반환
    - 인자(attributeName)는 값을 얻고자 하는 속성의 이름



- `03_attribute.html`

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
      .red { 
        color: red;
      }
      .blue {
        color: blue;
      }
    </style>
  </head>
  <body>
    <h1 class="red text-center my-5">안녕하세요</h1>
    <script>
      // a tag 조작
      const a = document.createElement('a')
      a.innerText = '실라버스'
      const body = document.querySelector('body')
      body.appendChild(a)
      a.setAttribute('href', 'https://syllaverse.com')
      console.log(a.getAttribute('href'))
  
      // h1 tag 조작 (클래스)
      const h1 = document.querySelector('h1')
      console.log(h1.classList)
    </script>
  </body>
  </html>
  ```

  

- DOM 조작 - 총 정리

  | 1. 선택한다.         | 2. 변경(조작)한다.    |
  | -------------------- | --------------------- |
  | `querySelector()`    | `innerText`           |
  | `querySelectorAll()` | `innerHTML`           |
  | ...                  | `element.style.color` |
  |                      | `setattribute()`      |
  |                      | `getattribute()`      |
  |                      | `createElement()`     |
  |                      | `appendChild()`       |
  |                      | ...                   |

  

- `04_event.html` (추가 학습하기)

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
    <h1>이건 복습말고 느낌만..</h1>
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

  
