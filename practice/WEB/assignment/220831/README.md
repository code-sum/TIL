# CSS 학습

> 💡참고자료
>
> - Learn CSS [(link)](https://web.dev/learn/css/)
> - MDN > 개발자를 위한 웹 기술 > flexbox의 기본 개념 [(link)](https://developer.mozilla.org/ko/docs/Web/CSS/CSS_Flexible_Box_Layout/Basic_Concepts_of_Flexbox)
> - MDN > Web 개발 학습하기 > Flexbox [(link)](https://developer.mozilla.org/ko/docs/Learn/CSS/CSS_layout/Flexbox#%EC%99%9C_flexbox%EC%9D%B8%EA%B0%80)



## 1. Box Model

- CSS가 표현하는 모든 것은 Box
- `border-radius` 를 활용해서 원처럼 보이는 박스를 만들거나, 텍스트만 적혀있는 경우일지라도 모두 네모난 Box
- Box Model 영역 (개발자도구 참조)
  1. Content box: 내용
  2. Padding box
  3. Border box: 테두리
  4. Margin box



## 2. Selectors

- CSS를 적용하기 위해서는 특정 마크업을 '선택' 해야함

- Selectors 유형

  1. 범용 선택자(=와일드카드): 모든 요소와 일치

     ```css
     * {
         color: blue;
     }
     ```

  2. 단순 선택자: HTML 요소, HTML 태그에 추가할 수 있는 id, 클래스, 기타 속성 (가급적이면 클래스 선택자 활용할 것)

     - 클래스 선택자

       ```css
       .my-class {
           color: red;
       }
       ```

       ```html
       <div class="my-class"></div>
       <button class="my-class"></button>
       <p class="my-class"></p>
       ```

     - id 선택자

       ```css
       #sun {
         border: 1px solid yellow;
       }
       ```

       ```html
       <div id="sun"></div>
       ```

       

## 3. Layout

- 웹 초기와 달리, 현대 CSS는 편리하고 효과적인 레이아웃 도구들 등장

- CSS layout over time

  | 1996   | 1998 | 2010                  | 2012          | 2017 | 2019                 | 2021              |
  | ------ | ---- | --------------------- | ------------- | ---- | -------------------- | ----------------- |
  | CSS1   | CSS2 | CSS3                  | Media Queries | Grid | Intrinsic Web Design | Container Queries |
  | Floats |      | Responsive Web Design | Flexbox       |      |                      |                   |

  

## 4. Flexbox

#### 4.1. What is flexbox in CSS?

- 인터페이스 내 아이템 간 공간 배분, 정렬을 위해 설계된 모듈

  ```css
  .flex-container {
      display: flex;
  }
  ```

- flexbox 내 2개의 축

  - 주축: `flex-direction` 속성을 이용해 지정, 아래 4개 값을 가짐
    - `row` : 주축은 인라인 방향으로 행을 따름 (왼-오)
    - `row-reverse` : 주축은 인라인 방향으로 행을 따름 (오-왼)
    - `column` : 주축은 페이지 상단에서 하단으로 블록 방향을 따름
    - `column-reverse` : 주축은 페이지 상단에서 하단으로 블록 방향을 따름
  - 교차축: 주축에 수직인 축

- **flex 컨테이너**에 지정할 수 있는 속성

  - `flex-direction` : 배치 설정
  - `align-items` : 교차축을 따라 flex 항목 열을 정렬하는 방식
  - `justify-content` : 주축을 따라 flex 항목 행을 정렬하는 방식, 공간 나누기

  ```css
  .item-container {
    display: flex;
    height: 500px;
    flex-direction: row;
    align-items: center;
    justify-content: center;
  }
  
  .card {
    width: 100px;
    height: 200px;
    border: 1px solid black;
    margin: 1rem;
  }
  ```

- **flex 항목**에 지정할 수 있는 속성

  - `flex-grow` : 첫 항목의 `flex-grow` 값을 2로, 나머지 두 개 항목을 1로 지정한다면 각 항목에 지정된 `flex-grow` 비율인 2:1:1 에 따라 픽셀 분배

  ```css
  .main {
    display: flex;
    height: 500px;
  }
  
  .section {
    background-color: beige;
  }
  
  .section1 {
    flex-grow: 1;
  }
  
  .section2 {
    flex-grow: 4;
  }
  
  .section3 {
    flex-grow: 1;
  }
  ```

  

#### 4.2. Why flexbox?

- flexbox 가 필요한 레이아웃 사례들

  ```
  1. 수직 정렬
  2. 아이템 너비 or 높이 or 간격 동일하게 배치하고 싶을 때
  ```

  - 부모 요소 내부에 포함된 블록 컨텐츠를 세로로 중심부에 맞추고 싶을 때
  - 사용 가능한 `width`, `height` 와 무관하게, 특정 컨테이너에 포함된 모든 자녀 요소가 주어진 `width`, `height`를 똑같은 크기로 점유해야할 때
  - 다단 레이아웃에 포함된 모든 단이 서로 다른 크기의 컨텐츠를 포함하고 있더라도 동일한 높이로 채택하고 싶을 때