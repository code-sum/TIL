CRUD



오늘 배운 내용을 잘 써먹으면 유튜브, 인스타그램 만들기에 활용할 수 있습니다.

어제는 URL 을 앱별로 각각 만들었고, 이 과정에서 include 를 활용했습니다(App URL mapping)



# Namespace

어제 배운 내용을 종합해보면 앱(기능)별로 각기 다른 공간(페이지)을 갖게 됨

이렇게 다른 공간을 만들고, 그 공간에 이름을 붙여주는걸 Namespace

예) https://www.youtube.com/gaming 에서 도메인이름 + /gaming



- 개요
  - 개체를 구분할 수 있는 범위



- Namespace 의 필요성

  - 페이지마다 여러가지 기능 붙임

  - 코드들의 변경을 최소화하면 유지보수할 때 좋은데, 이렇게 코드 변경 최소화하기 위한 방법 중에 하나가 바로 이런 변수화 잘하기!

  - `<a>` 태그 안에 `{% url 'greeting' %}` 들어가 있는 점이 새로우니까 어제 작업하던 프로젝트 폴더(담벼락 만들기)에서 직접 적용해봅니다 (=DTL)

  - 어제 작성한 create.html 에서 작업할텐데, url 에 이름 붙이기(=path 안에 name 작성) 먼저 해야됩니다

    ```python
    # atricles - urls.py
    
    from django.urls import path
    from . import views
    
    urlpatterns = [
        path('', views.index, name='index')
        path('create/', views.create, name='create')
    ]
    ```

  - 다시 create.html 로 돌아가서 아래와 같이 수정

    ```html
    {% extends 'base.html' %}
    
    {% block content %}
    <h1>작성완료</h1>
    <p>작성 내용: {{ content }}</p>
    <a href="{% url 'index' %}">방명록으로 돌아가기</a>
    
    {% endblock %}
    ```

  - 어제 만든 index.html 에서도 아래 부분으로 수정

    ```html
    <body>
        <div>
            <h1>방명록</h1>
        </div>
        <div>
            <h2>글 목록</h2>
            {% for content in guestbook %}
            <p>{{ content.content }}</p>
            {% endfor %}
        </div>
        <div>
            <h2>글 작성</h2>
            <form action="{% url 'create' %}" method="GET">
                <input type="text" name="content">
                <input type="submit">
            </form>
        </div>
    </body>   
        
    {% endblock %}
    ```

  - Namespace 만들 때 문제가 될 수 있는 부분은, practices 에도 index 가 있고, articles 에도 index 가 있기 때문에 두 앱에 같은 name 을 활용했을 때 엉킴 (이거 해결하는게 하단에서 설명한 URL namespace)



- URL namespace

  - 위에서 namespace 만들다가 url 끼리 엉키는 현상이 발생했기 때문에 URL namespace 작업이 필요

  - practices 와 articles 의 urls.py 파일들에 아래와 같은 코드 추가

    ```python
    # atricles - urls.py
    
    from django.urls import path
    from . import views
    
    app_name = 'articles'
    
    urlpatterns = [
        path('', views.index, name='index')
        path('create/', views.create, name='create')
    ]
    ```

  - URL tag의 변화 : index.html 로 돌아가서 DTL url 부분도 아래와 같이 수정

    ```html
    {% extends 'base.html' %}
    
    {% block content %}
    <h1>작성완료</h1>
    <p>작성 내용: {{ content }}</p>
    <a href="{% url 'articles:index' %}">방명록으로 돌아가기</a>
    
    {% endblock %}
    ```

    

- Template namespace
  - 어제 저희가 수업에서 Template 에도 namespace 를 줬었습니다
  - 전역에서 봤을 때 동일한 이름을 가진 애들을, 각기 다른 이름 공간으로 나눠주는 작업을 한 것
  - 이런 namespacing 을 잘해야 유지보수 하기 좋은 서비스를 만들어 나갈 수 있음



- Naming URL patterns
  - [참고] DRY 원칙 ⭐⭐⭐
    - Don't Repeat Yourself
    - 우리가 이 원칙을 처음으로 적용해 봤던 것이 templates 에서 `base.html` ! 여기서 최소한의 변경으로 최대한의 효과를 봤음
    - 면접에서 좋은 코드를 쓰려면 어떻게 써야할까요? 하는 질문이 나왔을 때 [DRY 원칙] 얘기하면 좋습니다
    - 더 품질 좋은 코드를 작성하기 위해서 알고, 따르면 좋은 소프트웨어 원칙들 중 하나로 "소스 코드에서 동일한 코드를 반복하지 말자" 라는 의미
    - 동일한 코드가 반복된다는 것은 잠재적인 버그의 위협을 증가 시키고 반복되는 코드를 변경해야 하는 경우, 반복되는 모든 코드를 찾아서 수정해야 함
    - 이는 프로젝트 규모가 커질수록 애플리케이션의 유지 보수 비용이 커짐
  - 삼성SDS 에 입사하면 승진할 때 아래 3가지 역량이 모두 중요하기 때문에 코드를 잘짜는 원칙을 지키는 것이 중요합니다
    - 알고리즘 역량: A(필수) -> B(pro, 과장급)
    - 코드 리뷰 역량: 클린코드&디자인패턴&TDD(test design pattern) (여기까지 주니어급)
    - 아키텍트 역량: 설계 디자인패턴&설계원칙 (여기는 시니어급)



- 마무리
  - Django의 설계 철학 (Templates System)
    - "표현과 로직(view)을 분리"
      - 템플릿 시스템은 표현을 제어하는 도구이자 표현에 관련된 로직일 뿐
      - 즉, 템플릿 시스템은 이러한 기본 목표를 넘어서는 기능을 지원하지 말아야 함
    - "중복을 배제"
      - 대다수의 동적 웹사이트는 공통 header, footer, navbar 같은 사이트 공통 디자인을 갖음
      - Django 템플릿 시스템은 이러한 요소를 한 곳에 저장하기 쉽게 하여 중복 코드를 없애야 함
      - 템플릿 상속의 기초가 되는 철학



- Framework 의 성격
  - 독선적(Opinionated) : 약속이 많고 고집스러움(Convention over Configuration, CoC 원칙, 설정 보다는 관례)
    - 독선적인 프레임워크들은 어떤 특정 작업을 다루는 '올바른 방법'에 대한 분명한 의견(규약)을 가지고 있음
    - 대체로 특정 문제내에서 빠른 개발방법을 제시
    - 어떤 작업에 대한 올바른 방법이란 보통 잘 알려져 있고 문서화가 잘 되어있기 때문
    - 하지만 주요 상황을 벗어난 문제에 대해서는 그리 유연하지 못한 해결책을 제시할 수 있음
  - 관용적(Unopinionated) : 고수 단계에 쓰면 좋음
    - 관용적 프레임워크들은 구성요소를 한데 붙여서 해결해야 한다거나 심지어 어떤 도구를 써야 한다는 ~



- Django Framework 의 성격
  - '다소 독선적'
    - 양쪽 모두에게 최선의 결과를 준다고 강조
  - 결국 하고자 하는 말은 현대 개발에 있어서는 가장 중요한 것 중에 하나가 '생산성'



---



## Django 구조 이해하기 (MTV Design Pattern)

SW는 무엇을 하는 도구일까요?

핵심은 문제 해결! 인간이 스스로 풀지 못하는 세상의 문제를 해결하게끔 소프트웨어를 이용하는 것인데, 세상의 문제가 너무 복잡하다는 문제가 또 있음

해피해킹이 풀고 싶은 문제는 사람들이 "빠르게" SW 를 배울 수 있게 하는 것이었는데, 이게 쉽지 않아서 [추상화(요약)] 에 집중하고 있음. 복잡한 문제를 요약하는 여러 스킬이 있는데, Django 는 웹사이트 만드는게 복잡해서 이를 단순화, 그리고 이게 너무 커졌을 때 어떻게 관리할지를 풀어주는 프레임워크임(2가지 핵심)



Design Pattern : 패턴은 개발 업계에서 설계를 의미

- Design Patten 이란?
  - 부산의 명물이라는 광안대교, 이러한 다리는 어떻게 만들까?
  - 광안대교 같은 다리를 현수교라고 함
  - 교량의 양쪽 끝과 가운데 솟아있는 주탑에 케이블을 두고 상판을 메다는 형식의 공법
  - 이와 똑같은 방식을 사용해서 인천대교, 이순신대교 등이 만들어졌음
  - 즉, 여러 번 짓다보니 자주 사용되는 구조가 있다는 것을 알게 되고 



- 소프트웨어에서의 관점
  - 각기 다른 기능을 가진 다양한 응용 소프트웨어를 개발할 때 공통적인 설계 문제가 존재하며, 이를 처리하는 



- 소프트웨어 디자인 패턴
  - 소프트웨어도 수십년간 전 세계 개발자들이 계속 만들다 보니 자주 사용되는 구조와 해결책이 있다는 것을 알게 됨
  - 앞서 배웠던 클라이언트-서버 구조도 소프트웨어 디자인 패턴 중 하나



- 소프트웨어 디자인 패턴의 목적
  - 특정 문맥



- 소프트웨어 디자인 패턴의 장점
  - 디자인 패턴을 알고 있다면 서로 복잡한 커뮤니케이션이 매우 간단해짐



- Django 에서의 디자인 패턴
  - Django 에도 이러한 디자인 패턴이 적용되어 있는데



- MVC 소프트웨어 디자인 패턴
  - MVC 는 Model - View - Controller 의 준말
  - 데이터 및 논리 제어를 구현하는데 널리 사용되는 소프트웨어 디자인 패턴
  - 하나의 큰 프로그램을 세가지 역할(관심사)로 구분한 개발 방법론
  - Model : 데이터와 관련된 로직을 관리 (데이터)
  - View : 레이아웃 화면을 처리 (FE 개발자)
  - Controller : 명령을 model과 view 부분으로 연결 (BE 개발자)



- MVC 소프트웨어 디자인 패턴의 목적
  - "관심사 분리" : 각자 잘하는 것만 하자!



- Django 에서의 디자인 패턴

  - Django 는 MVC 패턴을 기반으로 한 MTV 패턴을 사용
  - 두 패턴은 서로 크게 다른 점은 없으며 일부 역할에 대해 부르는 이름이 다름

  | MVC        | MTV      |
  | ---------- | -------- |
  | Model      | Model    |
  | View       | Template |
  | Controller | View     |



- MTV 디자인 패턴
  - Model
    - MVC 패턴에서 Model 의 역할에 해당
    - 데이터와 관련된 로직을 관리
    - 응용프로그램의 데이터 구조를 정의하고 데이터베이스의 기록을 관리
  - Template
    - 레이아웃과 화면을 처리
    - 화면상의 사용자 인터페이스 구조와 레이아웃을 정의
    - MVC 패턴에서의 View
  - View
    - Model & Template 과 관련한 로직을 처리해서 응답을 반환
    - 클라이언트의 요청에 대해 처리를 분기하는 역할
    - MVC 패턴에서 Controller 역할에 해당



- 정리
  - Django 는 MTV 디자인 패턴을 가지고 있음
  - Model : 데이터 관련
  - Template : 화면 관련
  - View : Model & Template 중간 처리 및 응답 반환



---



# ✅ Django Model



## Datebase

- Datebase
  - 체계화된 데이터의 모임
  - 검색 및 구조화 같은 작업을 보다 쉽게 하기 위해



- Database 기본 구조
  1. 스키마
  2. 구조



- 스키마
  - 뼈대(Structure)
  - 데이터베이스에서 자료의 구조, 표현 방법, 관계 등을 정의한 구조



- 테이블(Table)
  - 필드와 레코드를 사용해 조직된(=관계된) 데이터 요소들의 집합
  - 관계(Relation)라고도 부름



## Model

- 개요
  - Django 는 Model 을 통해 데이터에 접근하고 조작
  - 사용하는 데이터들의 필수적인 필드들과 동작들을 포함
  - 저장된 데이터베이스의 구조 (layout)
  - 일반적으로 각각의 모델은 



DB 에 데이터 저장할 수 있도록 python manage.py make migrations 파일을 만드는 것!



## Migrations

- makemigrations
  - 파이썬으로 작성된 설계도



- migrate
  - makemigrations 로 만든 설계도를 실제 데이터베이스에 반영



---



어제 복습 + 실제 게시판 만들기 (수업 후반 1시간 11:00~12:00)

어제 구현 + 담벼락 수정이랑 삭제까지 가능하도록!

CRUD with view



가상환경 켜고 터미널에 python manage.py startapp posts

settings.py 파일 안에 앱등록



메인 urls.py 에 게시판 시작 url 등록

```python
path('posts/', include(posts.urls)),
```



서브 문지기 정의하기(posts 앱 안에 urls.py 생성)

```python
# posts - urls.py

from django.urls import path
from . import views

"""
메인(R) 페이지: 게시글의 목록(/posts/) / 게시글 상세
작성(C) 페이지: 글을 작성하는 페이지 / 작성 완료
수정(U) 페이지: 글을 수정하는 페이지 / 수정 완료
삭제(D) : 글목록이나 상세 페이지에 넣을 기능, 글 삭제 완료
"""

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
]
```



index 함수 정의하러 가기(posts 앱 안에 views.py 생성) 

```python
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
```



posts 안에 templates 폴더 만들고, 그 안에 posts 폴더 만들기

제일 안쪽 폴더(posts)에 index.html 생성

```html
{% extends 'base.html' %}

{% block content %}
<h1>게시판</h1>

<ul>
    <li>제목: 첫글 | 내용: 와와</li>
    <li>제목: 두번째글 | 내용: 예예</li>
</ul>

<a href="{% url 'posts:new' %}">새글쓰기</a>

{% endblock %}
```



urls.py 수정하러 가기

```python
# posts - urls.py

from django.urls import path
from . import views

"""
메인(R) 페이지: 게시글의 목록(/posts/) / 게시글 상세
작성(C) 페이지: 글을 작성하는 페이지 / 작성 완료
수정(U) 페이지: 글을 수정하는 페이지 / 수정 완료
삭제(D) : 글목록이나 상세 페이지에 넣을 기능, 글 삭제 완료
"""

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new')
]
```



다시 views.py 가서

```python
from django.shortcuts import render

def index(request):
    return render(request, 'posts/index.html')

def new(request):
    return render(request, 'posts/new.html')
```



여기까지 하고 python manage.py runserver 하고

localhost:8000/posts/



새글쓰기 페이지 만들어 주러가자~

 index.html 처럼 제일 안쪽 폴더(posts) 안에 새 파일(new.html) 생성

```html
{% extends 'base.html' %}

{% block content %}
<h1>새글 쓰기</h1>
<form action="{% url 'posts:create' %}">
    제목: <input type="text" name="text"><br>
    내용: <input type="text" name="content">
    <input type="submit">
</form>

{% endblock %}
```



localhost:8000/posts/new/ 로 이동해보면

create 가 없다고 에러 뜸



create 설정하기 위해

```python
# posts - urls.py

from django.urls import path
from . import views

"""
메인(R) 페이지: 게시글의 목록(/posts/) / 게시글 상세
작성(C) 페이지: 글을 작성하는 페이지 / 작성 완료
수정(U) 페이지: 글을 수정하는 페이지 / 수정 완료
삭제(D) : 글목록이나 상세 페이지에 넣을 기능, 글 삭제 완료
"""

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new')
    path('create/', views.create, name='create'),
]
```



다시 views.py 가서

```python
from django.shortcuts import render

def index(request):
    return render(request, 'posts/index.html')

def new(request):
    return render(request, 'posts/new.html')

def create(request):
    pass  # 함수의 껍데기만 만들어주는 스킬
```



이 상태에서 localhost:8000/posts 들어가서 제목&내용 쓰고 제출 누르면

제목&내용 넘어갔다는 사실을 주소창 변화를 통해 알 수 있음



DB에 저장하는 로직 만들어주기

```python
from django.shortcuts import render

def index(request):
    return render(request, 'posts/index.html')

def new(request):
    return render(request, 'posts/new.html')

def create(request):
    # DB에 저장
    # parameter 로 날라온 데이터를 받아서
    title = request.GET.get('title')
    content = request.GET.get('content')
    
    context = {
        'title': title,
        'content': content, 
    }
    
    return render(request, 'posts/create.html', context)
```



템플릿 만들어주러 가기 (create.html 만들기)

```html
{% extends 'base.html' %}

{% block content %}
<h1>작성 완료</h1>
<p>제목: {{ title }}</p>
<p>내용: {{ content }}</p>

{% endblock %}
```



여기까지 하고 실제 DB에 저장하러 가기 models.py

```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
```



아래 명령어로 우리가 만든 model 을 django 에 반영해주기

$ python manage.py makemigrations  // 파일을 만들어주고

$ python manage.py migrate   // 실제 DB 에 반영



SQLITE EXPOLER 로 posts_post 생성된거 확인



```python
from django.shortcuts import render
from .models import Post

def index(request):
    return render(request, 'posts/index.html')

def new(request):
    return render(request, 'posts/new.html')

def create(request):
    
    # 1. parameter 로 날라온 데이터를 받아서
    title = request.GET.get('title')
    content = request.GET.get('content')
    
    # 2. DB에 저장
    Post.objects.create(title=title, content=content)
    
    context = {
        'title': title,
        'content': content, 
    }
    
    return render(request, 'posts/create.html', context)
```



여기까지 작업해서

localhost:8000/posts/ 창에서

제목+내용 컨텐츠 작성하고 제출 누르면! 작성완료 뜨고 DB에 저장



목록으로 돌아가는 버튼 만들어주기

```html
{% extends 'base.html' %}

{% block content %}
<h1>작성 완료</h1>
<p>제목: {{ title }}</p>
<p>내용: {{ content }}</p>

<a href="{% url 'posts:index' %}">목록으로</a>

{% endblock %}
```



SQLITE EXPOLER 로 posts_post 에서 작성한 글들이 들어가있는거 확인



views.py 아래와 같이 수정(def index 부분)

```python
from django.shortcuts import render
from .models import Post

def index(request):
    # 모든 글 목록을 보여준다.
    # 1. DB에서 모든 글을 불러온다.
    posts = Post.objects.all()
    # 2. template 에 보내준다.
    context = {
        'posts' : posts,
    }
    
    return render(request, 'posts/index.html', context)

def new(request):
    return render(request, 'posts/new.html')

def create(request):
    
    # 1. parameter 로 날라온 데이터를 받아서
    title = request.GET.get('title')
    content = request.GET.get('content')
    
    # 2. DB에 저장
    Post.objects.create(title=title, content=content)
    
    context = {
        'title': title,
        'content': content, 
    }
    
    return render(request, 'posts/create.html', context)
```



index.html 수정하러가기

```html
{% extends 'base.html' %}

{% block content %}
<h1>게시판</h1>

<ul>
    {% for post in posts %}
    <li>제목: {{ post.title }} | 내용: {{ post.content }}</li>
    {% endfor %}
</ul>

<a href="{% url 'posts:new' %}">새글쓰기</a>

{% endblock %}
```



글 썼을 때 create.html 페이지 대신, 바로 게시판 목록을 보는게 좋을 수 있음

이걸 리다이렉션이라고 함 (새글 쓰기 제출하면 목록으로 바로 넘어가게 만들기)

views.py 최상단&하단 부분 수정

```python
from django.shortcuts import render, redirect
from .models import Post

def index(request):
    # 모든 글 목록을 보여준다.
    # 1. DB에서 모든 글을 불러온다.
    posts = Post.objects.all()
    # 2. template 에 보내준다.
    context = {
        'posts' : posts,
    }
    
    return render(request, 'posts/index.html', context)

def new(request):
    return render(request, 'posts/new.html')

def create(request):
    
    # 1. parameter 로 날라온 데이터를 받아서
    title = request.GET.get('title')
    content = request.GET.get('content')
    
    # 2. DB에 저장
    Post.objects.create(title=title, content=content)
    
    context = {
        'title': title,
        'content': content, 
    }
    
    return redirect('posts:index')
```



여기까지만 하면 C, R 라서, D(삭제) 버튼도 만들어주기

(U, 수정은 비모쌤과 같이 하기)

```html
{% extends 'base.html' %}

{% block content %}
<h1>게시판</h1>

<ul>
    {% for post in posts %}
    <li>ID: {{ post.id }} | 제목: {{ post.title }} | 내용: {{ post.content }}
        <a href="">
            [수정]
        </a> / 
        <a href="/posts/delete/{{ post.id }}">
            [삭제]
        </a>
    </li>
    {% endfor %}
</ul>

<a href="{% url 'posts:new' %}">새글쓰기</a>

{% endblock %}
```



urls.py

```python
# posts - urls.py

from django.urls import path
from . import views

"""
메인(R) 페이지: 게시글의 목록(/posts/) / 게시글 상세
작성(C) 페이지: 글을 작성하는 페이지 / 작성 완료
수정(U) 페이지: 글을 수정하는 페이지 / 수정 완료
삭제(D) : 글목록이나 상세 페이지에 넣을 기능, 글 삭제 완료
"""

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new')
    path('create/', views.create, name='create'),
    path('delete/<int:pk>', views.delete, name='delete'),
]
```



delete 함수 정의하러 가기

```python
from django.shortcuts import render, redirect
from .models import Post

def index(request):
    # 모든 글 목록을 보여준다.
    # 1. DB에서 모든 글을 불러온다.
    posts = Post.objects.all()
    # 2. template 에 보내준다.
    context = {
        'posts' : posts,
    }
    
    return render(request, 'posts/index.html', context)

def new(request):
    return render(request, 'posts/new.html')

def create(request):
    
    # 1. parameter 로 날라온 데이터를 받아서
    title = request.GET.get('title')
    content = request.GET.get('content')
    
    # 2. DB에 저장
    Post.objects.create(title=title, content=content)
    
    context = {
        'title': title,
        'content': content, 
    }
    
    return redirect('posts:index')

def delete(request, pk):
    Post.objects.get(id=pk).delete()
    
    return redirect('posts:index')
```



이 상태에서 localhost:8000/posts 들어가서

맘에 안드는 글들 삭제 누르면 삭제됨



---



이까지 만들었을때 중자 해커는 localhost:8000/posts/create/?title=공격!!&content=공격!!

주소창에 입력해서 게시판 공격할 수 있음



고수 해커는 제일 상단에 templates 폴더 안에 hacking.py 작성

```python
import requests

base_url = 'http://localhost:8000/posts/'

while (True):
    requests.get(base_url + 'create/?title=공격!!&content=공격!!')
```

그리고 python hacking.py 터미널에 입력하면 해킹됨 ㅜㅜ