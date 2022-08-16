-- 테이블 CRUD 실습

-- classmates
-- name: TEXT
-- age: INT
-- address: TEXT

-----------[CREATE]-----------
CREATE TABLE classmates (
    name TEXT,
    age INT,
    address TEXT
);

-- 터미널 창에서 스키마 확인
.schema classmates
-- CREATE TABLE classmates (
--     name TEXT,
--     age INT,
--     address TEXT
-- );

-- classmates 테이블에 새로운 VALUES 추가하기
INSERT INTO classmates (name, age) VALUES ('홍길동', 23);

-- 새로운 VALUES가 잘 추가되었는지 조회/확인
.headers on
.mode column
SELECT * FROM classmates;
-- name  age  address
-- ----  ---  -------
-- 홍길동   23

-- classmates 테이블에 새로운 VALUES 추가하기2
INSERT INTO classmates (name, age, address) VALUES ('홍길동', 30, '서울'); 
INSERT INTO classmates (name, age, address) VALUES ('김철수', 40, '경기'); 
SELECT * FROM classmates;
-- name  age  address
-- ----  ---  -------
-- 홍길동   23
-- 홍길동   30   서울
-- 김철수   40   경기

-- 위 테이블에 표시되지 않은 id 값을 알고 싶다면?
SELECT rowid, * FROM classmates;
-- rowid  name  age  address
-- -----  ----  ---  -------
-- 1      홍길동   23
-- 2      홍길동   30   서울
-- 3      김철수   40   경기

-- rowid는 SQLite에서 자동으로 제공하고 있는 PK. 값이 1씩 증가

-- 위의 결과에서 맨 첫번째 address 값이 NULL 이므로
-- 기존 table 삭제한 다음
-- NULL 값 입력을 허용하지 않는 형태로 다시 작성하기
DROP TABLE classmates;