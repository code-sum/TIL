# ✅ 관점 지향 프로그래밍(AOP) 심화 | Middleware 커스텀



### FastAPI Middleware 커스텀

![FastAPI](https://github.com/code-sum/TIL/assets/106902415/ac8e55bb-c148-4840-bef2-e386d5c1027b)
*FastAPI 에서 Middleware 거쳐서 Request 에 대한 Response 출력하는 과정 [(이미지출처)](https://ks1171-park.tistory.com/87)*

- Middleware 커스텀 목적

  > *UUID 는 Request 전송 시점마다 새로 발급되며, 이에 대응되는 Response 에도 동일한 UUID 넣어서 짝을 맞춰야 함

  - **Request** | URL / Header(*UUID 추가) / Body 로깅 (.log 파일에 기록)
  - **Response** | Status Code / Header(*UUID 추가) / Body 로깅 (.log 파일에 기록)

- 제약조건

  - .log 파일명에 로깅 처리되는 날짜가 반영되어야 하며, 날짜가 바뀌면 새로운 .log 파일 자동으로 생성하여 로깅 처리
  - OpenAI GPT 모델이 생성한 응답이 `starlette.responses.StreamingResponse` 기반으로 전달되어야 화면에 스트리밍 기능 표출할 수 있음

- 참고자료

  - [Loguru] 공식문서 [(link)](https://loguru.readthedocs.io/en/stable/)
  - [FastAPI] 공식문서 - Middleware [(link)](https://fastapi.tiangolo.com/tutorial/middleware/)
  - [stackoverflow] How to log raw HTTP request/response in Python FastAPI? [(link)](https://stackoverflow.com/questions/69670125/how-to-log-raw-http-request-response-in-python-fastapi)
  - [CopyProgramming] Logging Request Parameters on a FastAPI Application using Loguru in Python [(link)](https://copyprogramming.com/howto/python-logging-with-loguru-log-request-params-on-fastapi-app)
  - [Post / KOR] FastAPI에서 이벤트 다루는 방법 [(link)](https://hides.kr/1091)
  - [Post / KOR] Fast API - Request/Response 로깅하기 [(link)](https://velog.io/@limelimejiwon/Fast-API-RequestResponse-%EB%A1%9C%EA%B9%85%ED%95%98%EA%B8%B0)

#### 1. Request Info 로깅 처리

> 소스코드 위치 : FastAPI 로 구현된 백엔드 디렉토리 >> `/app` >> `server.py`

- 원리

  - (1) `loguru` 패키지 install
  - (2) `loguru` 패키지 내 `logger` 모듈 import
  - (3) 동기 함수 `log_to_file()` 전역으로 선언하여 ①로거 포맷 세팅, ②기존 로깅 핸들러 제거, ③파일쓰기 방식으로 새로운 로깅 핸들러 추가하는 로직 구현
  - (4) 비동기 함수 `req_log()` 전역으로 선언하여 ①headers UUID 발급 및 추가, ②method, url, headers, body 4개 항목이 파일쓰기로 기록되는 로직 구현 
  - (5) FastAPI `app` 을 선언하고 관련 설정 초기화되는 곳에서 (3)의 전역함수 `log_to_file()` 호출
  - (6) `create_app()` 내에서 `log_to_file()` 호출하기 직전에 `init_routers()` 호출
    - `init_routers()` 는 FastAPI 패키지의 `include_router` 매서드 활용하여 router, dependencies 설정
    - 이 때 dependencies 에 logger 활용해서 Request Info 기록하는 비동기 함수 `req_log` 연결
  - (6) `req_log` 내에 try-except 로직 추가하여 에러메세지까지 기록하게끔 예외처리

- 코드

  ```python
  # ../backend/app/server.py
  
  from loguru import logger
  
  def log_to_file():
    # 로거 포맷 세팅
    logger_format = (
        "<white>{time:YYYY-MM-DD at HH:mm:ss}</white> | "
        "{level} | "
        "<lc>{name}</lc>:<lc>{function}</lc>:<lc>{line}</lc> | "
        "{message}"
    )
    # 기존 로깅 핸들러 모두 제거
    logger.remove()
    # 새로운 로깅 핸들러 추가
    logger.add(
        config.LOG_DIR, colorize=True, enqueue=True,
        rotation="00:00", format=logger_format,
        # allowing the entire stack trace to be displayed, including values of variables
        backtrace=True, diagnose=True)
  ```
  ```python
  def create_app() -> FastAPI:
      app_ = FastAPI(
          title="...",
          description="...",
          version="...",
          docs_url=None,
          redoc_url=None,
          dependencies=[Depends(...)],
          middleware=make_middleware(),
      )
      
      ...
      ...
      init_cache()
      log_to_file() # 해당 함수 주석 처리하면 파일쓰기 하지 않고 콘솔에서 로그 확인 가능
  
      app_.mount("...", ...)
      
      return app_
  
  app = create_app()
  ```

#### 2. Response Info 로깅 처리

> 소스코드 위치 : FastAPI 로 구현된 백엔드 디렉토리 >> `/app` >> `server.py`

- 원리

  - (1) `loguru` 패키지 install
  - (2) `loguru` 패키지 내 `logger` 모듈 import
  - (3) 동기 함수 `log_to_file()` 전역으로 선언하여 ①로거 포맷 세팅, ②기존 로깅 핸들러 제거, ③파일쓰기 방식으로 새로운 로깅 핸들러 추가하는 로직 구현
  - (4) 데코레이터 `@app.middleware('http')` 를 Response Info 로깅 처리하는 함수 상단에 작성 [(link)](https://fastapi.tiangolo.com/tutorial/middleware/)
  - (5) 비동기 함수 `log_middleware()` (4) 의 데코레이터와 함께 선언하여 ①request, response 처리(`call_next` 함수 활용), ②headers UUID 발급 및 추가, ③method, url, headers, body 4개 항목이 파일쓰기로 기록되는 로직 구현
  - (6) LLM 이 chunk 단위로 생성하는 응답을 비동기 방식으로 받아서 ①파일쓰기로 기록(`logger.info`), ②`StreamingResponse` 객체 리턴하는 로직 구현
  - (7) `log_middleware()` 내에 try-except 로직 추가하여 에러메세지까지 기록하게끔 예외처리
  - (8) FastAPI `app` 을 선언하고 관련 설정 초기화되는 곳에서 (3)의 전역함수 `log_to_file()` 호출

- 코드

  ```python
  # ../backend/app/server.py
  
  from loguru import logger
  
  def log_to_file():
    # 로거 포맷 세팅
    logger_format = (
        "<white>{time:YYYY-MM-DD at HH:mm:ss}</white> | "
        "{level} | "
        "<lc>{name}</lc>:<lc>{function}</lc>:<lc>{line}</lc> | "
        "{message}"
    )
    # 기존 로깅 핸들러 모두 제거
    logger.remove()
    # 새로운 로깅 핸들러 추가
    logger.add(
        config.LOG_DIR, colorize=True, enqueue=True,
        rotation="00:00", format=logger_format,
        # allowing the entire stack trace to be displayed, including values of variables
        backtrace=True, diagnose=True)
  ```
  ```python
  def create_app() -> FastAPI:
      app_ = FastAPI(
          title="...",
          description="...",
          version="...",
          docs_url=None,
          redoc_url=None,
          dependencies=[Depends(...)],
          middleware=make_middleware(),
      )
      
      ...
      ...
      init_cache()
      log_to_file() # 해당 함수 주석 처리하면 파일쓰기 하지 않고 콘솔에서 로그 확인 가능
  
      app_.mount("...", ...)
      
      return app_
  
  app = create_app()
  ```
  ```python
  # 기본형

  @app.middleware('http')
  async def log_middleware(request: Request, call_next):
      response = await call_next(request)
      if ("user_uuid" not in response.headers
          and "user_uuid" in request.headers):
          user_uuid = request.headers.get("user_uuid")
          response.headers.__dict__["_list"].append(
              (
                  "user_uuid".encode(),
                  f"{user_uuid}".encode(),
              )
          )    
      
      try: 
          async def generate():
              res_body_chunks = []
              async for chunk in response.body_iterator:
                  yield chunk
                  res_body_chunks.append(chunk.decode())
                  logger.info(f'Response Info: \n- Status Code: {response.status_code} \n- Headers: {response.headers} \n- Body: {res_body_chunks}')
          
          return StreamingResponse(generate(), status_code=response.status_code,
              headers=dict(response.headers), media_type=response.media_type)
      except Exception as e:
          logger.exception(f'Response Info: \n- Status Code: {response.status_code} \n- Headers: {response.headers} \n- ERROR: {e}')
  ```
  
