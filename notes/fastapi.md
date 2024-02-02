# ✅ FastAPI

> 1. 공식문서
> 2. FastAPI 설계 및 구현
> 3. FastAPI 서버 실행



### 1. 공식문서

> *"FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.8+ based on standard Python type hints."* [(link)](https://fastapi.tiangolo.com/ko/)

- **Fast**: Very high performance, on par with **NodeJS** and **Go** (thanks to Starlette and Pydantic). [One of the fastest Python frameworks available](https://fastapi.tiangolo.com/#performance).
- **Fast to code**: Increase the speed to develop features by about 200% to 300%. *
- **Fewer bugs**: Reduce about 40% of human (developer) induced errors. *
- **Intuitive**: Great editor support. Completion everywhere. Less time debugging.
- **Easy**: Designed to be easy to use and learn. Less time reading docs.
- **Short**: Minimize code duplication. Multiple features from each parameter declaration. Fewer bugs.
- **Robust**: Get production-ready code. With automatic interactive documentation.
- **Standards-based**: Based on (and fully compatible with) the open standards for APIs: [OpenAPI](https://github.com/OAI/OpenAPI-Specification) (previously known as Swagger) and [JSON Schema](https://json-schema.org/).



### 2. FastAPI 설계 및 구현

- [Quick Start](https://fastapi.tiangolo.com/ko/tutorial/first-steps/)

  - 메인스크립트 작성

    ```python
    # main.py
    
    from fastapi import FastAPI
    
    app = FastAPI()
    
    @app.get("/")
    async def root():
        return {"message": "Hello World"}
    ```

  - 라이브 서버 실행

    ```bash
    $ uvicorn main:app --reload
    
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
    INFO:     Started reloader process [28720]
    INFO:     Started server process [28722]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
    ```

  - 브라우저 주소창에 http://127.0.0.1:8000/ 입력

  - 아래 JSON 응답 확인

    ```json
    {"message": "Hello World"}
    ```



### 3. FastAPI 서버 실행

- API 구현완료 테스트
  - Postman 활용
    - 메인으로 작성한 스크립트 파일(.py) 먼저 터미널에서 실행
    - **GET / POST** Request 타입 선택
    - URL 입력
    - POST Request 라면, body 에 보내려는 JSON 데이터 입력
    - [send] 버튼 클릭
  - API 문서 화면에서 테스트
    - Swagger UI
      - http://127.0.0.1:8000/docs
    - 다른 방법
      - http://127.0.0.1:8000/redoc
     


### 4. FastAPI Middleware 커스텀
![FastAPI](https://github.com/code-sum/TIL/assets/106902415/ac8e55bb-c148-4840-bef2-e386d5c1027b)
*FastAPI 에서 Middleware 거쳐서 Request 에 대한 Response 출력하는 과정 [(이미지출처)](https://ks1171-park.tistory.com/87)*

- Middleware 커스텀 목적
  - Request URL / Header(*UUID 추가) / Body 로깅 (.log 파일에 기록)
  - Response Status Code / Header(*UUID 추가) / Body 로깅 (.log 파일에 기록)
    *UUID 는 Request 전송 시점마다 새로 발급되며, 이에 대응되는 Response 에도 동일한 UUID 넣어서 짝을 맞춰야 함
- 제약조건
  - .log 파일명에 로깅 처리되는 날짜가 반영되어야 하며, 날짜가 바뀌면 새로운 .log 파일 자동으로 생성하여 로깅 처리
  - OpenAI GPT 모델이 생성한 응답이 `starlette.responses.StreamingResponse` 기반으로 전달되어야 화면에 스트리밍 기능 표출할 수 있음
- 참고자료
  - FastAPI 공식문서 - Middleware [(link)](https://fastapi.tiangolo.com/tutorial/middleware/)
