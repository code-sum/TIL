# ✅ 관점 지향 프로그래밍(AOP) 기본
> _"컴퓨팅에서 관점 지향 프로그래밍(aspect-oriented programming, AOP)은 횡단 관심사(cross-cutting concern)의 분리를 허용함으로써 모듈성을 증가시키는 것이 목적인 프로그래밍 패러다임이다. 코드 그 자체를 수정하지 않는 대신 기존의 코드에 추가 동작(어드바이스)을 추가함으로써 수행하며, "함수의 이름이 'set'으로 시작하면 모든 함수 호출을 기록한다"와 같이 어느 코드가 포인트컷(pointcut) 사양을 통해 수정되는지를 따로 지정한다. 이를 통해 기능의 코드 핵심부를 어수선하게 채우지 않고도 비즈니스 로직에 핵심적이지 않은 동작들을 프로그램에 추가할 수 있게 한다. 관점 지향 프로그래밍은 관점 지향 소프트웨어 개발의 토대를 형성한다."_ [(link)](https://ko.wikipedia.org/wiki/%EA%B4%80%EC%A0%90_%EC%A7%80%ED%96%A5_%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)

- [예시] Logging 기능 적용

  
  > _"AOP의 핵심은 시스템 전반에 넓게 펴져있지만 핵심 비지니스 로직과 무관한 횡단 관심사를 모듈화하는 것입니다. 위에 설명한 로그와 같은 경우가 대표적인 예시입니다."_ [(link)](https://www.qu3vipon.com/fastapi-logging-aop)

  - Spring(Java), FastAPI(Python) 프레임워크를 활용해 서비스를 개발할 때, 매서드마다 logging 처리 코드를 넣거나 print 를 찍는 것은 비효율적이고 코드 유지보수를 어렵게 만들 수 있음
  - 이럴 때 AOP 를 적용해 비핵심 기능인 로그를 모듈화하여 관리하면, 코어단의 코드를 변경하지 않으면서도 HTTP Request / Response 를 기록할 수 있음
  - Spring Boot 프레임워크로 개발 시, AOP 적용하여 HTTP Request Logging 기능 구현한 설명 및 예시 코드 [(link)](https://shortstories.gitbook.io/studybook/spring_ad00_b828_c815_b9ac/aop/baa8-b4e0-c6f9-c694-ccad-c5d0-b300-d574-c11c-b85c-adf8-b85c-b0a8-ae30-ae30) 


- [예시] 인증 기능 적용
  - 브랜디 개발팀이 AOP 적용하여 구현한 인증 기능의 설명 및 예시 코드 [(link)](https://labs.brandi.co.kr//2020/01/07/yangjh.html)
