# ✅ Django URL-VIEW-TEMPLATE



요청과 응답

웹 서비스는 웹을 매개로 전달되는 서비스!

이 서비스의 패턴이 [요청과 응답]이라고 배웠습니다



오프라인 서비스는 주문서 포맷(요청)이나 응답이 다 다르지만, 웹으로 배포된 서비스는 재밌게도 요청(url)과 응답(HTML 문서)이 동일한 패턴

유튜브, 페이스북, 네이버 모두 동일!



장고를 이용해서 이런 요청과 응답을 어떻게 만드는지 살펴보자!

주소창으로 요청 보내는 것을 편하게 만들어 놓은 것이 네이버나 구글의 검색창

naver.com/sise 처럼, 도메인 이름에 + sise 붙여주면 naver 금융 정보가 담긴 HTML 페이지가 바로 뜸



- 요청과 응답

장고는 요청과 응답을 핸들링하는 패턴이 있음

서버의 입장에서는,

- 1)주문서 정의
- 2)로직 구현
- 3)HTML 페이지 구성

이걸 파일 단계에서는,

- 1)URL (urls.py)에 담김
- 2)views.py 에 담김
- 3)template(index.html) 에 담김

 => URL - VIEW - TEMPLATE



- URLs
  - URL => VIEW => TAMPLATE
  - 기초 과정을 작성해보고
  - 데이터의 흐름을 이해하기

```python
# urls.py

# 관리자 화면만 일단 만들어져 있음
# 그 아래에 홈페이지(index.html) path 함수 추가하기
urlpatterns = [
	path('admin/', admin.site.urls),
    path([주문서이름], [어떤 view 파일에서(함수에서) 정의할 것인지 - 로직 구현될 파일]),
] 

------------------------------------

위쪽에
from articles import views 작성해주고,

urlpatterns = [
	path('admin/', admin.site.urls),
    # 주문이 들어오면, views.py 안에 index 가 정의하도록 해라! 하는 명령
    path('index/', views.index),
]

-------------------------------------

# views.py 로 이동
# 위에서 언급했듯 django 는 선언형 프로그래밍이기 때문에 
# 우리가 하고 싶은 작업을 "함수"로 표현만 해주면 됨

from django.shortcuts import render

# Create your views here.

# 함수에 첫번째 인자 아무거나 넣어두기(request) : 아무렇게나 써도 되긴 하는데, 요청한 사람의 정보가 들어가는 자리라서 request 라고 쓰는 것
def index(request):
    # 환영하는 메인 페이지를 보여준다.
    return render(request, 'index.html')

==> 의미: index 라는 함수를 만들어 주는데, 이 함수의 끝은 무언가를 만들면서 끝난다

-----------------------------------

render(request, [템플릿이름], context)
render(request, 'index.html', context) 의 구조임

# articles 폴더(앱) 내에
# 폴더 추가 아이콘 클릭하고 templates 이름의 폴더를 생성 
# (위치, 이름 틀리지 않게 조심)
# templates 폴더 안에 index.html 파일 추가!
# index.html 파일에 사용자에게 보여줄 홈페이지 구조 작성

-----------------------------------

위 URL, VIEW, TEMPLATE 의 구조는 앞으로도 변하지 않음
urls.py, views.py 에 모두 index 라는 이름이 통일되어 활용되고 있음에 주의하자!

-----------------------------------

위와 같이 html 작성된 상태에서 
Git Bash 창에 
python manage.py runserver 해보면 이상한 브라우저 창이 뜨는데

이 주소창 localhost:8000 <- 요 옆에 /index/ 붙여서 다시 엔터키 치면
우리가 만든 html 페이지가 뜸!
```



---



환영합니다 페이지에 이미지 추가하기

```html
<img src="보이고 싶은 .jpg">

파일에 위 코드를 추가하고, Git Bash 에서
python manage.py runserver 다시 입력해줘야
변경된 내용이 반영됨

(끄고 싶을 때는 Git Bash 창에서 ctrl+c)
```



환영합니다 페이지를

정적인데 랜덤한 html 이 뜨도록 작성할수도 있음!

```python
# views.py 로 돌아가서 ... render() 괄호 안에 세번째 요소로 context 추가

from django.shortcuts import render

# Create your views here.

def index(request):
    # 환영하는 메인 페이지를 보여준다.
    return render(request, 'index.html', context)

-----------------------------------

# index 함수 안에 딕셔너리 추가

from django.shortcuts import render

# Create your views here.

def index(request):
    # 환영하는 메인 페이지를 보여준다.
    
    context = {
        'name': '강동주',
        'img': '위에서 추가했던 .img'
    }
    
    return render(request, 'index.html', context)

-----------------------------------

# index.html 로 돌아가서 ...

<body> 안에
	<h1>{{ name }} 님, 환영합니다<h1>
    <img src="위에서 추가했던 .img">
</body>

# 이렇게만 저장해도, 작업하던 웹 페이지 다시 들어가서 새로고침 하면
# 이름이 추가되어 있는 것을 볼 수 있음

-----------------------------------

# 다시 index.html 로 돌아가서 ...

<body>
	<h1>{{ name }} 님, 환영합니다<h1>
    <img src= "{{ img }}">
</body>

# 이렇게만 저장해도, 작업하던 웹 페이지 다시 들어가서 새로고침 하면
# 이미지 잘 들어가있음

-----------------------------------

# views.py 로 들어가서 ...
# 이름이나 인삿말을 여러가지로 바꿔보자

from django.shortcuts import render
import random

# Create your views here.
def index(request):
    # 환영하는 메인 페이지를 보여준다.
    
    names = ['주세환', '오진수', '임수경', '조병진', '차화영', '최근영', '김선교']
    
    random_name = random.choice(names)
    
    context = {
        'name': random_name,
        'img': '위에서 추가했던 .img'
    }
    
    return render(request, 'index.html', context)

```



---



여태까지는 이름 부분이 랜덤하게 출력되는 환영 페이지를 만들었는데

이제부터는 유저와 interaction 하는 주문서 만들기!

먼저, localhost:8000/index/[영어로된이름] 이런 구성으로 주문서가 만들어져야함

```python
# 1단계 : 주문서 만들기
# 먼저 urls.py 클릭
# django에서 변수화된 이름은 <> 표기

urlpatterns = [
	path('admin/', admin.site.urls),
    path('index/', views.index),
    path('welcome/<name(변수화된이름)>/', views.welcome),
] 

------------------------------------------

# views.py 클릭

from django.shortcuts import render
import random

# Create your views here.
def index(request):
    # 환영하는 메인 페이지를 보여준다.
    names = ['주세환', '오진수', '임수경', '조병진', '차화영', '최근영', '김선교']
    random_name = random.choice(names)
    context = {
        'name': random_name,
        'img': '위에서 추가했던 .img'
    }
    return render(request, 'index.html', context)


# name 변수가 urls.py 에서 넘어와서, welcome 함수에서 쓸 예정이라고 명령해주기 
def welcome(request, name):
    # 사람들이 /welcome/본인이름 을 입력하면, 환영 인사와 이름을 동시에 보여준다.
    print(name)
    
    return render(request, 'welcome.html')

------------------------------------------

# template 폴더에 들어가서 ...
# welcome.html 파일을 생성한다

<body>
	<h1>{{  }}님, 환영합니다!</h1>
</body>

------------------------------------------

# 위에서 {{  }} 채워 넣을 생각으로, views.py 클릭!
# 서버 돌릴 때 Bash 에서 오류 뜨면 ctrl+c 하고
# python manage.py runserver 다시 돌리자

------------------------------------------

# localhost:8000/welcome/john/ 주소창에 쳐보면 문제가 또 발생
# views.py 로 다시 돌아가서 ...

def welcome(request, name):
    # 사람들이 /welcome/본인이름 을 입력하면, 환영 인사와 이름을 동시에 보여준다.
    # print(name)
    context = {
        'name': name,
    }
    
    return render(request, 'welcome.html', context)

------------------------------------------

# template 폴더 - welcome.html 파일로 돌아가서 ...

<body>
	<h1>{{ name }}님, 환영합니다!</h1>
</body>

# 위와 같이 name 변수 넣어주고 서버 다시 돌려보면,
# localhost:8000/welcome/[이름] 이렇게 주소 넣었을 때
# 메인 화면에 [이름]님, 환영합니다! 문구가 뜸
```



---



이미지 여러개를 띄우고 싶으면?

```python
# views.py ...

def welcome(request, name):
    # 사람들이 /welcome/본인이름 을 입력하면, 환영 인사와 이름을 동시에 보여준다.
    # print(name)
    context = {
        'name': name,
        'img1': '~.jpg'
        'img2': '~.jpg'
        'img3': '~.jpg'
    }
    
    return render(request, 'welcome.html', context)

# 위와 같이 이미지 하나하나 넣으면 번거로우니까
# 아래와 같이 알고리드믹하게 작성

-------------------------------------

def welcome(request, name):
    # 사람들이 /welcome/본인이름 을 입력하면, 환영 인사와 이름을 동시에 보여준다.
    # print(name)
    context = {
        'name': name,
        'images': [
            '~.jpg',
            '~.jpg',
            '~.jpg'
        ],
        'greetings': [
            '안녕하세요', 'Hi', 'Hello'
        ]
    }
    
    return render(request, 'welcome.html', context)

----------------------------------------

# welcome.html ...
# {%  %} 부분은 django 가 만들어준 템플릿 랭귀지(DTL, django template language)

<body>
	<h1>{{ name }}님, 환영합니다!</h1>
    <p>{{ greetings }}</p>
    {% for greeting in greetings %}
    	<p>{{  greeting  }}</p>
    {% endfor %}
    
    <!-- for greeting in greetings -->
    <!-- print(greeting)
</body>
```

