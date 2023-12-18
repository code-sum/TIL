# ✅명령어 정리

> 1. Linux
> 2. pyenv



## 1. Linux

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
- 특정 문자를 포함하는 Python 패키지 목록 찾기
  - [기본형] `pip list`
  - [응용형] `pip list | grep ra`
    - 작업공간에 설치된 Python 패키지 목록에서 'ra' 를 포함하는 패키지명 검색
    - 특정 패키지의 설치 유무와 버전 정보를 확인하고 싶을 때 유용
    - 'ra' 부분에는 검색하려는 내용을 자유롭게 입력 
- 숨겨진 파일 확인 (hidden)
  - `.`
- 새로운 파일 생성
  - `touch` + [파일명.확장자]
- 해당 파일 내용 확인 (파일 내용을 모두 보여줌)
  - `cat` + [파일명]
- a 라는 이름의 파일 변화내역 즉시 모니터링
  - `tail -f a` 



## 2. pyenv

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

  
