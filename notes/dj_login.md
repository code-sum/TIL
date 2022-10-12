# ✅Django 로그인에 대한 이해

> 
>
> 🗂️ [실습] 회원관리 서비스 만들기
>
> 1. HTTP & 쿠키(Cookie)
> 2. Login
> 3. Authentication with User
> 4. Logout
> 5. Limiting access to logged-in users



## 🗂️ [실습] 회원관리 서비스 만들기

> Django Auth 를 활용해 회원관리(회원가입/회원목록/프로필/로그인/로그아웃)가 가능한 서비스 개발
>
> 
>
> 1. 프로젝트 사전 설정
> 2. accounts app & User model 생성
> 3. 회원가입, 회원목록, 프로필
> 4. 로그인
> 5. 로그아웃



![221012](https://user-images.githubusercontent.com/106902415/195368518-29b0cb06-11cf-457a-afd7-e47528ed3e38.gif)



### 1. 프로젝트 사전 설정 👉 [(link)](https://github.com/code-sum/TIL/blob/master/notes/dj_modelform2.md)

### 2. accounts app & User model 생성 👉 [(link)](https://github.com/code-sum/TIL/blob/master/notes/dj_auth.md)

### 3. 회원가입, 회원목록, 프로필

#### 3-0. 서비스 메인 페이지

> [GET] http://127.0.0.1:8000/

```python
# pjt/urls.py
# 추가 코드 : path('', views.index, name='index'),

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # 메인화면
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
]
```

```python
# pjt/views.py 생성후 아래와 같이 채움

from django.shortcuts import render

def index(request):
    return render(request, "index.html")
```

```django
<!-- templates/index.html 생성 후 아래와 같이 채움 -->

{% extends 'base.html' %}
{% load django_bootstrap5 %}

{% block content %}
  <div class="row text-center mt-5">
    <h1>회원가입 서비스</h1>
    <!-- Buttons -->
    <div class="form d-flex justify-content-center my-3">
      <a class="btn btn-primary me-3" href="">회원가입</a>
      <a class="btn btn-outline-primary" href="">회원목록</a>
    </div>
  </div>
{% endblock content %}
```

#### 3-1. 회원가입

> [GET] http://127.0.0.1:8000/accounts/signup/

```python
# accounts/forms.py 생성후 아래와 같이 채움

'''
URL-VIEW-TEMPLATE 단계로 넘어가기 전에, 
UserCreationForm() 커스텀하는 단계
'''

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')
        labels = {
            'username': '닉네임',
            'email' : '이메일',
            'password1': '비밀번호',
            'password2': '비밀번호 확인'
    }
```

```python
# accounts/urls.py
# 추가 코드 : path('signup/', views.signup, name='signup'),

from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
]
```

```python
# accounts/views.py

from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    else:     
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)
```

```django
<!-- accounts/templates/accounts/signup.html 생성 -->

{% extends 'base.html' %}
{% load django_bootstrap5 %}

{% block content %}
  <div class="row mt-5">
    <h1 class="text-center">회원가입</h1>
    <form action="" method="POST" class="my-3">
      {% csrf_token %}
      {% bootstrap_form form %}
      {% bootstrap_button button_type="submit" button_class="btn-primary" content="가입하기" %}
    </form>
  </div>

{% endblock content %}
```

```python
# accounts/admin.py

'''
admin 사이트에서도 가입한 회원정보를
한 눈에 볼 수 있게 admin.py 등록하기
'''

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

admin.site.register(get_user_model(), UserAdmin)
```

```django
<!-- templates/index.html -->

<!--
회원가입 기능을 구현했으니
메인화면 [회원가입] 버튼에 url 연결하기
-->

<a class="btn btn-primary me-3" href="{%  url 'accounts:signup' %}">회원가입</a>
```

#### 3-2. 회원조회

```python
# accounts/urls.py
# 추가 코드 : path('', views.index, name="index"),

from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.index, name="index"),
    path('signup/', views.signup, name='signup'),
]
```

```python
# accounts/views.py
# 추가 코드 : index 함수

from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model

def index(request):
    users = get_user_model().objects.all()
    context = {
        "users": users,
    }
    return render(request, "accounts/index.html", context)

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    else:     
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)
```

```django
<!-- accounts/templates/accounts/index.html 생성 -->

{% extends 'base.html' %}
{% load django_bootstrap5 %}

{% block content %}
  <div class="row mt-5">
    <h1 class="text-center">회원목록</h1>
    <!-- Table -->
    <table class="table table-hover mt-3">
      <thead>
        <tr>
          <th scope="col">번호</th>
          <th scope="col">닉네임</th>
          <th scope="col">이메일</th>
        </tr>
      </thead>
      <tbody>
        {% for user in users %}
          <tr>
            <th scope="row">{{ forloop.counter }}</th>
            <td>
              <a href="">{{ user.username }}</a>
            </td>
            <td>{{ user.email }}</td>
          </tr>
        {% endfor %}
      </tbody>
    </table>
  </div>
  <a class="btn btn-primary" href="{% url 'index' %}">처음으로</a>
</div>
{% endblock content %}
```

```django
<!-- templates/index.html -->

<!--
회원목록 기능을 구현했으니
메인화면 [회원목록] 버튼에 url 연결하기
-->

<a class="btn btn-outline-primary" href="{%  url 'accounts:index' %}">회원목록</a>
```

#### 3-3. 프로필

> [GET] http://127.0.0.1:8000/accounts/<user_pk>/
>
> 회원목록 페이지에서 특정 회원의 이름을 누르면 상세보기가 가능하도록

```python
# accounts/urls.py
# 추가 코드 : path('<int:pk>/', views.detail, name='detail'),

from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.index, name="index"),
    path('signup/', views.signup, name='signup'),
    path('<int:pk>/', views.detail, name='detail'),
]
```

```python
# accounts/views.py
# 추가 코드 : detail 함수

from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model

def index(request):
    users = get_user_model().objects.all()
    context = {
        "users": users,
    }
    return render(request, "accounts/index.html", context)

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    else:     
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)

def detail(request, pk):
    user = get_user_model().objects.get(pk=pk)
    context = {
        'user': user
    }
    return render(request, 'accounts/detail.html', context)
```

```django
<!-- accounts/templates/accounts/detail.html 생성 -->

{% extends 'base.html' %}

{% block content %}
  <div class="row mt-5 text-center justify-content-center">
    <h1 class="my-5">{{ user.username }}님의 프로필</h1>
    <p class="mb-4">이메일 :
      {{ user.email }}</p>
    <a href="{% url 'accounts:index' %}" class="btn btn-primary col-2">목록으로</a>
  </div>

{% endblock content %}
```

```django
<!-- accounts/templates/accounts/index.html -->

<!--
프로필 기능을 구현했으니
회원목록 [닉네임] <a>태그에 url 연결하기
-->

<a href="{% url 'accounts:detail' user.pk %}">{{ user.username }}</a>
```

### 4. 로그인

> [POST] http://127.0.0.1:8000/accounts/login/

#### 4-1. 기본 로그인 기능 구현

```python
# accounts/urls.py
# 추가 코드 : path('login/', views.login, name='login'),

from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.index, name="index"),
    path('signup/', views.signup, name='signup'),
    path('<int:pk>/', views.detail, name='detail'),
    path('login/', views.login, name='login'),
]
```

```python
# accounts/views.py
# 추가 코드 : login 함수
# 추가 코드2 : 최상단 from django.contrib.auth import login as auth_login

def login(request):
    if request.method == 'POST':
        # AuthenticationForm은 ModelForm 이 아님!
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # 세션에 저장
            # login 함수는 request, user 객체를 인자로 받음
            # user 객체는 form 에서 인증된 유저 정보
            auth_login(request, form.get_user()) 
            return redirect('accounts:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)
```

```django
<!-- accounts/templates/accounts/login.html 생성 -->

{% extends 'base.html' %}
{% load django_bootstrap5 %}

{% block content %}
  <div class="row mt-5">
    <h1 class="text-center">로그인</h1>
    <form action="" method="POST" class="my-3">
      {% csrf_token %}
      {% bootstrap_form form %}
      {% bootstrap_button button_type="submit" button_class="btn-primary" content="가입하기" %}
    </form>
  </div>

{% endblock content %}
```

```django
<!-- templates/index.html -->
<!-- 메인 화면에 로그인 페이지로 넘어가는 버튼 추가 -->

{% extends 'base.html' %}
{% load django_bootstrap5 %}

{% block content %}
  <div class="row text-center mt-5">
    <h1>환영합니다!</h1>
    <!-- 회원인 경우 -->
    <div>
      <p class="mt-5">회원이신가요?</p>
      <a class="btn btn-warning me-3" href="{%  url 'accounts:login' %}">로그인</a>
    </div>
    <!-- 회원이 아닌 경우 -->
    <div>
      <p class="mt-5">회원이 아니신가요?</p>
      <div class="form d-flex justify-content-center my-3">
        <a class="btn btn-primary me-3" href="{%  url 'accounts:signup' %}">회원가입</a>
        <a class="btn btn-outline-primary" href="{%  url 'accounts:index' %}">비회원으로 계속하기</a>
      </div>
    </div>
  </div>
{% endblock content %}
```

```django
<!-- templates/base.html body 태그 안쪽을 아래와 같이 [if문 분기처리] 작성 --> 
<!-- 조건 1. 로그인 상태일 때, 화면 상단에 사용자의 username 항상 출력 -->
<!-- 조건 2. username 클릭 시, 프로필 페이지로 이동하도록 링크도 추가 -->

<nav class="navbar bg-light">
  <div class="container ms-3 justify-content-start">
    {% if user.is_active %}
          <a class="navbar-brand fw-bold" href="{% url 'accounts:detail' user.pk %}">{{ user }}</a>
    {% else %}
          <a class="navbar-brand fw-bold" href="#">비회원</a>
    {% endif %}
    <span>님 안녕하세요</span>
  </div>
</nav>
<div class="container">
  {% block content %}{% endblock content %}
</div>
```

#### 4-2. 템플릿 분기 처리하기

> 로그인을 했을 때, index.html 에 로그인/회원가입 버튼이 계속 뜨는건 이상하므로 {% if %} ~ {% else %} ~ {% endif %} 로 이어지는 조건문을 작성

```django
<!-- templates/index.html -->

{% extends 'base.html' %}
{% load django_bootstrap5 %}

{% block content %}
  <div class="row text-center mt-5">
    <h1>환영합니다!</h1>
    {% if user.is_authenticated %}
      <!-- 로그인 상태라면 작동하는 코드 -->
      <div>
        <p class="mt-5">로그아웃 하시겠어요?</p>
        <a class="btn btn-danger me-3" href="">로그아웃</a>
      </div>
    {% else %}
      <!-- 로그아웃 상태라면 작동하는 코드 -->
      <!-- 회원인 경우 -->
      <div>
        <p class="mt-5">회원이신가요?</p>
        <a class="btn btn-warning me-3" href="{%  url 'accounts:login' %}">로그인</a>
      </div>
      <!-- 회원이 아닌 경우 -->
      <div>
        <p class="mt-5">회원이 아니신가요?</p>
        <div class="form d-flex justify-content-center my-3">
          <a class="btn btn-primary me-3" href="{%  url 'accounts:signup' %}">회원가입</a>
          <a class="btn btn-outline-primary" href="{%  url 'accounts:index' %}">비회원으로 계속하기</a>
        </div>
      </div>
    {% endif %}
  </div>
{% endblock content %}
```

#### 4-3. `.is_authenticated` `.is_anonymous` 활용하기

> 그러나 위 4-2. 과 같이 템플릿을 분기 처리를 해도 http://127.0.0.1:8000/accounts/login/ 접속하면 회원 상태에서도 여전히 로그인을 또 할 수 있게끔 되어있음(ㅠㅠ) 이런 회원가입(혹은 글쓰기)을 템플릿이 아닌 백엔드 차원에서 막기 위해 views.py 에서 아래와 같이 조건문 추가 (로그인 안되었을 때만 로그인 가능하도록 .user.is_anonymous 을 조건문에 활용하고, 로그인된 상태에서는 해당 url 에 접근해도 accounts/index.html 페이지로 redirect 시켜버리기)

```python
# accounts/views.py
# 수정 코드 : login 함수

def login(request):
    if request.user.is_anonymous:
        if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                auth_login(request, form.get_user()) 
                return redirect('accounts:index')
        else:
            form = AuthenticationForm()
        context = {
            'form': form
        }
        return render(request, 'accounts/login.html', context)
    else:
        return redirect('accounts:index')
```

#### 4-4. `@login_required` : 다음 실습 때 활용법 정리하기(강의 3:05~3:)

> @login_required 데코레이터는 글쓰기/글수정하기에서 비회원의 접근을 막을 때 유용하게 쓸 수 있음

### 5. 로그아웃

> [POST] http://127.0.0.1:8000/accounts/logout/

```python
# accounts/urls.py
# 추가 코드 : path('logout/', views.logout, name='logout'),

from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.index, name="index"),
    path('signup/', views.signup, name='signup'),
    path('<int:pk>/', views.detail, name='detail'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
```

```python
# accounts/views.py
# 추가 코드 : logout 함수
# 추가 코드2 : 최상단 from django.contrib.auth import logout as auth_logout

def logout(request):
    auth_logout(request)
    return redirect('index')
```

```django
<!-- templates/index.html -->

<!-- 
로그아웃 기능 구현했으니
[로그아웃] 버튼에 url 연결하기
-->

<a class="btn btn-danger me-3" href="{% url 'accounts.logout' %}">로그아웃</a>
```

