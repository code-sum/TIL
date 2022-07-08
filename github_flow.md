# ✅GitHub 협업의 흐름

> CLI(command line interface)에서 Git 을 활용하기 전에 항상
>
> $ git status 명령어로 현재 상태를 확인합니다. 



1. Git Flow

   * Git Flow 란?

     * Git 를 활용하는 협업의 흐름, 브랜치를 활용하는 전략
     * 각 프로젝트, 회사의 서비스 상황에 따라 제안되는 흐름이 다름
     
     
   
   * 기능별 브랜치 종류

   ```bash
   master(main) :배포 가능한 상태의 코드
   # 예시 :LOL 클라이언트 라이브 버전(9.23.298.3143)
   
   develop(main) :feature branch로 나뉘거나, 버그 수정 등 개발진행
                  개발 이후 release branch로 갈라짐
   # 예시 :다음 패치를 위한 개발(9.24)
   
   feature branches(supporting) :기능별 개발 브랜치(topic branch)
                                 기능 반영/드랍 이후 브랜치 삭제
   # 예시 :신규챔피언 세나, 드래곤 업데이트
   
   release branches(supporting) :개발 완료후 QA/Test 등을 통해 얻어진
                                 다음 배포 전 minor bug fix 등 반영
   # 예시 :9.24a, 9.24b, ...
   
   hotfixes(supporting) :급하게 반영해야하는 bug fix
                         release branch 이 다음 버전을 위한 것이라면,
                         hotfix branch 는 현재 버전을 위한 것
   # 예시 :긴급 패치를 위한 작업
   ```

   [참고자료](https://nvie.com/posts/a-successful-git-branching-model/)



2. 브랜치 기초 명령어

   * 브랜치 생성

   ```bash
   (master) $ git branch {branch name}
   ```

   * 브랜치 이동

   ```bash
   (master) $ git checkout {branch name}
   ```

   * 브랜치 생성 및 이동

   ```bash
   (master) $ git checkout -b {branch name}
   ```

   * 브랜치 목록

   ```bash
   (master) $ git branch
   ```

   * 브랜치 삭제

   ```bash
   (master) $ git branch -d {branch name}
   ```

   

   💡 [활용] 로컬 저장소에서 브랜치 관리하기

   ```bash
   가지치기를 하기 전에 나무의 뿌리(루트 커밋)를 만들어 주는 과정이 필요하다.
   
   따라서 아래 명령어를 순차적으로 입력해준다.
   
   $ git init
   $ touch README.md
   $ git  add .
   $ git commit -m 'Init'
   
   *master: 기준이 되는 뿌리 브랜치
   
   $ git branch : 현재 '브랜치 조회'
   $ git branch example : example 이라는 이름의 '브랜치 생성'
   $ git checkout example : '브랜치 변경'
   
   작업이 다 끝나면 git status 로 확인
   $ git add . 
   $ git commit -m '변경 내용'
   $ git log --oneline
   
   이 상태에서 $ git checkout master 명령어로 브랜치 이동
   $ git log --oneline 으로 재확인하면
   example 브랜치에서 작성했던 커밋이 사라져있는 것을 확인
   
   *HEAD: 현재 위치하게 된 브랜치를 알려줌
   
   브랜치 병합하기
   $ git checkout master :기준이 되는 브랜치로 이동
   $ git merge example
   $ git log --oneline 으로 HEAD의 흐름이 어떻게 생겼는지 확인
   
   브랜치 지우기
   $ git branch -d example 
   *브랜치를 지워도 지운 브랜치에서 작업했던 커밋이 지워지는 것은 아니다(master에 붙였기 때문)
   *실제로 개발할 때 merge 가 완료된 브랜치는 지워버린다
   ```

   

3. Github Flow

   * Github Flow 기본 원칙 (Github에서 제안하는 브랜치 전략)

     * master branch 는 반드시 배포 가능한 상태여야 함
     * feature branch 는 각 기능의 의도를 알 수 있도록 작성
     * Commit message 는 매우 중요, 명확하게 작성
     * Pull Request 를 활용해 협업 진행
     * 변경사항을 반영하고 싶을 때, master branch 에 병합

     

   * Github Flow Models
     * 위와 같은 기본 원칙 아래, Github 에서 제시하는 2가지 방법

     * **Shared Repository ↔️ Model Fork & Pull Model**
       : 2가지 모델의 차이점은 작업자가 해당 프로젝트 저장소에 직접적인 push 권한을 갖고 있는지 여부
       
       
       
   
   💡원격 저장소(Github)에서 브랜치 관리하기
   
   * 브랜치 이름은 개발을 담당한 사람보단, 기능 이름을 주로 적음
   * Github 로 merge 작업을 수행했다면, 로컬에서는 별도로 merge 작업을 더하지 않아도 됨
   * 다만 Github 에서 merge 해버리면 불필요해진 브랜치는 직접 지워야됨



---



`ctrl + l`터미널 정리



과제: 리드미에 수업후기 작성해서 넣어주세요

```bash
$ git push origin example
# 위와 같이 입력했는데 깃헙에 반영이 안된다면,
# 로컬에서 remote: 부분에 뜬 url을 컨트롤+클릭하면 됨!
```



💡특정 파일에 대한 add 만 취소하고 싶다면?

예시) png 파일, exe 파일을 함께 add 해버렸는데

.exe 에 대한 add 를 취소하고 싶을 때

```bash
$ git restore --staged f.exe
```



💡마크다운 보고서를 저장하지 않았는데, 내용이 지워져있을 때

어떻게 복구해야할까?

커밋, 푸시, 풀 아무것도 안한 상황

```bash
$ git status : 파일이 modified 되었는지 먼저 확인
$ git restore 파일명 : modified 이전 상태로 복구해줌
```



1. 모든 변경사항은 로컬에서 하고, 커밋&푸시하는 연습!



.gitkeep: 빈 폴더를 만들기 위해서 <- git 을 효율적으로 관리하기 위해
(이름 바꾸기 가능)

.gitignore: git 이 추적하지 않는 파일을 관리 <- git 은 모든 디렉토리의 하위 파일을 추적하니까
(이름 바꾸기 불가능)



https://data101.oopy.io/startup-benefits
