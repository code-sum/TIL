# ✅단축키 정리

> 1. Linux
> 2. VSCODE
> 3. Eclipse
> 4. Browser
> 5. pyenv



## 1. Linux

- 현재 작업 중인 터미널에서 내렸던 명령어 목록 확인
  - `history`
- 현재 작업 중인 디렉토리 내부 보여주기
  - `ls` + [디렉토리명]
  - [디렉토리명] 은 생략 가능
- 현재 작업 중인 디렉토리 경로 확인
  - `pwd`
- 홈 디렉토리로 바로 이동
  - `cd` + `~`
- 현재 디렉토리에 이름이 t 로 시작하는 디렉토리가 있다면, 해당 디렉토리명 자동완성
  - `cd` + `t` (다른 문자 가능) + [tab] 키
- 프로젝트 디렉토리를 VSCODE 로 열기
  - `code` + [디렉토리명]
    - 해당 디렉토리보다 상위에 있을 때 사용
  - `code` + `.`
    - 해당 디렉토리에 경로 잡혀있는 상황에서 VSCODE 열고 싶을 때 사용
- 숨겨진 파일 확인 (hidden)
  - `.`
- 새로운 파일 생성
  - `touch` + [파일명.확장자]
- 해당 파일 내용 확인 (파일 내용을 모두 보여줌)
  - `cat` + [파일명]
- a 라는 이름의 파일 변화내역 즉시 모니터링
  - `tail -f a` 



## 2. VSCODE

> VSCODE 단축키 관련 튜토리얼 👉 [(link)](https://demun.github.io/vscode-tutorial/shortcuts/)

- 사용자 설정 열기
  - `ctrl` + `,`
- 파일 검색
  - `ctrl` + `p`

- 해당 파일 코드 전체 선택
  - `ctrl` + `a`
- 작업중인 파일에서 특정 코드(단어) 찾기
  - `ctrl` + `f`

- 전체 프로젝트에서 특정 코드(단어) 찾기
  - `ctrl` + `shift` + `f`

- 코드 주석 처리
  - `ctrl` + `/`

- 통합 터미널 열기/닫기
  - `ctrl` + `(물결 기호 넣을 때 누르는 키)

- 창 닫기
  - `ctrl` + `w`
- 똑같은 코드(단어) 동시에 바꾸기
  - 수정하려는 단어 맨 앞에 마우스 클릭하고 `ctrl` + `shift` + `l` 
- 들여쓰기(indentation)
  - 들여쓰기 원하는 코드 전체 드래그 하거나 시작 시점에 마우스 클릭하고 `tab`
- 내어쓰기
  - 내어쓰기 원하는 코드 전체 드래그 하거나 시작 시점에 마우스 클릭하고 `shift` + `tab`
- 특정 라인의 코드를 위/아래줄로 옮기기
  - 옮기고 싶은 범위의 코드 드래그하고 `alt` + `위/아래 방향키`

- VSCODE 컬러 테마 변경
  - `ctrl` + `k` 누르고 1초 후 `ctrl` + `t`



## 3. Eclipse

- 전체 파일명 검색
  - `ctrl` + `shift` + `r`



## 4. Browser

- 크롬 개발자도구 열기
  - `ctrl` + `shift` + `c`
- 로컬에서 코드 수정 작업 마치고 runserver 할 때
  - `ctrl` + `shift` + `r`
  - Chrome also offers the reload shortcut combinations of “Ctrl + F5” and “Ctrl + Shift + R” to reload the currently open page and override the locally cached version.



## 5. pyenv

- 가상환경 신규 생성

  ```bash
  $ pyenv virtualenv [파이썬버전] [가상환경이름]
  ```

- 최상위 디렉토리에 디폴트 가상환경 설정

  - 일단 최상위 디렉토리로 이동

    ```bash
    $ cd ~
    ```

  - 전체 프로그램에 디폴트로 적용하고 싶은 가상환경 활성화

    ```bash
    $ pyenv local [가상환경이름]
    
    $ pyenv local sum-env
    ```

- 현재 PC에 설치된 Python 버전 및 가상환경 목록 확인

  ```bash
  $ pyenv versions
  ```

- 특정 가상환경 활성화

  ```bash
  $ pyenv activate [가상환경이름]
  
  $ pyenv activate sum-env
  ```

- 현재 설정된 가상환경 비활성화 (=종료)

  ```bash
  $ pyenv deactivate
  ```

- 특정 가상환경 삭제

  ```bash
  $ pyenv uninstall [가상환경이름]
  
  $ pyenv uninstall sum-env
  ```

  
