# ✅Django 이미지 관리

> 1. 이미지 업로드
> 2. 이미지 Resizing
> 3. (보너스) The messages framwork
>
> 
>
> +) 인스타그램에 이미지 여러 장 업로드하던 것처럼 기능 구현하고 싶다면?
> (1) 모델 설계(1:N)
> (2) 뷰에서도 반복적으로 저장하게끔 로직 추가 (django modelform multiple images 검색)
>
> +) 부트스트랩 폼을 커스텀하고 싶다면?
> https://pypi.org/project/django-widget-tweaks/



![221017](https://user-images.githubusercontent.com/106902415/196209012-0c3b5a71-6153-4bea-9fb8-2093b871125d.gif)



- 2022-10-17 추가 구현 기능 (`div` 영역 전체에 링크 걸기)

  - 하단 코드와 같이 링크를 걸고 싶은 `div` 에 style, onclick 속성 명시적으로 작성하기

  ```django
  <!-- articles/templates/articles/index.html -->
  
  {% for article in articles %}
          <div class="col-4" style="cursor: pointer;" onclick="location.href='{% url 'articles:detail' article.pk %}'">
            <div class="card" style="width: 18rem;">
              <img src="..." class="card-img-top" alt="...">
              <div class="card-body">
                <h5 class="card-title">{{ article.title }}</h5>
                <p class="card-text">익명1</p>
              </div>
            </div>
          </div>
        {% endfor %}
  ```

  

## 1. 이미지 업로드(기본 설정)

> 가장 먼저 생각해볼 부분은 이미지를 DB에 저장해야하기 때문에, 필드를 추가
>
> 그 다음, 우리가 사용자에게 입력 받을 때 ModelForm 을 사용하고 있기 때문에 이걸 수정해야겠다고 생각하는게 기본
>
> 🗂️ [(참고자료)](https://docs.djangoproject.com/en/4.1/topics/files/) [(참고자료2)](https://djangocentral.com/uploading-images-with-django/)

### 1-1. pillow library 설치

>  **python imaging library 를 활용하는 pillow library** 설치해야 함
>
> 공식 문서 먼저 읽어보고 문서에서 요구하는 방식대로 설치하기 [(link)](https://pillow.readthedocs.io/en/latest/installation.html)

```bash
$ pip install Pillow
$ pip freeze > requirements.txt
```

### 1-2. `ImageField` 정의

```python
# articles/models.py

from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
	image = models.ImageField(upload_to='images/', blank=True)
```

```bash
# DB 반영

$ python manage.py makemigrations
$ python manage.py migrate
```

### 1-3. Form 에도 반영하기

```python
# articles/forms.py
# fields = ['image'] 누락되어 있었다면 추가

from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        labels = {
            'title': '제목',
            'content' : '내용',
            'image' : '이미지',
    }
```

### 1-4. `create` 함수 수정(저장 부분)

```python
# articles/views.py

def create(request):
    if request.method == 'POST':
        # 수정된 코드 👇👇 ArticleForm(request.POST, request.FILES)
        article_form = ArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:index')
    else:
        article_form = ArticleForm()
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/new.html', context=context)
```

### 1-5. `new.html` 템플릿 `<form>` 태그 수정

```django
<!-- articles/templates/articles/new.html -->
<!-- 
추가 코드 : enctype="multipart/form-data"
-->

{% extends 'base.html' %}
{% load django_bootstrap5 %}

{% block content %}
  <div class="row mt-5">
    <h1 class="text-center">글쓰기</h1>
    <form action="" method="POST" enctype="multipart/form-data">
      {% csrf_token %}
      {% bootstrap_form article_form %}
      {% bootstrap_button content="작성완료" button_type="submit" button_class="btn-primary" %}
    </form>
  </div>
{% endblock %}
```

### 1-6. 업로드한 이미지를 `detail.html` 에서 보여주기

```django
<!-- articles/templates/articles/detail.html -->

<img src="{{ article.image.url }}" alt="{{ article.image }}" width="400" height="300">
```

### 1-7. 서버 서빙 설정

> `MEDIA_ROOT`, `MEDIA_URL` 에 대한 공식 문서에서 확인하고 `settings.py`, `urls.py` 에 아래와 같은 코드 추가

```python
# settings.py 

# Media files (user uploaded files)

MEDIA_ROOT = BASE_DIR / 'images'
MEDIA_URL = '/media/'
```

```python
# pjt/urls.py

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```



## 2. 이미지 Resizing

> 서버에 업로드된 이미지들을 너무 좋은 해상도로 관리하면, 서버의 저장 공간도 늘어나고 페이지 로딩도 느리기 때문에 원본 그 자체를 쓰기보단 프로세싱 처리해서 서버에 저장하기
>
> 이미지 관련 다른 처리들도 공식 문서 보면서 따라해보기(워터마크 등)
>
> 🗂️ [(참고자료1)](https://github.com/matthewwithanm/django-imagekit) [(참고자료2)](https://wayhome25.github.io/django/2017/05/11/image-thumbnail/)

### 2-1. django-imagekit 설치

```bash
$ pip install django-imagekit
$ pip freeze > requirements.txt
```

### 2-2. `settings.py` 에 `imagekit` 등록

```python
# settings.py

INSTALLED_APPS = [
    ...,
    'imagekit',
]
```

### 2-3. `ProcessedImage` 필드 추가

```python
# articles/models.py

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = ProcessedImageField(upload_to='images/', blank=True,
                                processors=[ResizeToFill(400, 300)],
                                format='JPEG',
                                options={'quality': 80})
```

```bash
# DB 반영

$ python manage.py makemigrations
$ python manage.py migrate
```

### 2-4. `detail.html` 분기 처리

> 이미지 파일이 없는 게시글들은 눌렀을 때 에러가 뜨기 때문

```django
<!-- articles/templates/articles/detail.html -->

{% if article.image.url %}
    <img src="{{ article.image.url }}" alt="{{ article.image }}" width="400" height="300">
{% endif %}
```

### 2-5. `update` 함수 수정

> `create` 함수처럼, 코드에 `request.FILES` 추가

```python
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, request.FILES, instance=article)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:detail', article.pk)
    else: 
        article_form = ArticleForm(instance=article)
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/update.html', context)
```



## +) `accounts/index.html` 썸네일 반영

```python
# articles/models.py

from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = ProcessedImageField(upload_to='images/', blank=True,
                                processors=[ResizeToFill(400, 300)],
                                format='JPEG',
                                options={'quality': 80})
    thumbnail = ImageSpecField(source='image', 
                                processor=[ResizeToFill(120,80)], 
                                format='JPEG')
```

```bash
# DB 반영

$ python manage.py makemigrations
$ python manage.py migrate
```

```django
<!-- articles/templates/articles/index.html -->

{% if article.thumbnail.url %}
	<img src="{{ article.thumbnail.url }}" class="card-img-top" alt="{{ article.thumbnail }}">
{% endif %}
```



## 3. (보너스) The messages framwork

> 공식문서 : https://docs.djangoproject.com/en/4.1/ref/contrib/messages/
>
> 상세과정은 10.17 강의 2:44:54 참조
>
> 상세코드 : https://github.com/kdt-live/01-django-modelform/commit/d8e46dc179f730b6d3395581c7c97753f464ae0f

