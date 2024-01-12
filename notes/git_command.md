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

  💡`ctrl + l` 작업하고 있던 Terminal 이 너무 길어질 때 한번씩 정리해주는 단축키

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
  
  $ git restore --staged f.exe
  # f.exe 라는 특정 파일에 대한 add 만 취소하고 싶을 때 활용
  
  $ git commit --amend
  # 직전 커밋한 메세지를 수정하고 싶을 때 활용
  # 이 명령어를 입력하면 VSCODE 에 커밋 메세지 수정창이 뜸
  
  $ git add . :.gitignore에 기재된 것 고려하여 모두 추가
  $ git add * :.gitignore에 기재된 것 상관없이 모두 추가
  # .gitignore 에 대한 상세정보는 본 문서 하단 참조
  ```

* 현재 상태를 확인할 때

  ```bash
  $ git status :1통, 2통 상태 확인
  $ git status --ignored  :.gitignore 파일에 기입되어 ignored 상태인 파일목록 확인
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

* 변경된 파일을 복구하고 싶을 때

  *예시) .md 파일을 저장하지 않았는데 내용이 지워져있을 때
           commit, push, pull 아무 것도 안한 절망적인 상황이라면?*

  ```bash
  $ git status :파일이 modified 되었는지 먼저 확인
  $ git restore 파일명 :modified 이전 상태로 복구해줌
  # ctrl+z 단축키가 만능은 아니므로, 위급할 땐 restore 를 활용하자
  ```

* 텅 빈 디렉토리도 commit 하고 싶을 때

  *Git 은 파일이 들어있지 않은 채 비어있는 폴더의 변경사항을 기록하지 않는다*
  *이 때 비어있는 디렉토리도 commit 하고 싶다면 그 안에 .gitkeep 파일을 만든다*
  
```bash
  $ touch 디렉토리명/.gitkeep
  $ git add .
  $ git commit -m 'Adding my empty directory'
```

  💡.gitkeep 은 dummy 기에 파일명도 변경가능하지만, 관용적으로 이 이름을 씀

* 버전 관리와 상관없는 파일을 제외/hide하고 싶을 때

   *Git 은 기본적으로 모든 디렉토리의 하위 파일을 추적한다*
  *이 때 .gitignore 는 Git 이 추적하지 않는 파일을 관리한다(=Git 이 무시하는 목록)*
  *Git 저장소에 .gitignore 파일을 생성해 해당 내용을 관리하자*

  1. `.gitignore` 파일 생성
  
     ```bash
     $ touch .gitignore
     ```
  
  2. `.gitignore` 파일에 무시하고 싶은 파일들을 적어둠
     
     * 특정 디렉토리: /true_secret
     * 특정 파일: 1.txt(모든 1.txt), test/1.txt(test 폴더의 1.txt)
     * 특정 확장자: *.csv
     * 예외 처리: !2.csv
  
  💡[개발 언어](https://github.com/github/gitignore)
  
  💡[프로젝트에 맞는 .gitignore 파일 만들기](https://gitignore.io)
  
  💡.gitignore 파일명은 변경이 불가능

- 커밋하지 않은 변경사항들 임시로 stash 브랜치에 옮겨놓기

  ```bash
  $ git stash drop
  # 가장 최근에 만든 stash 삭제
  
  $ git stash drop stash@{0}
  # 특정 stash id 삭제 (git stash list 입력할 때 확인할 수 있는 id)
  
  $ git stash clear
  # 모든 stash 내역 삭제
  ```

  