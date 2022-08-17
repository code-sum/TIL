-- WHERE 활용

-- 테이블 생성
-- 정호,유,40,전라북도,016-7280-2855,370

CREATE TABLE users (
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    balance INTEGER NOT NULL
);

-- 데이터를 추가
.mode csv
-- 같은 디렉토리에 있는 users.csv 파일을 users 테이블로
.import users.csv users

-- 쿼리

-- 30세 이상인 사람들
SELECT * FROM users WHERE age >= 30;
-- 30세 이상인 사람들의 이름
SELECT first_name FROM users WHERE age >= 30;
-- 30세 이상인 사람들의 이름 3명만
SELECT first_name FROM users WHERE age >= 30 LIMIT 3;
-- 30세 이상이고 성이 김씨인 사람의 나이&이름 출력
SELECT age, first_name FROM users WHERE age >= 30 AND last_name='김';

-- 30세 이상인 사람들의 숫자
SELECT COUNT(*) FROM users WHERE age >= 30;
-- 전체 데이터 중에 가장 작은 나이
SELECT MIN(age) FROM users;
-- 성이 이씨인 사람 중에 가장 어린 사람의 나이
SELECT MIN(age) FROM users WHERE last_name='이';
-- 성이 이씨인 사람 중에 가장 어린 사람의 이름과 계좌잔고
SELECT MIN(age), first_name, balance FROM users WHERE last_name='이';
-- 30세 이상인 사람들의 평균 나이
SELECT AVG(age) FROM users WHERE age >= 30;
-- 계좌 잔액이 가장 많은 사람
SELECT MAX(balance), first_name FROM users;

-- 지역번호가 02인 사람의 수
SELECT COUNT(*) FROM users WHERE phone LIKE '02-%';
-- 이름이 '-준'으로 끝나는 사람의 수
SELECT COUNT(*) FROM users WHERE first_name LIKE '%준';
-- 전화번호 가운데 부분이 5114인 사람의 수
SELECT COUNT(*) FROM users WHERE phone LIKE '%-5114-%';

-- 나이 오름차순으로 정렬된 사람들의 이름을 10명만 출력
SELECT first_name FROM users ORDER BY age ASC LIMIT 10;
-- 나이, 성 순으로 오름차순 10명의 데이터 출력
SELECT * FROM users ORDER BY age, last_name LIMIT 10;
-- 계좌 잔액 내림차순 정렬된 사람들 10명의 이름&성씨&잔고 출력
SELECT last_name, first_name, balance FROM users ORDER BY balance DESC LIMIT 10;
-- 계좌 잔액 내림차순, 성 오름차순 정렬된 사람들 10명의 이름&성씨&잔고 출력
SELECT last_name, first_name, balance FROM users ORDER BY balance DESC, last_name ASC LIMIT 10;
