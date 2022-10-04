# ✅Django ModelForm I

> 1. 가상환경 및 Django 설치
> 2. articles app 생성 및 등록
> 3. Model 정의 (DB 설계)
> 4. CRUD 기능 구현
>
> 
>
> [학습목표]
>
> Form Class / ModelForm 에 대한 이해
>
> ModelForm 구현
>
> CRUD 로직을 ModelForm 으로 변경



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

### 1-2. Django 설치 및 기록

```bash
# upgrade pip
$ python -m pip install --upgrade pip

# install Django 
$ pip install django==3.2.13

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

### 1-4. 프로젝트 추가 설정(internationalization)

> 다국어 지원은 django i18n 검색 결과 참조

```python
# pjt/settings.py 하단으로 내려가서

# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'UTC' 부분을 아래와 같이 변경

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'
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

```python
# 먼저 pjt/urls.py 에서

from django.contrib import admin
from django.urls import path

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

<body>
    <h1>안녕!</h1>
</body>

<!-- 여기까지 작성 후,
     http://127.0.0.1:8000/articles/ 접속했을때
     서버 정상적으로 실행되는지 확인 -->
```



## 3. Model 정의 (DB 설계)

> SW개발에서 UI 기능 / DB 는 서로 밀접한 연관을 맺고 있음
>
> CRUD 를 만든다는 것은 DB의 생성, 수정, 삭제를 고려해야 하는 것이므로, CRUD 로 넘어가기 전에 모델 정의가 선행되어야함

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

# 2. 설계한 모델을 DB에 반영
```

### 3-2. 마이그레이션 파일 생성

```bash
$ python manage.py makemigrations
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

### 4-1. [CREATE] 게시글 생성

> 핵심 : form 으로 데이터를 입력 받아서, DB 에 추가해야함
>
> 위 2가지 기능이 들어가기 때문에 url 도 2개가 필요한 것
>
> = 사용자에게 HTML Form 제공, 입력받은 데이터를 처리 (ModelForm 로직으로 변경)

#### 4-1-1. [CREATE_기능1] HTML Form 제공

> http://127.0.0.1:8000/articles/new/
>
> 위의 url 을 new 함수에서 처리할 수 있도록 구현

```python
# articles/urls.py 에서 아래와 같이 path 채워넣기
# 새로 추가한 코드 : path('new/', views.new, name='new'),

from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    # 아래 주소에 들어오면 어떤 화면을 보여줄지
    # 생각하면서 path 를 작성 ...
    # http://127.0.0.1:8000/articles/
    path('', views.index, name='index'),
    # http://127.0.0.1:8000/articles/new/
    path('new/', views.new, name='new'),
]
```

```python
# articles/views.py 에서 new 함수 생성
# 새로 추가한 코드 : def new 부분

from django.shortcuts import render

# Create your views here.

# 요청 정보를 받아서..
def index(request):

    # 원하는 페이지를 render..
    return render(request, 'articles/index.html')

def new(request):
    return render(request, 'articles/new.html')
```

```django
<!-- articles/templates/articles 폴더 최하단에 
     new.html 생성 -->

<h1>글쓰기</h1>

<!-- form : 사용자에게 양식을 제공하고 
  값을 받아서(input : name, value)
  서버에 전송(form : action) -->
<form action="">
  <label for="title">제목 : </label>
  <input type="text" name="title" id="title">
  <label for="content">내용 : </label>
  <textarea name="content" id="content" cols="30" rows="10"></textarea>
  <input type="submit" value="글쓰기">
</form>

<!-- 여기까지 작성 후,
     http://127.0.0.1:8000/articles/new/ 접속했을때
     서버 정상적으로 실행되는지 확인 -->
```

#### 4-1-2. [CREATE_기능2] 입력받은 데이터 처리

> http://127.0.0.1:8000/articles/create/
>
> 위의 url 을 create 함수에서 처리할 수 있도록 구현
>
> 게시글 DB에 생성하고 index 페이지로 redirect (이건 설계하기 나름)

```python
# articles/urls.py 에서 아래와 같이 path 채워넣기
# 새로 추가한 코드 : path('create/', views.new, name='create'),

from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    # 아래 주소에 들어오면 어떤 화면을 보여줄지
    # 생각하면서 path 를 작성 ...
    # http://127.0.0.1:8000/articles/
    path('', views.index, name='index'),
    # http://127.0.0.1:8000/articles/new/
    path('new/', views.new, name='new'),
    # http://127.0.0.1:8000/articles/create/
    path('create/', views.create, name='create'),
]
```

```python
# articles/views.py 에서 create 함수 생성
# 새로 추가한 코드 : def create 부분

from django.shortcuts import render, redirect
from .models import Article

# Create your views here.

# 요청 정보를 받아서..
def index(request):

    # 원하는 페이지를 render..
    return render(request, 'articles/index.html')

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    # DB에 저장하는 로직
    title = request.GET.get('title')
    content = request.GET.get('content')
    Article.objects.create(title=title, content=content)
    return redirect('articles:index')
```

```django
<!-- 앞서 작업하고 있던 new.html 파일의
     form 태그 action DTL 로 작성
     (DTL 활용 이유: url 을 변수화해서 쓰고 있기 때문) -->

<h1>글쓰기</h1>

<!-- form : 사용자에게 양식을 제공하고 
  값을 받아서(input : name, value)
  서버에 전송(form : action) -->
<form action="{% url 'articles:create' %}">
  <label for="title">제목 : </label>
  <input type="text" name="title" id="title">
  <label for="content">내용 : </label>
  <textarea name="content" id="content" cols="30" rows="10"></textarea>
  <input type="submit" value="글쓰기">
</form>

<!-- 위와 같이 DTL 로 form 태그의 action 속성을 정의했지만,
     서버 돌려서 http://127.0.0.1:8000/articles/new/ 페이지의
     '페이지 소스 보기' 클릭하면 action 속성이 아래와 같이 변역되어있다
     <form action="/articles/create/"> -->

<!-- 여기까지 create 기능을 구현한 다음, form 에 입력한 데이터가
     실제 DB에 반영되고 있는지 Open Databese 통해 확인하기 -->
```

```django
<!-- articles/templates/articles 폴더 최하단 index.html 로 돌아가서
     새글쓰기 버튼 생성 -->

<body>
    <h1>안녕!</h1>
    <a href="{% url 'articles:new' %}">새글쓰기</a>
</body>
```

### 4-2. [READ] 게시글 목록

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

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    # DB에 저장하는 로직
    title = request.GET.get('title')
    content = request.GET.get('content')
    Article.objects.create(title=title, content=content)
    return redirect('articles:index')
```

```django
<!-- template 에 전달하기 단계 -->
<!-- articles/templates/articles 폴더 최하단 index.html 에서
     게시글 title 목록 생성 (DTL 반복문 활용) -->

<body>
  <h1>안녕!</h1>
  <a href="{% url 'articles:new' %}">새글쓰기</a>
  {% for article in articles %}
  <h3>{{ article.title }}</h3>
  <p>{{ article.created_at }} | {{ article.updated_at }}</p>
  <hr>
  {% endfor %}
</body>
```



- HTTP POST

  - 위와 같이 코드를 작성하고 발생할 수 있는 이슈가 보안, 유효성 문제
  - 예를 들어 우리가 만든 form 이 회원가입을 목적으로 한다면, 클라이언트가 데이터를 submit 할 때 주소창(url)이나 log 에 비밀번호처럼 민감한 개인정보가 노출됨
  - HTTP 요청 메세지의 구성을 보면([이미지](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)) `GET` 메서드가 활용되고 있음을 알 수 있는데 새로운 메서드인 `POST ` 활용해서 이런 이슈를 해결할 수 있음
  - 따라서 form 은 `POST` 이용해서 작성하는 것이 일반적임
  - **앞으로도 게시글 생성(CREATE 구현)할 때 무조건 POST 활용하자**

  | HTTP request methods | [(source)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods) |
  | -------------------- | ------------------------------------------------------------ |
  | `GET`                | The GET method requests a representation of the specified resource. Requests using GET should only retrieve data. (=리소스의 표현, **데이터를 '조회'할 때만 사용**) [ex. Google 검색창 form 의 method] |
  | `POST`               | The POST method submits an entity to the specified resource, often causing a change in state or side effects on the server. (=서버의 상태를 변화시키고, **데이터를 '제출/등록'할 때 사용**) [ex. Google 회원가입창 form 의 method] |

- 위 내용을 참조해서 우리가 작성했던 코드를 바꿔보면 url 요청이 `"POST /articles/create/ HTTP/1.1" 302 0` 이런식으로 보안처리 되어서 넘어감

  ```django
  <!-- 변화 1. --> 
  <!-- new.html 의 form 태그 안에 method="POST" 속성 추가 -->
  <!-- {% csrf_token %} 추가  -->
  
  <form action="{% url 'articles:create' %} method="POST">
    {% csrf_token %}
    <label for="title">제목 : </label>
    <input type="text" name="title" id="title">
    <label for="content">내용 : </label>
    <textarea name="content" id="content" cols="30" rows="10"></textarea>
    <input type="submit" value="글쓰기">
  </form>
                                    
  <!-- csrf 는 사이트 간 요청 위조의 준말로, 
       다른 사이트에서 요청이 변조된건 아닌지 확인하는 Django 기본 기능 -->
  ```

  ```python
  # 변화 2.
  # articles/views.py 에서 create 함수에
  # GET 메서드로 작성된 부분을 전부 POST 메서드로 바꿔주기
  
  def create(request):
      # DB에 저장하는 로직
      title = request.POST.get('title')
      content = request.POST.get('content')
      Article.objects.create(title=title, content=content)
      return redirect('articles:index')
  ```



- ModelForm

  - DB 기반의 어플리케이션을 개발하다보면, HTML Form(UI)은 Django 의 모델(DB)과 매우 밀접한 관계를 갖게 됨
    - 사용자로부터 값을 받아 DB에 저장하여 활용하기 때문
    - 즉, 모델에 정의한 필드의 구성 및 종류에 따라 HTML Form 이 결정됨
  - 사용자가 입력한 값이 DB의 데이터 형식과 일치하는지를 확인하는 유효성 검증이 반드시 필요하며 이는 서버 사이드에서 반드시 처리해야 함

- 위 내용을 참조해서 우리가 작성했던 코드를 바꿔보면 FE, BE 단에서 이중처리를 해야됨

  ```django
  <!-- 변화 1. FE 단에서 처리하기 -->
  <!-- 일단 new.html 의 input, textarea 태그 안에 required 써주면 
  	사용자가 제목이나 내용을 공란으로 제출할 때 경고창 띄워주긴 하지만,
  	개발자도구 열어서 required 지우면 공란 제출이 가능해져버림 -->
  <!-- 궁극적으로 서버 사이드에도 유효성 검증 로직을 넣어야 한다는 말 -->
  
  <form action="{% url 'articles:create' %} method="POST" required>
    {% csrf_token %}
    <label for="title">제목 : </label>
    <input type="text" name="title" id="title" required>
    <label for="content">내용 : </label>
    <textarea name="content" id="content" cols="30" rows="10" required></textarea>
    <input type="submit" value="글쓰기">
  </form>
  ```

  ```python
  # 변화 2. BE 단에서 ModelForm 생성하기(1)
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

  ```python
  # 변화 3. BE 단에서 ModelForm 생성하기(2)
  # ModelForm 의 인스턴스를 넘겨줘서 new.html 에 작성된 form 대체해야 함
  # 따라서 articles/views.py 에서 new 함수를 아래와 같이 수정
  
  from django.shortcuts import render, redirect
  from .models import Article
  from .forms import ArticleForm
  
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
  
  def new(request):
      article_form = ArticleForm()
      context = {
          'article_form': article_form
      }
      return render(request, 'articles/new.html', context=context)
  
  def create(request):
      # DB에 저장하는 로직
      title = request.POST.get('title')
      content = request.POST.get('content')
      Article.objects.create(title=title, content=content)
      return redirect('articles:index')
  ```

  ```django
  <!-- 변화 4. BE 단에서 ModelForm 생성하기(3) -->
  <!-- articles/new.html 에서 {{ article_form.as_p }} 추가 -->
  
  <form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    {{ article_form.as_p }}
    <label for="title">제목 : </label>
    <input type="text" name="title" id="title" required>
    <label for="content">내용 : </label>
    <textarea name="content" id="content" cols="30" rows="10" required></textarea>
    <input type="submit" value="글쓰기">
  </form>
  
  <!-- 여기까지 작성하고 서버 돌려보면, form 이 중복되어 작성됨
       위쪽은 ModelForm 이 만들어준거고, 아래는 우리가 직접 쓴거 -->
  <!-- 따라서 {{ article_form.as_p }} 이하에 우리가 직접 작성한
       label, input, label, textarea 주석처리해도 정상 작동 -->
  ```

  ```python
  # 변화 5. BE 단에서 ModelForm 생성하기(4) : 유효성 검사
  # 위 articles/views.py 에서 new 함수를 바꾼 것처럼,
  # articles/views.py 에서 create 함수도 아래와 같이 수정하고
  # 유효성 검사하기 위한 로직 만들기
  
  def create(request):
      # DB에 저장하는 로직
      article_form = ArticleForm(request.POST)
      if article_form.is_valid():
          article_form.save()
          return redirect('articles:index')
      else:
          # 일반적인 사이트들은 유효하지 않을 때
          # 이슈가 발생한 페이지를 보여주고 정정하라고 하는데,
          # ModelForm 활용해서 new.html 로 넘겨주라고 else 문 작성하면
          # 우리가 원했던 기능이 구현됨
          context = {
              'article_form': article_form
          }
          return render(request, 'articles/new.html', context=context)
  
  # 위와 같이 작성하고 제목이나 내용을 비운 상태로 글쓰기 버튼 누르면
  # 유효성 검사를 통과하지 못했기 때문에, 글 작성이 안되는 것 확인 가능
  # Django 공식 문서 : 'Validation on a ModelForm' 참조
  ```

  ```python
  # 변화 6. BE 단에서 ModelForm 생성하기(5) : 코드 병합
  # def new 아랫단과 def create 아랫단의 로직이 매우 유사하므로
  # 이 두 함수를 하나로 합치는 작업
  
  # 2개 함수를 1개로 합치려면, 일단 2개로 나뉜 url을 1개로 병합
  # 일단 articles/views.py 에서 def new 부분을 주석 처리하고
  # def create 부분을 아래와 같이 수정
  
  # def new(request):
  #     article_form = ArticleForm()
  #     context = {
  #         'article_form': article_form
  #     }
  #     return render(request, 'articles/new.html', context=context)
  
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

  ```python
  # 변화 7. BE 단에서 ModelForm 생성하기(6)
  # articles/urls.py 에서 아래와 같이
  # path('new/', views.new, name='new'), 부분 주석 처리
  
  urlpatterns = [
      # 아래 주소에 들어오면 어떤 화면을 보여줄지
      # 생각하면서 path 를 작성 ...
      # http://127.0.0.1:8000/articles/
      path('', views.index, name='index'),
      # http://127.0.0.1:8000/articles/new/
      # path('new/', views.new, name='new'),
      # http://127.0.0.1:8000/articles/create/
      path('create/', views.create, name='create'),
  ]
  ```

  ```django
  <!-- 변화 8. BE 단에서 ModelForm 생성하기(7) -->
  <!-- index.html 에서 새글쓰기 버튼의 a 태그 링크도 아래와 같이 변경 -->
  
  <a href="{% url 'articles:create' %}">새글쓰기</a>
  ```

  

### 4-3. [READ_detail] 상세보기

> 수정하기(UPDATE) 기능을 구현하기 위해, 상세보기 페이지를 먼저 작성
>
> 상세보기 핵심 : '특정한' 글을 본다
>
> url 패턴 : http://127.0.0.1:8000/articles/`<int:pk>`/

```python
# articles/urls.py 에서 detail 페이지로 넘어가는 path 를 아래와 같이 작성

urlpatterns = [
    # 아래 주소에 들어오면 어떤 화면을 보여줄지
    # 생각하면서 path 를 작성 ...
    # http://127.0.0.1:8000/articles/
    path('', views.index, name='index'),
    # http://127.0.0.1:8000/articles/new/
    # path('new/', views.new, name='new'),
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
    article = Article.objects.get(pk=pk)
    # template 에 객체 전달
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)
```

```django
<!-- detail.html 생성하고 아래와 같이 내용 채우기 -->

<h1>{{ article.pk }}번 게시글</h1>
<p>{{ article.created_at }} | {{ article.updated_at }}</p>
<p>{{ article.content }}</p>
```

```django
<!-- index.html 에서 게시글 title 을 누르면 detail 페이지로
     넘어가게끔 a 태그의 href 작성 -->

<body>
  <h1>안녕!</h1>
  <a href="{% url 'articles:create' %}">새글쓰기</a>
  {% for article in articles %}
  <h3><a href="{% url 'articles:detail' article.pk %}">{{ article.title }}</a></h3>
  <p>{{ article.created_at }} | {{ article.updated_at }}</p>
  <hr>
  {% endfor %}
</body>

```

### 4-4. 삭제하기

> 삭제하기 핵심 : '특정한' 글을 삭제한다
>
> http://127.0.0.1:8000/articles/`<int:pk>`/delete/

### 4-5. 수정하기

> ModelForm 활용해서 수정하는 것이 중요
>
> 수정하기 핵심 : '특정한' 글을 수정한다 => 사용자에게 수정할 수 양식을 제공하고(GET) 특정한 글을 수정한다(POST)
>
> http://127.0.0.1:8000/articles/`<int:pk>`/update/

```python
# articles/urls.py 에서 아래와 같이 update path 추가

urlpatterns = [
    # 아래 주소에 들어오면 어떤 화면을 보여줄지
    # 생각하면서 path 를 작성 ...
    # http://127.0.0.1:8000/articles/
    path('', views.index, name='index'),
    # http://127.0.0.1:8000/articles/new/
    # path('new/', views.new, name='new'),
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

```django
<!-- detail.html 페이지에 a 태그로 수정하기 버튼 생성 -->

<h1>{{ article.pk }}번 게시글</h1>
<p>{{ article.created_at }} | {{ article.updated_at }}</p>
<p>{{ article.content }}</p>
<a href="{% url 'articles:update' article.pk %}">수정하기</a>
```

```python
# articles/views.py 에서 아래와 같이 update 함수 추가

def update(request, pk):
    # GET 처리 : Form 을 제공
    article_form = ArticleForm()
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/update.html', context)
```

```django
<!-- update.html 생성하고 아래와 같이 내용 채우기 -->

<h1>글 수정하기</h1>

<form action="" method="POST">
  {{ article_form.as_p }}
  <input type="submit" value="수정">
</form>
```

```python
# articles/views.py 에서 update 함수를 아래와 같이 수정

def update(request, pk):
    # GET 처리 : Form 을 제공
    article = Article.objects.get(pk=pk)
    # 기존 instance 가진 상태의 ArticleForm()
    article_form = ArticleForm(instance=article)
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/update.html', context)
```

```django
<!-- update.html 에서 form 태그 안에 csrf 코드 추가하기 -->

<h1>글 수정하기</h1>

<form action="" method="POST">
  {% csrf_token %}
  {{ article_form.as_p }}
  <input type="submit" value="수정">
</form>
```

```python
# DB 에 실제 수정된 값 반영하기(저장하기)
# articles/views.py 에서 update 함수 아래와 같이 수정하기

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

