# ✅Git 기초 명령어

> 
>
> 본 문서를 이해하는데 도움이 될 개념을 먼저 정리했습니다.

* 기본 개념 및 용어정리
  * 1통: `working directory`, `modified`
    *이 단계에 머문 파일은 파일명이 **붉은 글씨**로 표시 됨*
  * 2통: `staging area` (=임시공간), `add`
    *이 단계에 머문 파일은 파일명이 **초록 글씨**로 표시 됨*
  * 3통: `repository` (=commit)



---



* 작업중인 폴더 내 **새로운 (빈) 폴더** 생성할 때

  ```bash
  $ mkdir 폴더명
  # mkdic = make directory 의미
  # git은 파일 단위로 변화를 감지하기 때문에, 비어있는 폴더를 새로 생성했다고 해서 add, commit 명령어를 입력할 필요는 없음
  ```

* 작업중인 폴더 내 **새로운 파일** 생성할 때

  ```bash
  $ touch 파일명
  # 파일명.csv 와 같이 파일명 옆에 원하는 파일형식 입력 가능
  ```

* 작업중인 폴더 내 **하위 폴더로 이동**해서 작업하고 싶을 때

  ```bash
  $ cd 폴더명
  # cd = change directory 의미
  ```

* 작업중인 폴더보다 **상위 폴더로 이동**해서 작업하고 싶을 때

  ```bash
  $ cd ..
  ```

* **저장소(repository)**를 처음 만들 때

  ```bash
  $ git init
  ```

* 작업하고 있던 저장소를 **삭제**할 때

  ```bash
  $ rm -rf .git
  # GUI에서 [숨은 폴더 표시] 기능을 이용해 .git 파일을 삭제해도 됨
  ```

* 사용자 정보 입력

  ```bash
  # 본격적으로 버전을 기록하기 전에, 아래와 같은 명령어를 이용해 사용자 정보(commit author)를 입력해야 함
  # username 과 email 은 GitHub와 동일해야 함
  $ git config --global user.name "username"
  $ git config --global user.email "my@email.com"
  
  # 설정한 사용자 정보 내역 확인
  $ git config --L
  $ git config --global --L
  $ git config --global --list
  $ git config user.name
  ```

* **버전을 기록**할 때

  ```bash
  $ git add . :현재 디렉토리 중 변경된 파일 모두 2통으로!
  $ git commit -m '커밋하고 싶은 메시지'
  # 1통~2통: add
  # 2통~3통: commit
  
  $ git add 파일명 :특정한 하나의 파일만 수정해서 그 버전을 만들고 싶을 때
  $ git add 파일명 파일명 파일명 :복수의 파일을 하나의 버전으로 만들고 싶을 때
  $ git add . :.gitignore에 기재된 것 고려하여 모두 추가
  $ git add * :.gitignore에 기재된 것 상관없이 모두 추가
  # .gitignore 에 대한 상세정보는 본 문서 하단 참조
  ```

* 현재 상태를 확인할 때

  ```bash
  $ git status :1통, 2통 상태 확인
  $ git log :커밋(=버전) 확인
  
  # log 명령어는 현재 저장소에 기록된 커밋 조회
  $ git log -1
  $ git log --oneline :저장된 커밋들을 간략히 출력
  $ git log -2 --oneline
  ```

* 로컬에서 불필요해진 파일을 삭제한 다음 그 버전을 기록할 때

  ```bash
  $ git add .
  $ git commit -m 'OOO 파일 삭제'
  # 이렇게 커밋을 한 다음 과거 버전으로 돌아가면, 삭제했던 파일이 되살아남
  $ git push origin master
  ```

* 버전 관리와 상관없는 파일을 제외/hide하고 싶을 때

  *.gitignore 는 Git 이 무시하는 목록이다*

  *Git 저장소에 .gitignore 파일을 생성해 해당 내용을 관리하자*

  1. `.gitignore` 파일 생성
  2. `.gitignore` 파일에 무시하고 싶은 파일들을 적어둠
     * 특정 디렉토리: /true_secret
     * 특정 파일: 1.txt(모든 1.txt), test/1.txt(test 폴더의 1.txt)
     * 특정 확장자: *.csv
     * 예외 처리: !2.csv

  💡[개발 언어](https://github.com/github/gitignore)

  💡[프로젝트에 맞는 .gitignore 파일 만들기](https://gitignore.io)