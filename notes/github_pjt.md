# ✅Git/Github 프로젝트에 적용하기

> 1. 프로젝트 시작
> 2. 프로젝트 진행
> 3. 프로젝트 종료(저장소 Mirror)
>
> 
>
> 작업 순서는 문서 위에서 아래로 읽어가면서 진행



## 1. 프로젝트 시작

- **1번 팀원**이 저장소 생성 (저장소 이름은 자유)
  
  - Settings 클릭
  - 왼쪽에서 Collaborators 클릭
  - Add people 클릭
  - 모달창에서 2번 팀원의 계정 검색해서 추가
  
- **2번 팀원**이 개인 이메일 확인
  
  - View invitaion 클릭
  - Accept invitaion 클릭
  - 이렇게 되면 두 사람 모두 저장소에 대한 권한을 똑같이 가진 것
  
- **1번 팀원**이 프로젝트 세팅
  
  - VSCODE 열어서 프로젝트 진행할 폴더에 가상환경(venv) 생성 & 활성화
  
    ```bash
    $ python -m venv venv
    $ source venv/Scripts/activate
    (venv)
    ```
  
  - 필요한 패키지 설치 및 기록
  
    ```bash
    # upgrade pip
    $ python -m pip install --upgrade pip
    
    # install packages 
    $ pip install django==3.2.13
    $ pip install django-bootstrap5
    
    # 팀원들이 동일한 패키지 공유하도록 기록지에 남기기
    $ pip freeze > requirements.txt
    ```
  
  - Django 프로젝트 생성 / 🗂️ [(프로젝트 추가설정)](https://github.com/code-sum/TIL/blob/master/notes/dj_modelform2.md)
  
    ```bash
    # 현재 위치(.)에 pjt 라는 이름의 프로젝트를 생성
    $ django-admin startproject pjt .
    
    # 서버 실행되는지 확인
    $ python manage.py runserver
    
    # .gitignore 파일 프로젝트 진행하는 폴더에 넣고 git 추적 시작
    $ git init
    $ git add .
    $ git commit -m 'init'
    $ git remote add origin [원격저장소 링크]
    $ git push -u origin master(or main)
    ```
  
  - 여기까지 세팅하면 모든 팀원이 push 가능
  
- **2번 팀원**은 1번 팀원이 세팅한 프로젝트를 받아오고 작업 시작(예시: 앱 생성)

  - 해당 원격저장소를 로컬에 clone 하기

    ```bash
    $ git clone [원격저장소주소]
    ```

  - 1번 팀원이 작성한 가상환경과 똑같은 이름으로 가상환경(venv) 생성 & 활성화

    ```bash
    $ python -m venv venv
    $ source venv/Scripts/activate
    (venv)
    ```

  - 프로젝트에 세팅된 패키지 받아오기

    ```bash
    $ pip install -r requirements.txt
    ```

  - 작업 시작(예시: 앱 생성 및 등록)

    ```bash
    $ python manage.py startapp articles
    ```

    ```python
    # pjt/settings.py
    
    # INSTALLED_APPS = [] 괄호 내 최상단에 아래와 같이 생성한 앱 등록
    
    INSTALLED_APPS = [
        'articles',
        ...,
    ]
    ```

    ```bash
    $ git add .
    $ git commit -m '2번 팀원이 작업한 내용'
    $ git push origin master(or main)
    ```

- **1번 팀원**이 2번 팀원의 commit 내용 pull 로 받기

  ```bash
  $ git pull origin master(or main)
  ```

- 이 상태로 개발 시작



---



## 2. 프로젝트 진행

### 2-1. 드라이버 / 네비게이터 전환 방식

> 핵심 : 항상 두 사람이 같은 코드를 유지해야함

- 역할 분담

  - 드라이버인 사람 담당 : add / commit / push
  - 네비게이터인 사람 담당 : pull

- [주의] DB 이슈

  - `db.splite3` 파일이 원격저장소에 올라가면 회원정보나 게시글/댓글 정보가 노출되는 위험이 있기 때문에, `.gitignore` 에 `.splite3` 를 적어준다.

  - 따라서 드라이버를 전환할 때, 이전 드라이버가 작업하던 DB를 인계받지 못하는 이슈가 생긴다.

  - 그러나 `migrations` 파일은 서로 공유할 수 있다.

  - 그러므로 특정 드라이버가 모델을 변경하고 다음 드라이버에게 바톤터치할 때, pull 받은 드라이버는 꼭 migrate 를 해야 변경된 DB로 작업할 수 있다 (국룰임)

    ```bash
    # models.py 변경한 드라이버 시점
    $ python manage.py makemigrations
    $ python manage.py migrate
    $ git add .
    $ git commit -m '모델 변경'
    $ git push origin master
    
    # 다음 타자 드라이버 시점
    $ git pull origin master
    $ python manage.py migrate
    ```

- [주의] 프로젝트 도중 패키지를 추가 설치했다면?

  ```bash
  $ git pull origin master(or main)
  $ pip install -r requirements.txt
  ```

### 2-2. 브랜치 나눠서 여러 기능을 동시에 구현하는 방식

#### 2-2-1. 가상환경 꼭 켜기

```bash
$ source venv/Scripts/activate
(venv)
```

#### 2-2-2. 구현하고 싶은 기능 이름따서 브랜치 생성

> 브랜치 이름에 오타 생기면 👉 $ git branch -m [기존브랜치이름] [바꿀브랜치이름]

```bash
$ git checkout -b [새브랜치이름]
```

#### 2-2-3. 브랜치 이름 잘 확인하고 개발 진행

>  `master(or main)` 에서 작업하지 않도록 항상 신경쓰자! 

#### 2-2-4. 각 브랜치에서 목표했던 기능 구현이 끝나면 commit / push

> add / commit / push 하기 전에 브랜치 이름 한번 더 확인!

```bash
$ git add .
$ git commit -m 'OOO 기능 구현'
$ git push origin [새로따서작업하던브랜치이름]
```

#### 2-2-5. Github 원격저장소로 넘어가기

- 원격저장소에서 PR 생성(`Compare & pull request` 클릭)
- 브랜치 병합(`Create pull request `, `Merge pull request`, `Delete branch` 차례로 클릭)

#### 2-2-6. 로컬저장소에서 뒷정리

- master (or main) 브랜치로 전환 후 pull

  ```bash
  # master(or main) 브랜치로 전환
  $ git checkout master(or main)
  
  # master(or main) 브랜치 Pull
  $ git pull origin master(or main)
  ```

- 기능 구현이 끝난 곁가지 삭제

  ```bash
  $ git branch -d [새로따서작업하던브랜치이름]
  ```



---



## 3. 프로젝트 종료(저장소 Mirror)

>  - 위 과정이 종료되면, 처음에 원격저장소를 생성한 1번 팀원의 Github 계정에만 저장소가 위치하고 있기 때문에 저장소 Mirror 작업으로 2번, 3번, ... N번 팀원의 Github 계정에 동일한 저장소를 공유
>  - 1번 팀원은 아래 내용을 따라하지 않아도 됨

### 3-1. Github 원격저장소 생성

- Github 메인 화면에서 `Create a new repository` 클릭해서 진행

### 3-2. 프로젝트 하던 1번 팀원의 원격저장소를 로컬에 clone

> 아래 코드로 안되면 $ git clone --bare [1번팀원의기존원격저장소주소] 코드로 진행해보기

```bash
$ cd [작업할(=비어있는)폴더이름]
$ git clone --mirror [1번팀원의기존원격저장소주소]
$ cd [1번팀원의저장소이름]
```

### 3-3. 복사한 저장소의 원격저장소 설정

```bash
$ git remote set-url --push origin [2번팀원의새로운원격저장소주소]
```

#### 3-4. Push 

```bash
$ git push --mirror
```
