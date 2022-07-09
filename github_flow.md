# ✅GitHub 협업의 흐름

> CLI(command line interface)에서 Git 을 활용하기 전에 항상
> $ git status 명령어로 현재 상태를 확인합니다. 
>
> 각 기능별 버전관리는 로컬에서 진행하여 커밋하고,
> 이를 원격저장소에 push 하는 연습을 반복합니다.



## 1. Git Flow

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



## 2. 브랜치 기초 명령어

   * 브랜치 생성

   ```bash
   (master) $ git branch {branch name}
   # 브랜치 이름은 개발을 담당한 사람보단, 기능 이름을 주로 적음
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
   나무의 가지가 뻗어나가듯 기능별 브랜치를 확장하기 전에,
   기준이 되는 가지, 즉 뿌리 역할을 해주는 가지를 만들어야 한다.
   아래 1~5단계 명령어를 순차적으로 입력해 기준 브랜치를 만들고
   각 기능별 브랜치를 병합(merge)하는 작업까지 완료해보자.
   
   # 1단계, 기준이 되는 브랜치 생성하기
   $ git init
   $ touch README.md
   $ git add .
   $ git commit -m 'Init'
   
   *본 실습에서는 (master)가 기준이 되는 뿌리 브랜치
   
   # 2단계, 새로운 브랜치 생성하기
   $ git branch :현재 브랜치 조회
   $ git branch example :'example' 이라는 이름의 브랜치 생성
   $ git checkout example :작업중인 브랜치에서 (example)로 브랜치 변경
   
   (example) 브랜치에 해당하는 기능별 변경 작업 진행
   
   # 3단계, 새로운 브랜치에서 버전 기록하기
   $ git status :작업이 다 끝난 후 상태 확인
   $ git add . 
   $ git commit -m '변경 내용'
   $ git log --oneline
   
   $ git checkout master :기준이 되던 (master)로 브랜치 이동
   $ git log --oneline :이때 (example) 브랜치에서 작성했던 커밋들은 
                        사라져있는 것을 확인할 수 있음
   
   *HEAD: 현재 위치하고 있는 브랜치를 알려줌
   
   # 4단계, 로컬 저장소에서 브랜치 병합하기
   $ git checkout master :기준이 되던 (master)로 브랜치 이동
   $ git merge example :(master)에 (example)를 병합
   $ git log --oneline :HEAD의 흐름이 어떻게 진행되었는지 확인
   
   # 5단계, 불필요해진 브랜치 지우기
   $ git branch -d example 
   
   *특정 브랜치를 지워도 지운 브랜치에서 작업했던 커밋까지
    지워지는 것은 아니다 (이미 master 브랜치에 붙였기 때문)
   *실제로 개발할 때 merge 가 완료된 브랜치는 지워버린다
   ```

   

## 3. Github Flow

   * Github Flow 기본 원칙 (Github에서 제안하는 브랜치 전략)

     * master branch 는 반드시 배포 가능한 상태여야 함
     * feature branch 는 각 기능의 의도를 알 수 있도록 작성
     * Commit message 는 매우 중요, 명확하게 작성
     * Pull Request 를 활용해 협업 진행
     * 변경사항을 반영하고 싶을 때, master branch 에 병합

     

   * Github Flow Models
     * 위와 같은 기본 원칙 아래, Github 에서 제시하는 2가지 방법

     * **Shared Repository Model ↔️ Fork & Pull Model**
       : 2가지 모델의 차이점은 작업자가 해당 프로젝트 저장소에 
        직접적인 push 권한을 갖고 있는지 여부
       
       
       

   💡[활용] 원격 저장소(Github)에서 브랜치 관리하기
                                                       *Fork & Pull Request Model 의 예시*

```bash
# 1단계, 떠오고 싶은 원격저장소 Fork 하기
  1) 특정 원격저장소 우측상단에서 Fork 클릭
  2) 본인의 원격저장소에 저장될 이름 작성후 Creat fork 클릭
  3) 본인의 원격저장소에서 Fork 작업이 완료되었는지 확인
  
# 2단계, Fork 했던 원격저장소를 로컬에 Clone 하기
  1) Fork 완료된 원격저장소에서 Code 클릭
  2) 원격저장소 url 복사
  3) 바탕화면에서 VS code 켜고 아래 명령어 입력
     $ git clone https://github.com/깃헙계정/저장소이름.git
  4) 아래 명령어로 신규 브랜치를 생성하고 이동
     $ git branch example
     $ git checkout example

# 3단계, 작업완료 후, 변경사항을 add, commit, push
$ git add .
$ git commit -m "OOO 변경"
$ git push origin example
*만약 여기까지 입력했는데 Github 에 반영이 안된다면
 로컬 terminal 에서 remote: 부분에 뜬 url 을 ctrl+클릭하면 됨!

# 4단계, Pull Request 작업 진행하기
  1) Github 에서 Compare & pull request 클릭
  2) base repository <- head repository 제대로 되었는지 확인
  3) pull request 내용을 작성하고 Creat pull request 클릭

💡 이렇게 Github 로 merge 작업을 수행했다면, 
   로컬에서는 별도로 merge 작업을 더하지 않아도 됨
💡 다만 Github 에서 merge 해버리면 불필요해진 브랜치는 직접 지워야됨
```
