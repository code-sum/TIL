# ✅[Git/Github] Upstream, Origin, Local repository

![image](https://github.com/code-sum/TIL/assets/106902415/04bd74a5-99cd-4d3f-ab4c-bb0ba76a3f6c)
[(이미지출처)](https://velog.io/@koominji/Git-%ED%98%91%EC%97%85%ED%95%98%EA%B8%B0-fork-clone-pull-request-fetch-upstream#1-%EC%9B%90%EB%B3%B8-%EC%A0%80%EC%9E%A5%EC%86%8C%EC%97%90%EC%84%9C-%EB%82%98%EC%9D%98-%EC%A0%80%EC%9E%A5%EC%86%8C%EB%A1%9C-fork-%ED%95%B4%EC%98%A4%EA%B8%B0)


### 1. Local repository & Remote repository 

- Local repository
  - 생성방법
    - (1) local 환경에서 프로젝트 진행하려는 empty repository 에 진입한 다음 `git init`
    - (2) Github 에서 생성한 repository 를 `git clone`
- Remote repository
  - remote 는 Github 에 존재하고 있는 repository 를 지칭하며, origin 은 remote repository 에 붙인 이름임

  
    > _"'origin' 도 git clone 명령이 자동으로 만들어주는 리모트 이름이다. git clone -o booyah 라고 옵션을 주고 명령을 실행하면 booyah/master 라고 사용자가 정한 대로 리모트 이름을 생성해준다." [(link)](https://git-scm.com/book/ko/v2/Git-%EB%B8%8C%EB%9E%9C%EC%B9%98-%EB%A6%AC%EB%AA%A8%ED%8A%B8-%EB%B8%8C%EB%9E%9C%EC%B9%98)_
  - local 과 remote 작업 내역을 서로 반영(동기화)하기 위해 `git push` (local 에서 remote 로), `git pull` (remote 에서 local 로)
  - 생성방법
    - (1) local 에서 직접 `git init` 한 경우, `git remote -v` 명령어로 remote 설정을 확인한 다음 `git remote add origin https://github.com/깃헙유저네임/저장소이름.git` 으로 Github 에 생성한 remote repository 를 연결
    - (2) 이미 init 하여 형상관리 되고 있던 repository 를 Github 에서 `git clone` 받은 경우, origin 설정도 되어 있는 상태


### 2. Upstream repository & Downstream repository

- Upstream repository
- Downstream repository
