# ✅ CMD 명령어 정리

> 1. Linux
> 2. pytest
> 3. pyenv
> 4. Poetry
> 5. Docker



## 1. Linux

- 현재 작업 중인 디렉토리 내부 구성요소 목록 보여주기
  
  > [디렉토리명] 생략하고 `ls` 명령어만 내리는 것도 가능
  
  ```bash
  $ ls [디렉토리명]
  ```
  
- 현재 작업 중인 디렉토리 경로 확인

  ```bash
  $ pwd
  ```

- 홈(=최상위) 디렉토리로 곧장 이동

  ```bash
  $ cd ~
  ```

- 1단계 위 디렉토리로 이동

  ```bash
  $ cd ..
  ```

- 현재 디렉토리에 이름이 't' 로 시작하는 디렉토리가 있다면, 해당 디렉토리명 자동완성

  ```bash
  $ cd t(혹은 다른 문자) + [tab] 키
  ```

- 프로젝트 디렉토리를 VSCODE 로 열기
  - 해당 디렉토리보다 상위에 있을 때
  
    ```bash
    $ code [디렉토리명]
    ```
  
  - 해당 디렉토리에 이미 경로 잡혀있을 때 
  
    ```bash
    $ code .
    ```
  
- 특정 문자를 포함하는 Python 패키지 목록 찾기
  
  - 기본형
  
    ```bash
    $ pip list
    ```
  
  - 응용형
  
    - 작업공간에 설치된 Python 패키지 목록에서 'ra' 를 포함하는 패키지명 검색
    - 특정 패키지의 설치 유무와 버전 정보를 확인하고 싶을 때 유용
    - 'ra' 부분에는 검색하려는 내용을 자유롭게 입력 
  
    ```bash
    $ pip list | grep ra
    ```
  
- 현재 디렉토리 내 숨겨진 파일 확인 (hidden)

  ```bash
  $ .
  ```

- 새로운 파일 생성

  ```bash
  $ touch [파일명.확장자]
  ```

- 해당 파일 내용 확인 (파일 내용을 모두 보여줌)

  ```bash
  $ cat [파일명]
  ```

- a 라는 이름의 파일 변화내역 즉시 모니터링

  ```bash
  $ tail -f a
  ```

- 파일 삭제

  ```bash
  $ rm a.txt
  
  $ rm a.txt b.txt c.txt
  ```

- 빈 폴더 삭제

  ```bash
  $ rmdir temp
  
  $ rm -d temp
  ```

- 파일이 있는 폴더 삭제
  ```bash
  $ rmdir -r temp/
  ```

- 파일이 있는 `fastapi` 폴더 강제 삭제 (삭제 확인 질문하지 않음)
  ```bash
  $ rm -rf fastapi/
  ```




## 2. pytest

- 현재 진입한 디렉토리 내 모든 테스트 실행

  ```bash
  $ pytest
  ```

- 특정 테스트 파일만 실행


  > 코드 내 `print()` 항목까지 테스트 결과에서 확인하고 싶다면 명령어 맨 뒤에 `-s` 파라미터 붙이기 

  ```bash
  $ pytest test_lsg.py

  # print() 항목도 같이 확인하기
  $ pytest test_lsg.py -s
  ```

- 특정 테스트 파일 안에 있는 특정 테스트 함수만 실행


  > 코드 내 `print()` 항목까지 테스트 결과에서 확인하고 싶다면 명령어 맨 뒤에 `-s` 파라미터 붙이기 

  ```bash
  $ pytest test_lsg.py::test_memory

  # print() 항목도 같이 확인하기
  $ pytest test_lsg.py::test_memory -s
  ```




## 3. pyenv

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
  



## 4. Poetry

- `pyproject.toml` 파일 생성

  ```bash
  $ poetry init
  ```

- `pyproject.toml` 에 작성된 의존성 패키지 설치

  ```bash
  $ poetry install
  ```

- `pyproject.toml`  에 작성된 파이썬 가상환경 생성 및 실행

  ```bash
  $ poetry shell
  ```

- 특정 패키지 설치하기 >> `pyproject.toml` 파일 업데이트 됨

  > `pip install` 은 항상 최신 버전 패키지를 설치하지만, `poetry add` 는 설치하려는 패키지들의 의존성을 확인하고 그에 맞게 설치해줌
  
  ```bash
  $ poetry add [패키지명]
  
  $ poetry add fastapi uvicorn
  ```
  
- 특정 패키지 삭제하기

  ```bash
  $ poetry remove [패키지명]
  ```

  

## 5. Docker
> - 공식문서 [(link)](https://docs.docker.com/?_gl=1*1679sz2*_ga*MTg0MDA3MjIwLjE3MDQ0MTQwMTA.*_ga_XJWPQMJYHQ*MTcwNjA1Nzk1NC4zLjEuMTcwNjA1Nzk1Ni41OC4wLjA.)
> - 2023.07 부터 Compose V1 지원이 중단되고 Compose V2 (released in 2020) 사용을 권장하고 있으므로, 이전까지 `docker-compose` 로 작성되었던 명령어도 `docker compose` 로 전환 [(link)](https://docs.docker.com/compose/migrate/)


- 현재 실행중인 컨테이너 목록 확인

  ```bash
  $ docker ps
  ```

- Exited 까지 포함하여 전체 컨테이너 목록 확인

  ```bash
  $ docker ps -a
  ```

- Docker Compose 관련 설정을 확인할 때

  ```bash
  $ docker compose config
  ```

- 다른 경로에 있는 Docker Compose 설정 파일 사용 시, `-f` 옵션

  ```bash
  # 1개의 설정 파일만 사용할 때 (기본형)
  $ docker-compose -f docker-compose-local.yml up
  
  # 2개의 설정 파일을 사용할 때 (뒤쪽 설정이 앞쪽 설정보다 우선함)
  $ docker-compose -f docker-compose.yml -f docker-compose-local.yml up
  ```

- `docker run` vs. `docker exec` vs. `docker attach` 차이점
  
  (1) 새로운 컨테이너를 생성하면서 명령어를 실행할 때

    ```bash
    $ docker container run
    
    $ docker run
    ```

  (2) 이미 실행중인 컨테이너에서 명령어를 실행할 때

    ```bash
    $ docker container exec
    
    $ docker exec
    ```

  (3) 실행 중인 컨테이너에 현재 작업하는 터미널의 표준입출력/에러 처리를 연동 (컨테이너ID, 컨테이너명 활용)
  
    ```bash
    $ docker container attach <the-container-id>
    
    $ docker attach <the-container-id>
    ```
  
- 백그라운드에서 컨테이너를 한 번에 생성하고 실행 시, `up` 활용

  > `-d` 옵션이 없으면, 현재 터미널에 로그가 출력되며 터미널이 종료 시 모든 컨테이너도 종료됨
  > `up` 의 반대 동작은 `down`

  ```bash
  $ docker-compose -f docker-compose.yml up -d 
  ```

- 컨테이너 구동 시작 (특정 컨테이너를 올려줄 때 사용, 보통은 `up` 을 활용)
  > `start` 의 반대 동작은 `stop`

  ```bash
  $ docker-compose start <the-container-id>
  ```

- 컨테이너에서 빠져나오기

  (1) 컨테이너 종료하면서 빠져나오기

  - `exit` 입력 혹은 `ctrl` + `d`

  (2) 컨테이너 가동 상태를 유지하면서 접속만 종료하기

  - `ctrl` + `p` 입력 후 `q`

- 컨테이너 삭제

  - 컨테이너 삭제 전, 멈춤 작업 먼저 하기

    ```bash
    $ docker stop <the-container-id>
    ```
    
  - 컨테이너 삭제

    ```bash
    $ docker rm <the-container-id>
    ```

💡 What's the difference between up, run, and start? [(link)](https://docs.docker.com/compose/faq/#whats-the-difference-between-up-run-and-start)
- `docker compose up`
  - _"Typically, you want docker compose up. Use up to start or restart all the services defined in a compose.yml. In the default "attached" mode, you see all the logs from all the containers. In "detached" mode (-d), Compose exits after starting the containers, but the containers continue to run in the background."_
- `docker compose run`
  - _"The docker compose run command is for running "one-off" or "adhoc" tasks. It requires the service name you want to run and only starts containers for services that the running service depends on. Use run to run tests or perform an administrative task such as removing or adding data to a data volume container. The run command acts like docker run -ti in that it opens an interactive terminal to the container and returns an exit status matching the exit status of the process in the container."_
- `docker compose start`
  - _"The docker compose start command is useful only to restart containers that were previously created but were stopped. It never creates new containers."_


