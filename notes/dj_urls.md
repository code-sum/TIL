# ✅ Django URLs

어제 수업 정리: 파라미터를 날리고, 데이터를 받아왔습니다



- 게시판 만들기
  - 인스타그램은 사진 게시판, 트위터는 짧은 게시판, 유튜브는 동영상 임베딩한 게시판 ... 조회, 수정, 삭제가 되는 게시판의 기능이 모두 들어가 있는 서비스들
  - 그래서 오늘부터 게시판 만들기 시작(내일부터 CRUD 풀패턴 학습)



오늘 커리큘럼 조금 더 구체화하자면, 어제 만들었던 앱을 업데이트하고, ORM을 살짝 복습합니다

원래 있던 앱에 새롭게 앱을 추가하고 URL 어떻게 컨트롤하는지 배웁니다(멀티 앱)



---



[사전 작업: 새로운 앱(articles) 생성하기]

1)기존에 작업하고 있던 가상환경 켠다 source [가상환경이름]/Scripts/activate

2)새로운 앱 만든다 python manage.py startapp articles

3)settings.py 에 앱 등록한다 (INSTALLED_APPS 맨 윗줄)

4)게시판 앱(articles)의 메인 페이지를 어떻게 만들지 생각해본다

	- 오늘은 게시판 전에 방명록 먼저 만들어봅니다
	- 어제 만든 practices - ping pong 기능에 저장기능만 추가하면 됨

5)여태까지는 프로젝트 폴더 urls.py 에 URL을 모두 담았는데, 각각 앱의 주문서를 별도로 찢는 연습도 해봅시다 practices/urls.py ◀️▶️ articles/urls.py



[새로 만든 앱(articles)의 `views.py`, `templates` 만들기]

1)urls.py 에서

from practices import views 아랫단에

from articles import views 적으려면 문제가 생김(=views 2개니까)

해결) from practices import views **as practices_views**

​            from articles import views **as articles_views**

​	        as 로 별칭 붙여주고, 아래 urlpatterns 에 들어가는 views 도 전부 변경

2)articles 의 index url 도 만들어주기

   path('', articles_views.index),

   (위에서 ''은 루트경로! -- 루트경로에 대해 정확히 정리해두기)

3)articles 폴더 내 views.py 열어서 index 함수 작성하기

   ```python
   def index(request):
       return render(request, 'index.html')
   ```

4)articles 폴더 내 templates 폴더 생성해서 index.html 파일 만들기

   index.html 만들기 전에, templates  폴더만 생성한 상태에서 서버 돌리면

   (python manage.py runserver 치고 localhost:8000 주소창에 넣음)

   정의한적 없는 템플릿이 빡! 등장한 것을 볼 수 있음

   (사실 practices 에서 작성했던 index.html 임)

​	이렇게 되는 이유는 서버 돌릴 때, 장고에 앱등록하면서 INSTALLED_APPS 에 우선적으로 적힌 애들부터 모두 긁어감. 특히 서로 다른 앱에 templates 폴더가 2개 있으면, 장고는 이 두개를 하나의(=같은) 폴더처럼 관리해버림 (파일명이 같은게 있으면, 두번째 파일은 우선순위에서 밀려나거나 등록을 안하는 방식으로 처리)

  이럴 때 장점도 있는데, 예를 들면 base.html 을 서로 다른 앱에 모두 먹일 수 있음

  그런데 앱마다 templates 따로 관리하고 싶다면, articles -> templates -> articles 폴더를 또 만들고, view.py 로 가서  render(request, '**articles**/index.html') 로 수정해주기(=html 파일 경로에 articles/ 구분자 추가)

  마찬가지로 practices 앱으로 돌아가서 templates 안에 practices 폴더 하나 더 만들고 html 파일들 옮겨주기(base.html 만 templates 에 그대로 두기), views.py 내에 .html 파일들 앞에 pratices/ 구분자도 추가해주기

  base.html 처럼 전체 공통으로 먹여야하는 애들은 사실 상위에 있는 프로젝트 폴더에 옮겨주는게 좋음(이런 분리 경로를 어떤 식으로 주는지 컨벤션은 회사마다 상황마다 다양할 수 있는데, 이번 수업에서는 프로젝트보다 더 높은 최상단에 templates 폴더 생성). 그 다음 templates 를 관리하는 settings.py 를 조작하면 되는데, settings.py 내 `'DIRS': [],` 부분에 새로 만든 templates 폴더의 경로를 추가 (pdf Template inheritance-추가 템플릿 경로 추가하기 참고)

  다른 파일/폴더들은 상대경로를 썼지만, settings.py 내 `'DIRS': [],` 부분에 새로 만든 templates 폴더의 경로를 추가할 때 원래는 절대경로를 이용해야함. settings.py 맨 위 근처에 보면 `BASE_DIR = Path(__file__).resolve.parent.parent` 라고 적혀있는데, 이건 절대경로처럼 쓸 수 있도록 Django 에서 미리 지정해둔 경로라서 요 `BASE_DIR` 을 일단 쓰면 됨



[base.html 전체적으로 먹이기]

  프로젝트 폴더보다 더 위 상단에 templates 폴더 생성

  새로 만든 templates 안에 base.html 이동(혹은 생성)

  settings.py 로 이동해서 `TEMPLATES = []` 괄호 내에 `'DIRS': [],`  괄호 내에 `BASE_DIR/'templates'` 써줌

```python
# settings.py

TEMPLATES = [
    {
        'DIRS': [BASE_DIR/'templates'],
    }
]
```

  (참고) templates 대신 base 라고 폴더명 바꿔도 됨



[URL 분리하기] - (pdf Django URLs 파트 읽어보면서 공부)

프로젝트 폴더 내 - urls.py 로 이동하면 url 이 계속 생기고 있음을 알 수 있는데, 

앱이 커지면 url 이 수십줄씩 생기기 때문에 관심사의 분리(SW개념)가 필요

 (앱별로 URL 쪼개는걸 App - URL mapping 이라고 해서 pdf 에도 이렇게 적음)

 메인 문지기가 힘들어하니까 문지기의 문지기(서브문지기) 만들어서 업무 분장해주기

1)practices 내에 urls.py 새로 만들기 (기존 urls.py 와 구조는 비슷)

```python
# practices/urls.py

from django.urls import path
# [1]

urlpatterns = [
    메인에서 담당하던 path 들 ctrl+x ~ ctrl+v 해서 일단 붙여넣기
    이젠 practices_views.index 로 분리할 필요가 없기 때문에
    함수 이름 앞에 practices_views. 지워줄 차례인데
    그 전에, 위 # [1] 자리에 
    from . import views 입력하고
    함수명 앞에 있는 practices_views. 모두 지워주기
]
```

2)위 1)의 과정을 새로 만든 articles 앱에도 동일하게 반복

​    (기존 urls.py 에서 path('', articles_views.index) 가져오기)

3)기존 프로젝트 폴더 내 urls.py 에서

​    from practices import views as practices_views
​    from articles import views as articles_views
​    위 코드는 전부 필요없어졌으니 지우고 파일 저장

4)메인 urls.py 에 서브문지기에 대한 설정 적어주기(include 이용)

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
]
```

5)여기까지하고 주소창에 localhost:8000/articles 접속해보면 정상 작동

6)4)의 과정을 practices 에도 동일하게 반복

```python
# 메인 urls.py 내에 urlpatterns = [] 괄호 안에 아래 코드 추가

path('practices/', include('practices.urls')),
```

7)여기까지하고 주소창에 localhost:8000/practices 접속해보면 정상 작동



[`localhost:8000/articles` 페이지를 방명록(혹은 담벼락)으로 만들기]

1)articles 폴더 내 templates 폴더 내 artices 안에 있는 index.html 로 이동

```html
{% extends 'base.html' %}

{% block content %}

<body>
    <div>
        <h1>방명록</h1>
    </div>
    <div>
        <h2>글 목록</h2>
        <p>글1</p>
        <p>글2</p>
        <p>...</p>
    </div>
    <div>
        <h2>글 작성</h2>
        <form action="/articles/create/" method="GET">
            <input type="text" name="content">
            <input type="submit">
        </form>
    </div>
</body>   
    
{% endblock %}
```

2)위 상태에서 주소창에서 텍스트(하이) 입력하고 제출 누르면

   주소가 `localhost:8000/articles/create/?content=하이` 로 바뀜

  (근데 아직 create 페이지 안만들어서 화면에 뜨는건 없음)

3)이제 **articles 폴더 안에서** URL-VIEW-TEMPLATE 방법론에 따라서 작성 [하단 4)~7) 부분]

4)urls.py urlpatterns = [] 괄호 안에 path 작성해주기

```python
# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path=('', views.index),
    path=('create/', views.create),
] 
```

5)views.py 에서 create 함수 작성

```python
# views.py

def create(request):
    return render(request, 'articles.create.html')
```

6)create.html 작성

```html
{% extends 'base.html' %}

{% block content %}
<h1>작성 완료</h1>
<p>작성 내용: {{ content }}</p>

{% endblock %}
```

7)content 작성하러 가기

```python
# views.py

def create(request):
    return render(request, 'articles.create.html', {'content': request.GET.get('content')})
```

8)create.html 에서 홈 링크 달아주기

```html
{% extends 'base.html' %}

{% block content %}
<h1>작성 완료</h1>
<p>작성 내용: {{ content }}</p>
<a href='/articles'>홈으로</a>

{% endblock %}
```

+) 여기까지만 작성하고, DB 처리하지 않고도 DB 되는 척 해보기

```python
# views.py

guestbook = []

def index(request):
    return render(request, 'articles/index.html', {'guestbook': guestbook})

def create(request):
    guestbook.append(content)
    return render(request, 'articles.create.html', {'content': request.GET.get('content')})
```

++) index.html 로 이동해서

```html
{% extends 'base.html' %}

{% block content %}

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
        <form action="/articles/create/" method="GET">
            <input type="text" name="content">
            <input type="submit">
        </form>
    </div>
</body>   
    
{% endblock %}
```

⚠️ 근데 위 코드는 메모리에 올라가있기 때문에, 서버 꺼보면 썼던 내용들이 전부 사라져있다



+++) 이때 사용자들의 소중한 데이터를 영구 저장소에 넣고 싶으면? 

⚠️ 작업해야 하니까 가상환경 다시 켜주는거 잊지 않기

Django 가 지원하는 ORM 활용

```python
# models.py 에 아래 2줄 코드(class 이하) 작성

from django.db import models

class Article(models.Model):
    content = models.TextField()
```

++++) 위에서 작성한 model 을 실제 DB 로 만들겠다고 Terminal 에 입력

```bash
$ python manage.py makemigrations

$ python manage.py migrate
```

++++++) DB 에 저장

```python
# views.py

from django.shortcuts import render
from day3pjt.settings import BASE_DIR
from .models import Article

# guestbook = []

def index(request):
    # DB에서 가져오기
    guestbook = Article.object.all()
    # SELECT * FROM articles;
    
    return render(request, 'articles/index.html', {'guestbook': guestbook})

def create(request):
    # guestbook.append(content)
    # DB에 저장
    Article.objects.create(content=content)
    
    return render(request, 'articles.create.html', {'content': request.GET.get('content')})
```



===> 위 상태에서 python manage.py runserver 하고 

주소창에 localhost:8000/articles 입력해서 접속하고, 

원하는 방명록 텍스트 입력해보면 DB 가 작동하는 방명록이 계속 남아있음