# ✅ [TDD] pytest + python-dotenv



#### 1. 목표

- `pytest` 패키지 활용해서 TDD 진행할 때 API Key 등 민감정보를 `.env` 파일로 관리
- 주의사항 : _"`pytest` 의 core 가 `.env` 파일을 지원하지 않으므로, `pytest-dotenv` 패키지 설치하거나 사용하려는 환경변수 파일을 `pytest` 실행 시 옵션으로 직접 입력하여 해결"_ [(link)](https://velog.io/@novo2003/Fastapi-pytest-%EC%82%AC%EC%9A%A9-%EC%8B%9C-%EB%B0%9C%EC%83%9D%ED%95%9C-%EB%AC%B8%EC%A0%9C%EB%93%A4)



#### 2. 구현
> LangSmith API Key, PostgreSQL Connection 정보 관리의 예시
- 패키지 설치

  
  ```bash
  # poetry 로 패키지 관리하는 경우
  $ poetry add pytest
  $ poetry add pytest-dotenv
  
  # pip 로 패키지 관리하는 경우
  $ pip install pytest
  $ pip install pytest-dotenv
  ```
- `pytest.ini` 설정 파일 생성


  ```ini
  [pytest]
  env_override_existing_values = 1
  env_files =
      .env.sample # 루트에 저장한 .env 파일명 입력
  ```
- `.env.sample` 파일에 환경변수로 관리할 민감정보들 입력


  ```.env
  # LangSmith 연결
  LANGCHAIN_TRACING_V2=...
  LANGCHAIN_ENDPOINT=...
  LANGCHAIN_API_KEY=...
  LANGCHAIN_PROJECT=...

  # PostgreSQL 연결
  USERNAME=...
  PASSWORD=...
  HOST=...
  PORT=...
  DBNAME=...
  ```
- 테스트용 소스코드 `test_abcd.py` 와 `.env` 파일 내용 연결

  ```python
  import os, pytest
  from dotenv import load_dotenv
  load_dotenv()

  # LangSmith
  LANGCHAIN_TRACING_V2=os.environ.get("LANGCHAIN_TRACING_V2")
  LANGCHAIN_ENDPOINT=os.environ.get("LANGCHAIN_ENDPOINT")
  LANGCHAIN_API_KEY=os.environ.get("LANGCHAIN_API_KEY")
  LANGCHAIN_PROJECT=os.environ.get("LANGCHAIN_PROJECT")

  # PostgreSQL
  USERNAME=os.environ.get("USERNAME")
  PASSWORD=os.environ.get("PASSWORD")
  HOST=os.environ.get("HOST")
  PORT=os.environ.get("PORT")
  DBNAME=os.environ.get("DBNAME")
  
  DEFAULT_CONNECTION_STRING = f"postgresql+psycopg2://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}"
  ```


#### 3. 결과
- GUI, CLI 방식의 pytest 실행 상황 모두 LangSmith 에서 추적됨
- 테스트 코드에서 구현한 PostgreSQL RDB 조회 기능도 정상 작동

![스크린샷 2024-02-29 111028](https://github.com/code-sum/TIL/assets/106902415/94abc930-bdc7-4f01-833b-9a51ca814447)

![스크린샷 2024-02-29 111045](https://github.com/code-sum/TIL/assets/106902415/4221be7a-2caf-43ce-a3af-718c66af199d)




#### 4. 참고자료

- [Blog] python에서 .env 설정 파일 사용하기 [(link)](https://blog.gilbok.com/how-to-use-dot-env-in-python/)
- [Blog] Fastapi, pytest 사용 시 발생한 문제들 [(link)](https://velog.io/@novo2003/Fastapi-pytest-%EC%82%AC%EC%9A%A9-%EC%8B%9C-%EB%B0%9C%EC%83%9D%ED%95%9C-%EB%AC%B8%EC%A0%9C%EB%93%A4)
- [stackoverflow] PytestUnhandledCoroutineWarning: async def functions are not natively supported and have been skipped [(link)](https://stackoverflow.com/questions/76306054/pytestunhandledcoroutinewarning-async-def-functions-are-not-natively-supported)
