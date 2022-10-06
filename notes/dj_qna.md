# ✅ Django Q&A

> 최신 형태의 게시판을 참조하고 싶다면?
>
> 이오플래닛, 서핏, 디스콰이엇, 인살롱, 퍼블리(Q&A), 블라인드(detail page) 참조하는 것을 추천합니다.
>
> 💡 [VSCODE 에서 Django 템플릿 오토포매팅](https://velog.io/@junsikchoi/VSCode%EC%97%90%EC%84%9C-Django-%ED%85%9C%ED%94%8C%EB%A6%BF-%EC%98%A4%ED%86%A0-%ED%8F%AC%EB%A7%A4%ED%8C%85%ED%95%98%EA%B8%B0)



### 1. Django 근본적인 질문

Q : 서비스가 커지면 장고로 서비스하기 어렵다고 들었습니다. (동적 언어 한계 상) 장고의 커버리지는 어느 정도 일까요?

A : 여러분이 지금하고 있는 웹 개발은 그림 그릴 때 데생 작업 수준입니다. 그러니까 실무에서 장고로 서비스하기 어렵다고 너무 걱정할 필요는 없습니다. 지금 수업에서 배운 기술 스택/상황/서비스방식/버전이 실무에서는 천차만별로 다르고, 어차피 회사가면 새로운 언어를 배우게 될 수 있습니다. 국내 기술 생태계 다수는 Java 인데, 개발자 20명 가량되는 회사에서 Python 을 쓰다가 CTO가 바뀌면서 기술 스택이 또 달라질 수 있습니다. 즉 배워야할 기술은 계속 변하므로 절대적인 기준이 있는 건 아닙니다.



Q : 실제 장고로 백엔드 업무를 하게되면 꾸미는 건 아예 안하는거 아닌가요?

A : 우리 수업에서는 Django 서버에서 클라이언트에게 HTML 을 보여주기만 하고 있는데, 실제 현업에서는 서버에서 클라이언트에게 JSON 을 던져주고(=서버 사이드 렌더링) 그 다음 클라이언트 사이드 렌더링 단계로 넘어가면 JS 이용해서 최종 HTML 만들어야 합니다. (이때 쓰는 게 뷰, 리액트)



### 2. 개념 및 활용

Q : 모델폼을 사용하지 않고도 (폼을) 만들 수 있는데, 모델폼 사용하면 더 복잡해지는 느낌입니다. 모델폼 사용하면 더 간략해져서 사용하는 건가요?

A : 모델폼을 안쓰면 기능적으로는 HTML 일일이 작성하고, 유효성 검사를 위한 코드를 길게 작성해야 합니다. 반대로 모델폼을 활용하면 다양한 기능을 편하게 쓸 수 있습니다. 이게 바로 클래스 객체의 역할이기도 합니다. 또한 모델폼을 쓰면 기술적인 이슈가 발생했을 때 화면의 HTML 을 직접 고치는 것이 아니라, "모델폼을 고쳐야겠다" 하고 생각하면서 추상화된 Python 코드로 돌아가서 내포된 기능들을 고치면 되는 것입니다. 향후 커스텀이 필요한 시점이 올텐데, 그때는 한번씩 커스텀을 시작하면 되고, 지금은 우선 모델폼을 써먹읍시다. (참고 : 2017년 카카오 공채 필기 마지막 문제가 MVC 패턴이었습니다)

요약 : ModelForm : 기능(Class) (1) HTML Form <-> Model (2) Validation



Q : Django 부트스트랩 패키지 활용하는 것보다, base.html 에 부트스트랩 CDN 넣는게 더 편한거 같은데 Django 부트스트랩 패키지를 알려주신 이유가 있나요?

A : ModelForm 기능에 부트스트랩 스타일링을 자동으로 해주기 때문입니다(기능 + 스타일링) 즉 `{% Bootstrap_form form %}` 코드를 넣으면 내가 작성했던 기본 HTML Form 이 기능성도 가지면서 예쁘게 스타일링 되기 때문입니다. 그럼에도 불구하고 Form 을 개별적으로 커스텀 하고 싶은 분들은 Django 공식문서에서 DTL 반복문이나 위젯 활용한 방법들을 참고해 보세요.



### 3. 기능

Q : ModelForm, admin, model 왜 이렇게 클래스를 정의하는 경우가 많죠?

A : 기본 기능을 상속 받아서, 처음에 커스텀 설정을 하고 이걸 그대로 사용, 나도 사용, Django 도 사용하는 것입니다. 즉, 핵심은 요청 처리하는 것입니다. 지금 View 를 Function 으로 정의하고 있죠? FBV(Function based view) / CBV(Class based view) 중에 FBV 로 수업하고 있는건데 구글링해보면 View 까지 Class 로 정의하는 세계도 있습니다. 



Q : import 이해가 잘 안됩니다

A : 기본적으로 import 는 내가 필요할 때 가져와서 쓰는 것입니다. 인텔리제이 써보시면 import 가 따라와서 붙긴 합니다. import 이해가 잘 안된다면, 머릿속에 일단 폴더를 상상해 보세요. 우리가 django 라는 패키지를 쓰고 있는 거니까 Github 에서 django/django 들어가보면 여러 폴더 안에 ModelForm 이 클래스로 정의되어 있다는 것도 확인할 수 있습니다. 이런 폴더에서 내가 필요한 것을 꺼낸다고 생각하면 import 이해가 쉽습니다. (엄밀한 표현은 폴더가 아니라 모듈이긴 합니다)

https://github.com/django/django



Q : django 내장모듈 import 하면서 쓰고 있는게 함수인지 클래스인지 구분 못하겠어요

A : CamelCase 는 클래스, snake_case 는 함수라고 생각하면 편합니다. ModelAdmin 도 클래스, render, redirect 도 함수입니다. Python 의 규칙입니다.



Q : 글 작성 form 과 수정 form 이 비슷한 것 같은데 혹시 하나로 합쳐 하나의 html 로 구현할 수 있을까요?

A : new.html / update.html 2개를 form.html 로 바꾸고 2개 함수의 경로를 form.html 로 넘어오게 만들면 가능합니다. 이러면 각 페이지의 타이틀도 <글 생성하기>, <글 수정하기> 로 바뀌도록 기능 구현해야 합니다. 템플릿에서 쓸 수 있는 변수/값은 context 이기 때문에 view 에서 context 로 어떤 값을 넘겨서 처리하는 방법이 하나. 이거랑 다른 방법으로 해결하고 싶다면 settings.py 에서 `TEMPLATES = []` 괄호 내 값들 공부하고 (선생님이 TEMPLATES 에 달아놓은 주석 참고) 템플릿에 `{{ request.path }}` `{{ request.GET }}` 넣고, django request object 가 무슨 역할하는지 검색해봅니다. 템플릿에서 if 문 짜서 path 에 따라 다른 글자 보이도록 설계할 수 있습니다. 공식문서에서 resolver_match  읽어보고 템플릿에 `{{ request.resolver_match.url_name }}` 활용하면 if 문 짜기가 더 쉬워집니다.



Q : 어제 created_at 을 DB에 저장해서 html 로 끌고 왔을 때 2022년10월4일14시26분23초 이런 식으로 나오던데 날짜 형식을 직접 바꿀 수는 없을까요?

A : 이건 우리가 알고 있는 MTV 역할 중에서 T 가 하는 일입니다. 따라서 구글에 django template datetime format 검색해서 공식문서 보면 T 단에서 해결할 수 있는 다양한 코드를 알려줍니다. django template ago filter 검색해보면 "몇시간전" 같은 표시 형식도 넣을 수 있습니다. 표시 형식을 바꾸는 작업은 Django Template Filter `{|___}`, 추가적인 문법을 도와주는 것은 Django Template Tag `{%  %}` 입니다.

https://docs.djangoproject.com/en/4.1/ref/templates/builtins/



Q : `{% load ~ %}` 와 `{% extends ~ %}` 중에 더 상단에 작성해야 하는 코드는 무엇인가요?

A : 모든 템플릿의 가장 최상단에는 `{% extends ~ %}` 가 있어야 합니다. django template extends 검색해보면 공식문서에 템플릿 상속과 관련된 상세 내용이 설명되어 있습니다. 블록도 조각 조각내서 상속을 받을 수 있습니다.



Q : base.html 에 `{% load static %}` 을 써줬는데 index.html 에서 안먹히더라고요. 그래서 index.html 에도 `{% load static %}` 을 또 써주니까 되더라고요. load 를 따로 써줘야하는 이유가 궁금합니다.

A : Django Template 에서 load 는 파이썬의 import 처럼 생각해주세요. 그래서 load 가 필요한 템플릿이 여러 개 있다면, 각각 하나씩 모두 load 해줘야 합니다.



Q : path 지정할 때 `<int:pk>/delete/` 이 path를 `delete/<int:pk>/` 이런식으로 순서를 바꿔도 상관은 없나요?

A : 순서 바꿔도 상관은 없습니다. 그치만 url 만드는 방식이라고 이해하시면 됩니다. 특정 글을 삭제한다는 의미에 있어서 `<int:pk>/delete/` 가 조금 더 명시적이기 때문에 수업에서 이렇게 작성하는 것입니다.