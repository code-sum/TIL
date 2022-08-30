-- 테이블 CRUD 실습2

-- 02.classmates.sql 파일에 이어서
-- 제약조건이 있는 table 작성 단계부터 시작

-----------[CREATE]-----------

CREATE TABLE classmates (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INT NOT NULL,
    address TEXT NOT NULL
);

.schema classmates
-- CREATE TABLE classmates (
--     id INTEGER PRIMARY KEY,
--     name TEXT NOT NULL,
--     age INT NOT NULL,
--     address TEXT NOT NULL
-- );

-- classmates 테이블에 새로운 VALUES 추가할 때
-- 스키마에 id를 직접 작성했기 때문에,
-- 입력할 column 들을 명시해야 오류가 안남
-- 아래 2가지 방법중 하나 선택해서 VALUES 추가하기

-- 방법1. id를 포함한 모든 VALUES 를 작성
INSERT INTO classmates VALUES (1, '홍길동', 30, '서울');
-- 방법2. 각 value에 맞는 column들을 명시적으로 작성
INSERT INTO classmates (name, age, address) VALUES ('홍길동', 30, '서울');

-- 위와 같이 id를 PK로 할당하지 않고도
-- rowid를 활용해서 편하게 값들을 추가할 수 있다
-- 이 작업을 위해 현재까지 작업한 table 삭제하고
-- PK가 없는 새로운 table 을 작성
DROP TABLE classmates;

CREATE TABLE classmates (
    name TEXT NOT NULL,
    age INT NOT NULL,
    address TEXT NOT NULL
);

-- PK가 없는 상태에서 여러 VALUES 한번에 추가
INSERT INTO classmates VALUES
('홍길동', 30, '서울'),
('김철수', 30, '서울'),
('이호영', 26, '인천'),
('박민희', 29, '대구'),
('최혜영', 28, '전주');
SELECT * FROM classmates;
-- name  age  address
-- ----  ---  -------
-- 홍길동   30   서울
-- 김철수   30   서울
-- 이호영   26   인천
-- 박민희   29   대구
-- 최혜영   28   전주


-----------[READ]-----------

-- LIMIT: 쿼리에서 반환되는 행 수를 제한
-- 특정 행부터 시작해서 조회하기 위해 OFFSET 키워드와
-- 함께 사용하기도 함
SELECT rowid, name FROM classmates LIMIT 2;
-- rowid  name
-- -----  ----
-- 1      홍길동
-- 2      김철수
SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;
-- rowid  name
-- -----  ----
-- 3      이호영

-- WHERE: 특정 조건에 맞는 값만 반환하도록 제한
-- classmates 테이블의 id, name 컬럼 값중에서
-- 주소가 서울인 경우의 데이터만 조회하려면?
SELECT * FROM classmates WHERE address='서울';
-- name  age  address
-- ----  ---  -------
-- 홍길동   30   서울
-- 김철수   30   서울
SELECT name FROM classmates WHERE age >= 30;
-- name
-- ----
-- 홍길동
-- 김철수

-- SELECT DISTINCT: 중복없이 조회하도록 제한
-- classmates 테이블에서 age값 전체를 중복없이 조회하려면?
SELECT DISTINCT age FROM classmates;
-- age
-- ---
-- 30
-- 26
-- 29
-- 28
SELECT DISTINCT address FROM classmates;
-- address
-- -------
-- 서울
-- 인천
-- 대구
-- 전주

-----------[DELETE]-----------

-- 5번째 행에 입력된 '최혜영/28/전주' 데이터를 삭제하고 싶다면?
DELETE FROM classmates WHERE rowid=5;
SELECT * FROM classmates;
-- name  age  address
-- ----  ---  -------
-- 홍길동   30   서울
-- 김철수   30   서울
-- 이호영   26   인천
-- 박민희   29   대구

-----------[UPDATE]-----------

-- 4번째 행에 입력된 '박민희/29/대구' 데이터를 수정하고 싶다면?
UPDATE classmates SET name='김탁구', address='제주도' WHERE rowid=4;
SELECT rowid, * FROM classmates;
-- rowid  name  age  address
-- -----  ----  ---  -------
-- 1      홍길동   30   서울
-- 2      김철수   30   서울
-- 3      이호영   26   인천
-- 4      김탁구   29   제주도

SELECT rowid, name FROM classmates LIMIT 100;
-- rowid  name
-- -----  ----
-- 1      홍길동
-- 2      김철수
-- 3      이호영
-- 4      김탁구