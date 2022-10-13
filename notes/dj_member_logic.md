# ✅Django 회원관리 서비스 이해

> 1. HTTP & 쿠키(Cookie)
>2. 로그인(Login)
> 3. Authentication with User
>4. 로그아웃(Logout)
> 5. Limiting access to logged-in users
> 6. 회원정보 수정
> 7. 회원탈퇴
> 8. 기타
> 9. Q&A



## 9. Q&A

지난주 : ModelForm 활용한 Article CRUD

- **ModelForm 은 DB 와 관련됨**

이번주 : User CRUD [다른 CRUD와 다른 점은 '인증', '비밀번호 암호화']

- 이 과정에서 Django Auth (django.contrib.auth) 활용

  - 인증(로그인) 👈 AbstractUser 클래스 상속받아 활용

  - 비밀번호 암호화 👈 Form 활용 
    - ModelForm : UserCreationForm (ex. 비밀번호 2개 체크)
    - 그냥 Form : Authenrication Form (ex. 인증/완료되면 user 객체)



특히 어제 공부한 로그인 핵심 개념은

- HTTP

  - connectionless : 응답하면 끝

  - stateless : 

- 로그인 : 어떤 사이트에 한 번 로그인 하면, 나의 인증 정보가 그 사이트에 박혀 있다고 생각하면 됨
  - 쿠키 : HTTP 상에서 상태를 관리할 수 있는 도구. 한 번에 연결되었던 사람이 있으면, 서버가 브라우저에 응답하면서 쿠키를 던져놓음. 그래서 다음에 또 같은 사람이 로그인하면 서버가 쿠키 정보를 보면서 로그인 했던 사람이라고 판단하는 것
  - 세션 : 범 CS 에서 많이 사용되는 용어. 연결되어 있다는 하나의 상태라고 이해하기. Django 는 DB 에 세션 정보를 저장하는 방식
  - 쿠키는 클라이언트가 요청을 보내면 응답할 때 같이 보내주는건데 이 쿠키 안에 session id가 저장되어 전달 되고 서버에서는 이 세션 아이디가 같은지를 확인하는 것



Q : 쿠키와 세션의 차이? 궁금합니다

A : 쿠키와 세션에 대한 위 설명을 보고 스스로 정리해보기



Q : 어제 실습 localhost:8000를 로그인에 따라 다르게 출력하라고해서(로그인하면 username 출력, username 누르면 해당 회원 조회), base.html 에 navbar 넣고, navbar 에 .is_authenticated 분기해서 로그인 하면 {{ user }} 혹은 {{ user.username }} 이 출력되게 작성했는데요! 요렇게만 작성하면 회원목록 타고 다른 회원의 detail.html 페이지 들어갔을때 navbar {{ user.username }} 부분이 로그인한 회원 이름이 아닌 detail.html 페이지에 설명되고 있는 다른 회원 이름으로 출력되는 이슈가 계속 발생하더라고요 {{ request.user.username }} 로 고치니까 해결됐습니다 이 미묘한 차이는 왜 발생하는 걸까요?

A : context 에서 전달되고 있는 user 라고 하는 것이 있었기 때문일 거에요. 그러니까 요청한 유저인 경우 request.user 쓰시면 좋을 것 같습니다



Q : 게시글을 작성한 계정만 글을 수정하고 삭제할 수 있게 할 수 있을까요?

A : 게시글에 User PK 를 저장해야 합니다. 예를 들면 {% if request.user == article.user %} 삭제 수정 버튼 보여줄게 {% endif %} ... 다음 주에 자세히 수업!



Q : username 클릭 시 해당 회원 조회 페이지(프로필 페이지)로 이동이 안되더라고요... for _ in accounts로 새로 구현 하는게 아닌가요?

A : detail 페이지를 구현하는 것이죠. /accounts/1



Q : 기존에 게시판 db가 있는 상태에서 accounts 를 만들면서 기존 db 날리고 다시 makemigrations랑 migrate해서 db를 만드는데요. 기존에 게시판 생성하면서 db 만들어 놓은 상태에서 accounts 만들 때 그냥 db를 생성 할 수 있나 궁금했습니다 => DB를 두 개로 관리 할 수 있나요?

A : https://www.youtube.com/watch?v=BnS6343GTkY 영상 한번씩 보기
