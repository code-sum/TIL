# 🗂️ Django - ORM 복습

> 2022-09-27
>
> Django 쿼리셋 API / ORM 실습
>
> 
>
> ❓ shell을 사용해서 실습을 진행하는 이유 : 
>
> shell을 활용하는 것은 디버깅과 동일합니다.
>
> 쿼리셋 API를 사용한 복잡한 로직을 구현할 때 view에서 테스트하는 건 제약이 있기 때문에 shell을 활용하는 방법을 배워야 합니다.
>
> [(참고자료1)](https://tutorial.djangogirls.org/ko/django_orm/) [(참고자료2)](http://www.incodom.kr/Django_ORM) [(참고자료3)](https://tibetsandfox.tistory.com/7)



### 실습 안내

shell_plus 터미널에서 아래 실습 문제들을 해결합니다.
각 실습 문제를 해결하는 코드는 각 문제 코드 블럭에 작성합니다.
실습 완료 후 현재 파일 `실습.md` 을 실라버스에 제출합니다.



### 실습 모델 정보

- 모델 이름 : Todo

- 모델 필드

  | 필드 이름  | 역할       | 필드    | 속성              |
  | ---------- | ---------- | ------- | ----------------- |
  | id         | 기본키     |         |                   |
  | content    | 할 일 내용 | Char    | max_length=80     |
  | completed  | 완료 여부  | Boolean | default=False     |
  | priority   | 우선순위   | Integer |                   |
  | created_at | 생성 날짜  | Date    | auto_now_add=True |
  | deadline   | 마감 기한  | Date    | null=True         |



### 실습 사전 작업

1. 압축 풀기

2. 폴더 내 가상환경 생성 및 실행

   ```bash
   python -m venv venv
   
   # window
   . venv/scripts/activate
   
   # mac
   . venv/bin/activate
   ```

3. 패키지 설치

   ```bash
   pip install -r requirements.txt
   ```

4. 서버 정상 실행 확인 후 종료

   ```bash
   python manage.py runserver
   ```

5. **shell_plus** 진입

   ```bash
   python manage.py shell_plus
   ```



---



### 실습 문제

1. 아래 내용의 데이터 추가하기
   - content : 실습 제출
   - priority : 5
   - deadline : 2022-09-27

```py
Todo.objects.create(content='실습 제출', priority='5', deadline='2022-09-27')
```

2. 모든 데이터를 id를 기준으로 오름차순으로 정렬해서 가져오기

```py
todos = Todo.objects.order_by('id')

----[출력]----
for i in Todo.objects.order_by('id'):
    print(i.id, i.content, i.priority, i.completed, i.created_at, i.deadline)
```

3. 모든 데이터를 deadline을 기준으로 내림차순으로 정렬해서 가져오기

```py
todos_dead = Todo.objects.order_by('-deadline')

----[출력]----
for i in Todo.objects.order_by('-deadline'):
    print(i.id, i.content, i.priority, i.completed, i.created_at, i.deadline)
```

4. 모든 데이터를 priority가 높은 순으로 정렬해서 가져오기

```py
todos_prio = Todo.objects.order_by('priority')

----[출력]----
for i in Todo.objects.order_by('priority'):
    print(i.id, i.content, i.priority, i.completed, i.created_at, i.deadline)
```

5. priority가 5인 모든 데이터를 id를 기준으로 오름차순으로 정렬해서 가져오기

```py
todos = Todo.objects.filter(priority='5').order_by('id')

----[출력]----
todos = Todo.objects.filter(priority='5').order_by('id')
for i in todos:
    print(i.id, i.content, i.priority, i.completed, i.created_at, i.deadline)
```

6. completed가 True인 모든 데이터를 id를 기준으로 오름차순으로 정렬해서 가져오기

```py
todos = Todo.objects.filter(completed='True').order_by('id')

----[출력]----
todos = Todo.objects.filter(completed='True').order_by('id')
for i in todos:
    print(i.id, i.content, i.priority, i.completed, i.created_at, i.deadline)
```

7. priority가 5인 데이터의 개수

```py
count = Todo.objects.filter(priority='5').count()
print(count)  // 정답: 16개
```

8. id가 1인 데이터 1개 가져오기

```py
# get() 은 ()안에 작성한 조건에 맞춰 인스턴스를 '단 1개만' 반환

todo = Todo.objects.get(id=1)

----[출력]----
todo = Todo.objects.get(id=1)
print(todo.id, todo.content, todo.priority, todo.completed, todo.created_at, todo.deadline)
```

9. id가 1인 데이터 삭제하기

```py
todo = Todo.objects.get(id=1)
todo.delete()
```

10. id가 10인 데이터의 priority 값을 5로 변경하기

```py
todo = Todo.objects.get(id=10)
todo.priority = 5
todo.save()
```
