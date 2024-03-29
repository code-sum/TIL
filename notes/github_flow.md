# ✅[Git/Github] 협업의 흐름

> 
>
> CLI(command line interface)에서 Git 을 활용하기 전에 항상
> $ git status 명령어로 현재 상태를 확인합니다. 
>
> 각 기능별 버전관리는 로컬에서 진행하여 커밋하고,
> 이를 원격저장소에 push 하는 연습을 반복합니다.



## 1. Git Flow

   * Git Flow 란?

     * Git 를 활용하는 협업의 흐름, 브랜치를 활용하는 전략
     * 각 프로젝트, 회사의 서비스 상황에 따라 제안되는 흐름이 다름
     



- Git 브랜치 관리
  - 브랜치는 저장소의 새로운 분할
  - 브랜치 확인
    - 로컬 브랜치 목록 출력
    - `git branch --list`
  - 모든 브랜치 목록 확인
    - `git branch --all`



- 기능별 브랜치 종류 [(link)](https://nvie.com/posts/a-successful-git-branching-model/)


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



## 2. 브랜치 기초 명령어

* 새로운 브랜치 생성

  ```bash
  (master) $ git branch {branch name}
  # 브랜치 이름은 개발을 담당한 사람보단, 기능 이름을 주로 적음
  ```

* 브랜치 이동 (switch, 이렇게 이동하면 작업 공간이 바뀌는 것)

  ```bash
  (master) $ git checkout {branch name}
  ```

* 브랜치 생성과 동시에 이동하기

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
  (master) $ git branch --delete {branch name}
  ```

* 브랜치 강제 삭제
  > 위 명령어는 merge 되지 않은 브랜치를 삭제할 때 에러가 나므로, 아래 명령어로 강제 삭제

  ```bash
  (master) $ git branch -D {branch name}
  (master) $ git branch --delete --force {branch name}
  ```

* 브랜치 이름 변경

  ```bash
  (master) $ git branch -m {old-branch} {new-branch}
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
   $ git branch --list :브랜치 생성이 정상적으로 이뤄졌는지 확인
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
       - 위 2가지 모델의 차이점은 작업자가 해당 프로젝트 저장소에 직접적인 push 권한을 갖고 있는지 여부
       
       
       

💡[활용] 원격 저장소(Github)에서 브랜치 관리하기
  > *Fork & Pull Request Model 의 예시*

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
$ git commit -m 'OOO 변경'
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



- Git 브랜치 합치는 방법
  > * (1) Merge
  > * (2) Rebase


  - (1) Merge 방식으로 브랜치 합치기

      - 변경 내용을 병합하기 전에 비교(diff)
   
        
        ```bash
        $ git diff {원본 브랜치} {대상 브랜치}
        $ git diff master hotfix
        $ git diff master origin/master        
        ```

      - 예시: (master) 브랜치에 (hotfix) 브랜치를 병합

  
        ```bash
        $ git checkout master
        $ git merge hotfix
        ```
      
      - 예시2: (master) 브랜치에 (origin/master) 브랜치를 병합 [로컬에 원격 브랜치 병합]
   

        ```bash
        $ git checkout master
        $ git diff master origin/master
        $ git merge origin/master
        ```
      
      - Conflict(충돌) 해결: Merge 하다가 충돌이 발생했을 때 >> 일단 병합 취소하기
   

        ```bash
        $ git merge --abort
        ```

      
      - 위 코드로 병합 취소했다면, 충돌하는 파일을 수정 후 add, commit
   

        ```bash
        $ git add {conflict-filename}
        $ git commit -m "[merge] message"
        ```


  - (2) Rebase 방식으로 브랜치 합치기
       * 용도 : 저장소 upstream 설정작업 후, upstream 의 변경사항을 프로젝트에 빠르게 반영하면서 작업하고 싶을 때 유용함
       * 원리 : feature 브랜치의 작업 내역을 upstream 의 (main) 혹은 upstream 의 (master) 가장 최근 커밋에 Rebase
       * 참고자료
         * [공식문서] Git 브랜치 - Rebase 하기 [(link)](https://git-scm.com/book/ko/v2/Git-%EB%B8%8C%EB%9E%9C%EC%B9%98-Rebase-%ED%95%98%EA%B8%B0)
         * [블로그] Git Rebase 제대로 알고 쓰기 (feat. cherry-pick) [(link)](https://readystory.tistory.com/151)
       * Git Graph GUI 활용하는 방법
          * Git Graph GUI 에서 `Rebase current branch on this commit` 클릭
          * 새로 뜨는 알림창에서 Ignore Date 체크 확인하고, Yes, rebase 클릭

             ![rebase](https://github.com/code-sum/TIL/assets/106902415/7b916814-50ac-4c07-b483-cd6c9f60e874)
             
       * CLI 명령어 활용하는 방법
         ```bash
          
          # 다른 브랜치를 병합할 때 rebase를 먼저 실행한 후 병합을 하면 이력을 하나의 줄기로 만듦
          # (issue) 브랜치에 (master) 브랜치를 rebase 한 후
          $ git checkout issue
          $ git rebase master
          
          # 충돌이 발생하면 충돌 파일을 변경
          # 충돌 부분을 수정 한 후에는 commit 이 아니라 rebase --continue 옵션으로 rebase 수행
          
          $ git add hello.txt
          $ git rebase --continue 또는 $ git rebase --abort
          # master에 issue 브랜치의 변경 사항을 모두 병합
          # master와 issue는 동일한 HEAD를 가리키고 있으며 이력이 하나의 줄기로 만들어짐
          
          $ git checkout master
          $ git merge issue
         ```

- Cherry Pick 활용


  > _"git-cherry-pick - Apply the changes introduced by some existing commits"_ [(link)](https://git-scm.com/docs/git-cherry-pick)

  - 용도 : 현재 작업하는 브랜치가 어디인지에 상관없이 동료 개발자가 다른 브랜치에서 커밋한 코드 작성 내역을 바로 가져오고 싶을 때
  - 활용법 (Git Graph - GUI)
    - (1) `git fetch` 명령어 먼저 내려서 어떤 commit 이 원격저장소에 push 되었는지 확인
    - (2) 복사해 오려는 commit 마우스 오른쪽 버튼 클릭하여 `Cherry Pick...` 버튼 클릭
   
      
      ![스크린샷 2024-03-04 172019](https://github.com/code-sum/TIL/assets/106902415/ce388279-eabf-48dc-a6fc-b3f05e0c3b1e)
    - (3) `No commit` 옵션 선택하고, `Yes, cherry pick` 버튼 클릭
   
      
      ![스크린샷 2024-03-04 172041](https://github.com/code-sum/TIL/assets/106902415/beb1567b-d932-4449-83ca-085fcda361c6)
