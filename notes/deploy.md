# ✅ AWS + PostgreSQL + Github Actions

> 서비스 배포 가이드 문서 [(link)](https://www.notion.so/hg-edu/839d9d48a1d540ae9509a2009e1722e9) 
>
> 서비스 배포 특강 [(link)](https://www.youtube.com/watch?v=UsW0AbqzfU4)
>



## 1. 배포 서비스 기능 요약

1. AWS S3 : 미디어 파일 저장
2. AWS RDS : 데이터베이스 관리
   - 개발환경에서는 SQLite3 쓰고, 배포환경에서는 AWS RDS 쓰도록 설정

3. AWS Elastic Beanstalk : AWS 버전 헤로쿠

4. Github Actions
   - AWS Elastic Beanstalk 와 함께 써서 자동배포(CI/CD 환경을 구축해서 PR 생성하거나 push 할 때 자동으로 배포 환경에 변경 사항 반영)
   - 인프라 개발자들은 CI/CD 환경 구축하는 업무를 주로 담당
   - CI/CD 서비스는 Github actions 가 제일 유명하고, 젠킨스, travis CI 도 유명




## 2. 배포 강의 포인트

27:37 ~ 44:00 | **AWS S3 강의**

44:00 ~ 59:30 | **AWS RDS 강의**

57:30 ~ 돈이 얼마나 나가고 있는지 체크하고 문제가 되는 서비스 끄기

1:09:20 ~ | **AWS Elastic Beanstalk 강의** 

1:13:30 ~ Django 시크릿 키와 팀에서 쓰고 있는 API 가 따로 있으면 .env 파일에 넣어주기

1:21:45 ~ 1:34:10 | **Github Actions 강의** (deploy.yml 파일에 주석 들어가지 않게 주의!)



## 3. AWS 배포 후, 관리자 계정 생성
