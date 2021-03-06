# ✅원격저장소 활용(GitHub)

> Git 은 '분산버전관리시스템(DVCS)' 입니다.
> = Git 은 버전, 즉 커밋을 관리합니다.
>
> 분산버전관리시스템은 **원격 저장소(remote repository)**를 이용해 타인과 협업하고, 이전까지의 히스토리를 클라이언트 사이에 공유됩니다.



## 1. 원격 저장소의 종류

* GitHub, GitLab, Bitbucket ...



## 2. 원격 저장소의 기본적인 원리

1. 로컬 저장소에 있던 버전(=커밋)을 원격 저장소로 내보냄

```bash
$ git puch
```

2. 원격 저장소에 있던 버전(커밋)을 로컬 저장소에 내려 받음

```bash
$ git pull
```



## 3. [활용] GitHub로 원격 저장소 생성

1. GitHub 에 로그인하고, `create repository` 선택
2. 저장소 이름과 간단한 설명만 작성하고, 하단 `create repository` 선택
3. [경로 설정 1단계] `vs code` 를 켜고 아래의 명령어 입력

```bash
$ git remote add origin https://github.com/깃헙유저네임/저장소이름.git
```

4. [경로설정 2단계] 아래의 명령어로 원격 저장소 정보를 확인

```bash
$ git remote -v
```

5. [경로설정 3단계] 아래의 명령어로 원격 저장소에 로컬 저장소의 변경 내역(커밋)을 업로드

```bash
$ git push <원격저장소이름> <브랜치이름(수업 편의상 master)>
```



## 4. [활용] GitHub 에서 버전 가져오기

1. 복제를 원하는 github repository 에 접속해서 `Code`  클릭
2. 작업하려는 디렉토리에서 VS code 켜고, 아래 명령어 입력

```bash
$ git clone https://github.com/깃헙계정/저장소이름.git
```

3. 저장소이름으로 새롭게 생성된 파일을 열고, 그 파일의 git 저장소 열기(git bash)
4. 아래 명령어를 입력해 복제된 저장소의 커밋들을 받음

```bash
$ git pull origin master
```

​	

💡 Clone 과 Pull 의 차이

| clone           | pull                     |
| --------------- | ------------------------ |
| 저장소를 받아옴 | (저장소의) 커밋을 받아옴 |



​	💡 github repository 에서 `Code` 를 클릭하면 `Download ZIP` 을 누르고 싶은 충동을 느낄 수 있다. 그러나 이렇게 압축파일을 다운로드하면 최신버전의 '파일 폴더만' 가져오는 것이기 때문에, 버전을 받아오길 원한다면 무조건 `clone` 명령어를 이용하자



---



* 원격 저장소 설정 관련 명령어 정리

| 명령어                            | 내용                               |
| --------------------------------- | ---------------------------------- |
| git clone <url>                   | 원격저장소 복제                    |
| git remote -v                     | 원격저장소 정보 확인               |
| git remote add <원격저장소> <url> | 원격저장소 추가(일반적으로 origin) |
| git remote rm <원격저장소>        | 원격저장소 삭제                    |
| git push <원격저장소> <브랜치>    | 원격저장소에 push                  |
| git pull <원격저장소> <브랜치>    | 원격저장소로부터 pull              |

