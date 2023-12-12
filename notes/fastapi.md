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



### 3. FastAPI 서버 실행

- API 구현완료 테스트
  - Postman 활용
    - 메인으로 작성한 스크립트 파일(.py) 먼저 터미널에서 실행
    - **GET / POST** Request 타입 선택
    - URL 입력
    - POST =라면, body 에 보내려는 JSON 데이터 입력
    - [send] 버튼 클릭
  - API 문서 화면에서 테스트
    - Swagger UI
      - http://127.0.0.1:8000/docs
    - 다른 방법
      - http://127.0.0.1:8000/redoc
