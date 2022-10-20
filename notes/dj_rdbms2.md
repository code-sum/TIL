# ✅1:N (User - Article/Comment)

> 🗂️ [실습]  accounts 앱과 articles 앱 연동하기
>
> 1. User - Article
> 2. User - Comment



- 지금까지 우리는 ...

  - 지금까지의 구현한 서비스에서, 게시글이나 댓글은 누구나 작성할 수 있는 상황입니다.

  - `@login_required` 를 create 함수에 달아도, 글쓴이가 누구인지는 여전히 알 수 없습니다.
  - 따라서 오늘은 로그인된 사용자가 게시글/댓글을 생성, 수정, 삭제할 수 있는 로직을 추가하고, 게시글/댓글을 생성한 사람이 누구인지를 명시적으로 표시해주는 기능을 구현합니다.



- 추가 공부자료

1. AUTH_USER_MODEL 사용하는 이유 [(link)](https://docs.djangoproject.com/en/4.1/ref/applications/#initialization-process)

2. 쿼리셋

   ```python
   user.article_set.all() # article로 이뤄진 QuerySet 
   user.article_set.all()[0] # article 인스턴스 
   user.article_set.all()[0].comment_set.all() # article 인스턴스의 댓글들(comment로 이뤄진 QuerySet) 
   user.article_set.all()[0].comment_set.all()[0] # 그 댓글들 중에 첫번째 
   user.article_set.all()[0].comment_set.all()[0].user # 그 첫번째 댓글의 유저
   ```

3. [django-markdown-editor](https://github.com/agusmakmun/django-markdown-editor) 적용해서 게시글 입력창 수정해보기



## 🗂️ [실습] accounts 앱과 articles 앱 연동하기

> 사용자와 게시글, 사용자와 댓글이 각각 1 : N 관계로 매핑되는 것을 이해하고, 사용자의 프로필에 그동안 작성한 게시글&댓글 목록 출력하는 서비스를 개발합니다.
>
> [선행작업]
>
> 1. [필수] 프로젝트 사전 설정 [(link)](https://github.com/code-sum/TIL/blob/master/notes/dj_modelform2.md)
> 2. [필수] accounts app & User model 생성 [(link)](https://github.com/code-sum/TIL/blob/master/notes/dj_auth.md)
> 3. [필수] 회원관리 서비스 만들기 [(link)](https://github.com/code-sum/CRUD-Practice-5)
> 4. [필수] 게시판 서비스 만들기 [(link)](https://github.com/code-sum/TIL/blob/master/notes/dj_modelform2.md)
> 5. 이미지 관리 기능 추가 [(link)](https://github.com/code-sum/TIL/blob/master/notes/dj_image.md)
> 6. [필수] 댓글 작성 기능 추가 [(link)](https://github.com/code-sum/TIL/blob/master/notes/dj_rdbms1.md)



![221019](https://user-images.githubusercontent.com/106902415/196744386-0e9fa517-9e0a-43d0-94d8-d0b0757b095d.gif)



---



### 1. User - Article

#### 1-1. 모델 관계 설정

```python
# articles/models.py

from django.conf import settings

class Article(models.Model):
    ...
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
```

```bash
# DB 반영

$ python manage.py makemigrations

# 아래와 같은 에러 메세지뜸
You are trying to add a non-nullable field 'user' to article without a default; we can't do that (the database needs something to populate existing rows).Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py
Select an option:

# 위 상황에서 1, 1을 차례로 입력해서 이전에 작성되었던 글 user_id 가 1번 사용자로 모두 채워지도록 조치
$ python manage.py migrate
```

#### 1-2. [CREATE] 인증된 회원의 게시글 작성

```python
# articles/forms.py

'''
create 함수에서 사용하는 ArticleForm 의
fields = '__all__' 부분을 그대로 둔다면
새글쓰기 단계에서 작성자 이름을 선택하는 모양의
폼이 그대로 전달되어 버림
따라서 아래와 같이 필드를 명시적으로 써주거나,
exclude 코드를 활용해서 username 선택할 수 없게끔 만들기
'''

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'image']
        labels = {
            'title': '제목',
            'content' : '내용',
            'image' : '이미지',
    }
```

```python
# articles/views.py

from django.contrib.auth.decorators import login_required

@login_required
def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
            article = article_form.save(commit=False)
            # 로그인한 유저 => 작성자네!
            article.user = request.user 
            article.save()
            return redirect('articles:index')
    else:
        article_form = ArticleForm()
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/new.html', context=context)
```

#### 1-3. [READ] 게시글 작성자 출력

> 작성자 계정을 표현하고 싶은 템플릿에 `{{ article.user.username }}` 코드 넣기
>
> `detail.html` 에서는 작성자 계정을 클릭하면 프로필로 넘어가게끔 `<a>` 태그도 연결

##### 1-3-1. 작성자 이름 출력

```django
<!-- articles/templates/articles/index.html -->

<div class="card-text">{{ article.user.username }}</div>
```

```django
<!-- articles/templates/articles/detail.html -->

<div>
  <a class="text-decoration-none" href="{% url 'accounts:detail' article.user.pk %}">{{ article.user.username }}</a>
</div>
```

##### 1-3-2. [역참조] 프로필 페이지에 해당 사용자가 작성한 글 목록 모두 출력

> 역참조 코드인 `user.article_set.all` 활용
>
> `{{ user.article_set.counter }}` 으로 같은 페이지에 유저가 작성한 글이 총 몇 개인지도 출력

```django
<!-- accounts/templates/accounts/detail.html -->

<div class="mb-4">
  <h4 class="fw-bold">작성한 글</h4>
  <p class="text-muted">{{ user.article_set.count }}개를 작성하였습니다.</p>
  {% for article in user.article_set.all %}
    <p>
      <a class="text-decoration-none" href="{% url 'articles:detail' article.pk %}">{{ article.title }}</a>
    </p>
  {% endfor %}
</div>
```

#### 1-4. [UPDATE] 인증된 회원의 게시글 수정

##### 1-4-1. 수정하기/삭제하기 버튼 묶어서 템플릿 분기하고

```django
<!-- articles/templates/articles/detail.html -->

{% if request.user == article.user %}
  <div class="text-end">
    <a class="btn btn-success" href="{% url 'articles:update' article.pk %}">수정</a>
    <form action="{% url 'articles:delete' article.pk %}" method="POST">
      {% csrf_token %}
      <input type="submit" value="삭제" class="btn btn-danger">
    </form>
  </div>
{% endif %}
```

##### 1-4-2. update 함수도 수정

> 작성자가 아닐 때
>
> (1) 403 에러메시지를 던진다 `HttpResponseForbidden`
>
> (2) flash message 활용 [(link)](https://github.com/code-sum/TIL/blob/master/notes/dj_image.md)

```python
# articles/views.py

from django.http import HttpResponseForbidden

@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
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
    else:
        return HttpResponseForbidden()
```

#### 1-5. [DELETE] 인증된 회원의 게시글 삭제

```python
# articles/views.py

@login_required
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        if request.method == 'POST':
            article.delete()
            return redirect('articles:index')
    else:
        return HttpResponseForbidden()
```



---



### 2. User - Comment

#### 2-1. 모델 관계 설정

```python
# articles/models.py

from django.conf import settings

class Comment(models.Model):
    ...
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
```

```bash
# DB 반영

$ python manage.py makemigrations

# 아래와 같은 에러 메세지뜸
You are trying to add a non-nullable field 'user' to article without a default; we can't do that (the database needs something to populate existing rows).Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py
Select an option:

# 위 상황에서 1, 1을 차례로 입력해서 이전에 작성되었던 글 user_id 가 1번 사용자로 모두 채워지도록 조치
$ python manage.py migrate
```

#### 2-2. [CREATE] 인증된 회원의 댓글 작성

```python
# articles/forms.py

'''
comment_creat 함수에서 사용하는 CommentForm 의
fields = '__all__' 부분을 그대로 둔다면
새글쓰기 단계에서 작성자 이름을 선택하는 모양의
폼이 그대로 전달되어 버림
따라서 아래와 같이 필드를 명시적으로 써주거나,
exclude 코드를 활용해서 username 선택할 수 없게끔 만들기
'''

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={
            "placeholder": "여러분의 댓글을 기다리고 있어요!",
        })
    )
    class Meta:
        model = Comment 
        fields = ['content']
```

```python
# articles/views.py

@login_required
def comment_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
    return redirect('articles:detail', article.pk)
```

```django
<!-- articles/templates/articles/detail.html -->

<!-- 
로그인한 사용자에게만 
댓글 작성 폼이 보이도록
템플릿 분기 처리
-->

<!-- Comments -->
{% if request.user.is_authenticated %}
  <form action="{% url 'articles:comment_create' article.pk %}" method="POST">
    {% csrf_token %}
    {% bootstrap_form comment_form %}
    <div class="d-flex justify-content-end">
      {% bootstrap_button button_type="submit" content="등록" button_class="btn-primary" %}
    </div>
  </form>
{% endif %}
```

#### 2-3. [READ] 댓글 작성자 출력

> 작성자 계정을 표현하고 싶은 템플릿에 `{{ comment.user.username }}` 코드 넣기
>
> `detail.html` 에서는 작성자 계정을 클릭하면 프로필로 넘어가게끔 `<a>` 태그도 연결

##### 2-3-1. 작성자 이름 출력

```html
<!-- articles/templates/articles/detail.html -->

{% for comment in comments %}
  <div class="d-flex">
    <div class="d-flex align-items-center">
      <a class="text-decoration-none" href="{% url 'accounts:detail' comment.user.pk %}">{{ comment.user.username }}</a>&nbsp;|&nbsp;{{ comment.content }}
    </div>
      ... (중략)
```

##### 2-3-2. [역참조] 프로필 페이지에 해당 사용자가 작성한 댓글 목록 모두 출력

> 역참조 코드인 `user.comment_set.all` 활용
>
> `{{ user.comment_set.counter }}` 으로 같은 페이지에 유저가 작성한 댓글이 총 몇 개인지도 출력

```html
<!-- accounts/templates/accounts/detail.html -->

<div class="mb-4">
  <h4 class="fw-bold">작성한 댓글</h4>
  <p class="text-muted">{{ user.comment_set.count }}개를 작성하였습니다.</p>
  {% for comment in user.comment_set.all %}
    <p>
      <a class="text-decoration-none" href="{% url 'articles:detail' comment.article_id %}">{{ comment.content }}</a>
    </p>
  {% endfor %}
</div>
```

#### 2-4. [DELETE] 인증된 회원의 댓글 삭제

##### 2-4-1. 삭제하기 버튼 템플릿 분기하고

```html
<!-- articles/templates/articles/detail.html -->

{% if request.user == comment.user %}
  <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST">
    {% csrf_token %}
    <button type="submit" class="btn btn-outline-danger ms-3">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash" viewbox="0 0 16 16">
        <path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6z"/>
        <path fill-rule="evenodd" d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118zM2.5 3V2h11v1h-11z"/></svg>
    </button>
  </form>
{% endif %}
```

##### 2-4-2. comment_delete 함수도 수정

```python
# articles/views.py

@login_required
def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        if request.method == 'POST':
            comment.delete()
            return redirect('articles:detail', article_pk)
    else:
        return HttpResponseForbidden()
```