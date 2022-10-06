# ✅Django ModelForm II

> 1. 가상환경 및 Django 설치
> 2. articles app 생성 및 등록
> 3. Model 정의 (DB 설계)
> 4. CRUD 기능 구현
> 5. Admin site
> 6. Static files
> 7. Django Bootstrap5
>
> 
>
> 💡 Django ModelForm I 필기와의 차이점 : 
>
> - (CRUD 시작할때) 처음부터 ModelForm 활용해서  게시판 기능 구현
> - CRUD 중에 D(삭제) 기능 추가 구현
>   - Django ModelForm I 필기는 CRU 까지만 구현
>
> - Django Bootstrap5 패키지 활용
>   - 🗂️ [(참고자료)](https://pypi.org/project/django-bootstrap5/)
> - Django settings.py 에서 시크릿 키 분리
>   - 🗂️ [(참고자료)](https://grape-blog.tistory.com/17)
> - (프로젝트 추가 설정 단계에) base.html 적용
> - Admin site
> - Static files
>
> 
>
> 💡 추천 학습자료
>
> - [HTTP request & response object](https://docs.djangoproject.com/en/4.1/ref/request-response/)
> - [ModelForm](https://docs.djangoproject.com/en/4.1/topics/forms/modelforms/)
> - [Django view shortcut functions](https://docs.djangoproject.com/en/4.1/topics/http/shortcuts/)



## 1. 가상환경 및 Django 설치

> 가상환경 설치하는 이유 : 프로젝트마다 패키지를 별도로 가져가야하기 때문
>
> 가상환경 생성 및 실행하기 전에 .gitignore 파일, README.md 파일을 먼저 추가해놓고, 아래 명령어로 변경내역 추적 시작하기
>
> 이 때 .gitignore 파일에 가상환경 폴더를 써두어야함(`/venv`)
>
> `$ git init` 👉 `$ git add .` 👉 `$ git commit -m 'init'`

### 1-1. 가상환경 생성 및 실행

```bash
$ python -m venv venv
$ source venv/Scripts/activate
(venv)
```

### 1-2. Django / Bootstrap5 설치 및 기록

```bash
# upgrade pip
$ python -m pip install --upgrade pip

# install Django 
$ pip install django==3.2.13

# install Bootstrap5
$ pip install django-bootstrap5

# 내가 활용하고 있는 패키지들 기록지에 남기기
$ pip freeze > requirements.txt
```

### 1-3. Django 프로젝트 생성

```bash
# 현재 위치(.)에 pjt 라는 이름의 프로젝트를 생성
$ django-admin startproject pjt .

# 서버 실행되는지 확인
$ python manage.py runserver
```

### 1-4. 프로젝트 추가 설정

> 다국어 지원은 django i18n 검색 결과 참조

#### 1-4-1. 시크릿 키 분리하기

> 🗂️[(참고자료)](https://grape-blog.tistory.com/17)

#### 1-4-2. Bootstrap5 app 등록

```python
# pjt/settings.py 중반부에서 

# INSTALLED_APPS = [] 괄호 내 상단에 아래와 같이 Bootstrap5  앱 등록

INSTALLED_APPS = [
    'django_bootstrap5',
    ...,
]
```

#### 1-4-3. internationalization

```python
# pjt/settings.py 하단으로 내려가서

# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'UTC' 부분을 아래와 같이 변경

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'
```

#### 1-4-4. base.html 생성

(1) 프로젝트 폴더(pjt) 보다 더 상단에 templates 폴더 생성

(2) 새로 만든 templates 폴더 안에 base.html 파일 생성 (미리 만들어둔 base.html 파일 있으면 복붙)

(3) settings.py 에서 새로 만든 templates 폴더 등록해주기

```python
# pjt/settings.py 에서 TEMPLATES = [] 안에
# 'DIRS': [], 부분을 아래와 같이 수정

'DIRS': [BASE_DIR/"templates"],
```



## 2. articles app 생성 및 등록

> 기본적인 CRUD 기능이 동작하는 게시판 앱 만들기
>
> 앱은 MTV 패턴으로 제작
>
> 앱을 생성하기 위해, 위에서 실행하고 있던 서버를 잠깐 종료(`ctrl` + `c`)

### 2-1. app 생성

```bash
$ python manage.py startapp articles
```

### 2-2. app 등록

```python
# pjt/settings.py 에서

# INSTALLED_APPS = [] 괄호 내 최상단에 아래와 같이 생성한 앱 등록

INSTALLED_APPS = [
    'articles',
    ...,
]
```

### 2-3. urls.py 설정 

#### 2-3-1. urls.py 분리 작업

> url 관리를 각 앱에서 관리할 수 있도록, include 활용해 분리하기
>
> 💡 활용 : `articles:index` => `/articles/`
>
>   ex) Template 에서 활용 : `{% url 'articles:index' %}`
>
>   ex) View 에서 활용 : `redirect('articles:index')`

```python
# 먼저 pjt/urls.py 에서 아래와 같이 include import 한 다음
# 'articles/' 경로로 향하는 path 추가

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
]
```

```python
# articles/urls.py 생성하고,
# urlpatterns = [] 이런 식으로 빈 리스트 선언해야 서버 실행이 됨

urlpatterns = [
    
]
```

```python
# articles/urls.py 에서 아래와 같이 코드 계속 작성

from django.urls import path

app_name = 'articles'

urlpatterns = [

]
```

#### 2-3-2. index.html 생성

> 기본 순서 : URL - VIEW - TEMPLATE
>
> - url 을 등록하고, view 함수 생성, template 만든다
> - URL 을 요청 받아서, 처리하고 응답해주는게 Django 의 근본이니까 위와 같은 순서로 작업

```python
# articles/urls.py 에서 아래와 같이 path 채워넣기

from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    # 아래 주소에 들어오면 어떤 화면을 보여줄지
    # 생각하면서 path 를 작성 ...
    # http://127.0.0.1:8000/articles/
    path('', views.index, name='index'),
]
```

```python
# articles/views.py 에서 index 함수 생성

from django.shortcuts import render

# Create your views here.

# 요청 정보를 받아서..
def index(request):

    # 원하는 페이지를 render..
    return render(request, 'articles/index.html')
```

```django
<!-- articles/templates/articles 폴더 생성 후 
     폴더 최하단에 index.html 생성 -->

{% extends 'base.html' %}

{% block content %}

<h1>안녕!</h1>

{% endblock %}

<!-- 여기까지 작성 후,
     http://127.0.0.1:8000/articles/ 접속했을때
     서버 정상적으로 실행되는지 확인 -->
```



## 3. Model 정의 (DB 설계)

> SW개발에서 UI 기능 / DB 는 서로 밀접한 연관을 맺고 있음
>
> CRUD 를 만든다는 것은 DB의 생성, 조회, 수정, 삭제를 고려해야 하는 것이므로, CRUD 로 넘어가기 전에 모델 정의가 선행되어야함

### 3-1. 클래스 정의

```python
# articles/models.py 에 모델 설계

from django.db import models

# Create your models here.

'''
게시판 기능
- 제목(20글자이내)
- 내용(긴 글)
- 글 작성시간 / 글 수정시간(자동으로 기록, 날짜/시간)
'''

# 1. 모델 설계 (=DB 스키마 설계)
# Article 은 models 에 있는 Model 을 상속 받음
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# 2. 설계한 모델을 DB에 반영(아래 3-2. 부터 3-4. 까지)
```

### 3-2. 마이그레이션 파일 생성

```bash
$ python manage.py makemigrations

# 위 명령어 입력 후, 
# articles/migrations/0001_initial.py 생성된 것 확인
```

### 3-3. DB 반영 (`migrate`)

```bash
$ python manage.py migrate
```

### 3-4. DB 반영 잘 되었는지 Django 에서 확인

```bash
$ python manage.py showmigrations

# 이때 articles [X] 0001_initial 생성되어있으면 DB 반영된 것임
```



## 4. CRUD 기능 구현

> 위 모델에 맞는 CRUD 기능 구현해보기 

### 4-1. ModelForm 선언

> **선언된 모델에 따른** 필드 구성 
>
> (1) form 생성 (2) 유효성 검사

```python
# ModelForm 생성하기
# articles/forms.py 파일 새로 생성해서 아래와 같이 코드 채우기
# Article model 에 있는 모든 fields 를 가져다가 쓰겠다는 의미임

from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = '__all__'

# 만약 여기서 title 입력란만 생성하고 싶으면
# Meta class 안에 fields = ['title'] 이렇게 작성하면 되고,
# title, content 입력란 생성하고 싶으면
# Meta class 안에 fields = ['title', 'content'] 이렇게 작성
```

### 4-2. [CREATE] 게시글 생성

> 핵심 : form 으로 데이터를 입력 받아서, DB 에 추가해야함
>
> = 사용자에게 HTML Form 제공, 입력받은 데이터를 처리 
>
> 원래는 위 2가지 기능이 들어가기 때문에 url 도 2개가 필요하지만(new, create)
>
> **ModelForm 로직으로 변경하면서 create url 1개에 2가지 기능 넣을 수 있음**

```django
<!-- articles/templates/articles 폴더 최하단 index.html 로 돌아가서
     새글쓰기 버튼 일단 생성 -->

{% extends 'base.html' %}

{% block content %}

<h1>안녕!</h1>
<a href="{% url 'articles:create' %}">새글쓰기</a>

{% endblock %}
```

```python
# articles/urls.py 에서 아래와 같이 path 채워넣기
# 새로 추가한 코드 : path('create/', views.create, name='create'),

from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    # 아래 주소에 들어오면 어떤 화면을 보여줄지
    # 생각하면서 path 를 작성 ...
    # http://127.0.0.1:8000/articles/
    path('', views.index, name='index'),
    # http://127.0.0.1:8000/articles/create/
    path('create/', views.create, name='create'),
]
```

```python
# articles/views.py 에서 create 함수 작성
# GET 메서드가 아닌 POST 메서드 사용하는게 핵심

from django.shortcuts import render, redirect
from .forms import ArticleForm

# Create your views here.

# 요청 정보를 받아서..
def index(request):

    # 원하는 페이지를 render..
    return render(request, 'articles/index.html')

def create(request):
    if request.method == 'POST':
        # DB에 저장하는 로직
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:index')
    else: # request.method == 'GET':
        # 일반적인 사이트들은 유효하지 않을 때
        # 이슈가 발생한 페이지를 보여주고 정정하라고 하는데,
        # ModelForm 활용해서 new.html 로 넘겨주라고 else 문 작성하면
        # 우리가 원했던 기능이 구현됨
        article_form = ArticleForm()
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/new.html', context=context)
```

```django
<!-- articles/templates/articles 폴더 최하단에 
     아래와 같이 new.html 생성 -->

{% extends 'base.html' %}

{% block content %}

<h1>글쓰기</h1>
<form action="{% url 'articles:create' %}" method="POST">
  {% csrf_token %}
  {{ article_form.as_p }}
  <input type="submit" value="글쓰기">
</form>

{% endblock %}

<!-- 여기까지 작성 후,
     http://127.0.0.1:8000/articles/create/ 접속했을때
     서버 정상적으로 실행되는지 확인 -->
<!-- create 기능 구현이 완료되었다면, form 에 입력한 데이터가
     실제 DB에 반영되고 있는지 Open Databese 통해 확인하기 -->
```

### 4-3. [READ] 게시글 목록 읽기

> 게시글 목록 기능을 구현하기 전에, 가장 먼저 살펴볼 부분은
>
> 이 기능을 어떤 함수에서 처리하고 있는지를 확인하는 것
>
> 현재 작성되고 있는 코드에서는 `index` 함수에서 처리하고 있음
>
> DB에서 게시글을 가져와서, template 에 전달 :  context 딕셔너리!

```python
# DB에서 게시글 가져오기 단계
# articles/views.py 에서 index 함수 수정
# 수정된 코드 : def index 부분

from django.shortcuts import render, redirect
from .forms import ArticleForm
from .models import Article

# Create your views here.

# 요청 정보를 받아서..
def index(request):
    # 게시글을 가져와서..
    # (보통 게시판은 최신글이 맨위니까 .order_by('-pk') 활용)
    articles = Article.objects.order_by('-pk')
    # template 에 뿌려준다
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

def create(request):
    if request.method == 'POST':
        # DB에 저장하는 로직
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:index')
    else: # request.method == 'GET':
        # 일반적인 사이트들은 유효하지 않을 때
        # 이슈가 발생한 페이지를 보여주고 정정하라고 하는데,
        # ModelForm 활용해서 new.html 로 넘겨주라고 else 문 작성하면
        # 우리가 원했던 기능이 구현됨
        article_form = ArticleForm()
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/new.html', context=context)
```

```django
<!-- template 에 전달하기 단계 -->
<!-- articles/templates/articles 폴더 최하단 index.html 에서
     게시글 title 목록 생성 (DTL 반복문 활용) -->

{% extends 'base.html' %}

{% block content %}

<h1>안녕!</h1>
<a href="{% url 'articles:create' %}">새글쓰기</a>
{% for article in articles %}
<h3>{{ article.title }}</h3>
<p>{{ article.created_at }} | {{ article.updated_at }}</p>
<hr>
{% endfor %}

{% endblock %}
```

### 4-4. [READ_detail] 상세보기

> 수정하기(UPDATE) 기능을 구현하기 위해, 상세보기 페이지를 먼저 작성
>
> 상세보기 핵심 : '특정한' 글을 본다

- url 패턴 : `http://127.0.0.1:8000/articles/<int:pk>/`

```python
# articles/urls.py 에서 detail 페이지로 넘어가는 path 를 아래와 같이 작성
# 추가된 코드 : path('<int:pk>/', views.detail, name='detail'), 

from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    # 아래 주소에 들어오면 어떤 화면을 보여줄지
    # 생각하면서 path 를 작성 ...
    # http://127.0.0.1:8000/articles/
    path('', views.index, name='index'),
    # http://127.0.0.1:8000/articles/create/
    path('create/', views.create, name='create'),
    # http://127.0.0.1:8000/articles/1/ : 1번글
    # http://127.0.0.1:8000/articles/3/ : 3번글
    path('<int:pk>/', views.detail, name='detail'),
]
```

```python
# articles/views.py 에서 detail 함수를 아래와 같이 정의

def detail(request, pk):
    # 특정 글을 가져온다.
    #                        .get(모델칼럼명=urls.py에서 쓴 인자)
    article = Article.objects.get(pk=pk)
    # template 에 객체 전달
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)
```

```django
<!-- detail.html 생성하고 아래와 같이 내용 채우기 -->

{% extends 'base.html' %}

{% block content %}

<h1>{{ article.pk }}번 게시글</h1>
<h3>{{ article.title }}</h3>
<p>{{ article.created_at }} | {{ article.updated_at }}</p>
<p>{{ article.content }}</p>

{% endblock %}
```

```django
<!-- index.html 에서 게시글 title 을 누르면 detail 페이지로
     넘어가게끔 a 태그의 href 작성 -->

{% extends 'base.html' %}

{% block content %}

<h1>안녕!</h1>
<a href="{% url 'articles:create' %}">새글쓰기</a>
{% for article in articles %}
<h3><a href="{% url 'articles:detail' article.pk %}">{{ article.title }}</a></h3>
<p>{{ article.created_at }} | {{ article.updated_at }}</p>
<hr>
{% endfor %}

{% endblock %}
```

### 4-5. [UPDATE] 수정하기

> ModelForm 활용해서 수정하는 것이 중요
>
> 수정하기 핵심 : '특정한' 글을 수정한다 => 사용자에게 수정할 수 양식을 제공하고(GET) 특정한 글을 수정한다(POST)

- url 패턴 : `http://127.0.0.1:8000/articles/<int:pk>/update/`

```django
<!-- detail.html 페이지에 <a> 태그로 수정하기 버튼 먼저 생성 -->

{% extends 'base.html' %}

{% block content %}

<h1>{{ article.pk }}번 게시글</h1>
<h3>{{ article.title }}</h3>
<p>{{ article.created_at }} | {{ article.updated_at }}</p>
<p>{{ article.content }}</p>
<a href="{% url 'articles:update' article.pk %}">수정하기</a>

{% endblock %}
```

```python
# articles/urls.py 에서 아래와 같이 update path 추가
# 추가한 코드 : path('<int:pk>/update', views.update, name='update'),

urlpatterns = [
    # 아래 주소에 들어오면 어떤 화면을 보여줄지
    # 생각하면서 path 를 작성 ...
    # http://127.0.0.1:8000/articles/
    path('', views.index, name='index'),
    # http://127.0.0.1:8000/articles/create/
    path('create/', views.create, name='create'),
    # http://127.0.0.1:8000/articles/1/ : 1번글
    # http://127.0.0.1:8000/articles/3/ : 3번글
    path('<int:pk>/', views.detail, name='detail'),
    # http://127.0.0.1:8000/articles/1/update : 1번글 수정
    # http://127.0.0.1:8000/articles/3/update : 3번글 수정
    path('<int:pk>/update', views.update, name='update'),
]
```

```python
# DB 에 실제 수정된 값 반영하기(저장하기)
# articles/views.py 에서 아래와 같이 update 함수 추가

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        # POST : input 가져와서 검증하고 DB 에 저장
        article_form = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            # 유효성 검사 통과하면 저장후 상세보기 페이지로
            article_form.save()
            return redirect('articles:detail', article.pk)
        # 유효성 검사 통과 못하면 => 오류메세지
    else: 
        # GET 처리 : Form 을 제공
        article_form = ArticleForm(instance=article)
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/update.html', context)
```

```django
<!-- update.html 생성하고 아래와 같이 내용 채우기 -->

{% extends 'base.html' %}

{% block content %}

<h1>글 수정하기</h1>
<form action="" method="POST">
  {% csrf_token %}
  {{ article_form.as_p }}
  <input type="submit" value="수정">
</form>

{% endblock %}
```

### 4-6. [DELETE] 삭제하기

> 삭제하기 핵심 : '특정한' 글을 삭제한다

- url 패턴 : `http://127.0.0.1:8000/articles/<int:pk>/delete/`

```python
# articles/urls.py 에서 아래와 같이 delete path 추가
# 추가한 코드 : path('<int:pk>/delete/', views.delete, name='delete'),

urlpatterns = [
    # 아래 주소에 들어오면 어떤 화면을 보여줄지
    # 생각하면서 path 를 작성 ...
    # http://127.0.0.1:8000/articles/
    path('', views.index, name='index'),
    # http://127.0.0.1:8000/articles/create/
    path('create/', views.create, name='create'),
    # http://127.0.0.1:8000/articles/1/ : 1번글
    # http://127.0.0.1:8000/articles/3/ : 3번글
    path('<int:pk>/', views.detail, name='detail'),
    # http://127.0.0.1:8000/articles/1/update/ : 1번글 수정
    # http://127.0.0.1:8000/articles/3/update/ : 3번글 수정
    path('<int:pk>/update/', views.update, name='update'),
    # http://127.0.0.1:8000/articles/1/delete/ : 1번글 삭제
    # http://127.0.0.1:8000/articles/3/delete/ : 3번글 삭제
    path('<int:pk>/delete/', views.delete, name='delete'),
]
```

```python
# articles/views.py 에서 아래와 같이 delete 함수 추가

def delete(request, pk):
    Article.objects.get(pk=pk).delete()
    return redirect('articles:index')
```

```django
<!-- detail.html 페이지에 <a> 태그로 삭제하기 버튼 생성 -->

{% extends 'base.html' %}

{% block content %}

<h1>{{ article.pk }}번 게시글</h1>
<h3>{{ article.title }}</h3>
<p>{{ article.created_at }} | {{ article.updated_at }}</p>
<p>{{ article.content }}</p>
<a href="{% url 'articles:update' article.pk %}">수정하기</a>
<a href="{% url 'articles:delete' article.pk %}">삭제하기</a>

{% endblock %}
```



## 5. Admin site

> 사용자가 아닌 서버의 관리자가 활용하기 위한 페이지
>
> 모델 DB 를 admin.py 에 등록하고 관리
>
> http://127.0.0.1:8000/admin/ 에 접속하면 사용자 이름&비밀번호 입력해야 하는데,
>
> 아직 이 2가지 정보 설정이 안된 상태니까 아래 명령어로 설정 시작하기

### 5-1. 가상환경 (끈 상태였다면 다시) 켜기

```bash
$ source venv/Scripts/activate
(venv)
```

### 5-2. admin 계정 생성

```bash
$ python manage.py createsuperuser

# username 과 password 를 입력해 관리자 계정을 생성
# email은 선택사항이기 때문에 입력하지 않고 enter 가능
# 비밀번호 생성 시 보안상 터미널에 입력되지 않으니 무시하고 입력을 이어감
```

```python
# articles/admin.py 을 아래와 같이 채워놓기

from django.contrib import admin
from .models import Article

# Register your models here.

admin.site.register(Article)

# 여기까지 작성하고 http://127.0.0.1:8000/admin/ 에 로그인해보면
# 여태 작성된 Article objects 확인할 수 있고, 각각 관리(삭제/수정/조회)할 수 있음
```

### 5-3. admin 페이지 커스텀하기

```python
# articles/admin.py 을 아래와 같이 변경

from django.contrib import admin
from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')

admin.site.register(Article, ArticleAdmin)

# 여기까지 작성하고 http://127.0.0.1:8000/admin/ 에 로그인해보면
# Article objects 라고 표시되던 컨텐츠들이
# 전부 각각의 제목, 작성시간, 수정시간으로 표시되고 있음을 확인 가능
```



## 6. Static files

> 현 상태에서 메인 페이지에 이미지(정적 파일)를 넣고 싶을 때
>
> Django 는 아래와 같은 절차를 따름

### 6-1. pjt/settings.py 확인하기

```python
# INSTALLED_APPS = [] 안에 django.contrib.staticfiles 가 있는지 확인

INSTALLED_APPS = [
    ...,
    'django.contrib.staticfiles',
]

# STATIC_URL = '' 부분도 아래와 같이 정의되어 있는지 확인

STATIC_URL = '/static/'
```

### 6-2. 템플릿에서 static 템플릿 태그 사용

```django
<!-- index.html 에 이미지(static file) 1장 넣어보기 -->
<!-- static 템플릿 태그 사용함으로써 지정된 상대경로에 대한 URL 빌드 -->

{% extends 'base.html' %}

{% block content %}

{% load static %}

<h1>안녕!</h1>
<img src="{% static 'wow.jpg' %}" alt="img">

<a href="{% url 'articles:create' %}">새글쓰기</a>
{% for article in articles %}
<h3><a href="{% url 'articles:detail' article.pk %}">{{ article.title }}</a></h3>
<p>{{ article.created_at }} | {{ article.updated_at }}</p>
<hr>
{% endfor %}

{% endblock %}
```

### 6-3. 앱의 static 디렉토리에 정적 파일을 저장

- 예시) articles/static/wow.jpg 저장
- 생성된 static 폴더에는 images, css, js, fonts 파일들을 보관하는 다양한 폴더를 생성할 수 있음 (상세 내용은 pdf 참조)



## 7. Django Bootstrap5

> 1-4. 프로젝트 추가 설정에서  Bootstrap5 앱을 미리 등록했음
>
> 이제는 아래의 코드를 참조하여 Bootstrap5 테마를 모델폼에 적용시키기

```django
<!-- new.html 을 아래와 같이 바꿔주기 -->

{% extends 'base.html' %}

{% block content %}

  {% load django_bootstrap5 %}
  {% bootstrap_css %}
  {% bootstrap_javascript %}

  <h1>글쓰기</h1>
  <form action="" method="POST">
    {% csrf_token %}

    {% bootstrap_form article_form %}

    {% bootstrap_button content="글쓰기" button_type="submit" button_class="btn-primary col-3" %}

  </form>

{% endblock %}
```
