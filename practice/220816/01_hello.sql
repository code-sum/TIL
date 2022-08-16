-- classmates 라는 이름의 테이블 생성
CREATE TABLE classmates (
    id INTEGER PRIMARY KEY,
    name TEXT
);

-- 테이블 목록 조회
.tables
-- classmates  examples

-- 특정 테이블 스키마 조회
.schema classmates
-- CREATE TABLE classmates (
--     id INTEGER PRIMARY KEY,
--     name TEXT
-- );

-- 값 추가
INSERT INTO classmates VALUES (1, '조세호');

-- 테이블 조회
SELECT * FROM classmates;
-- 1|조세호

-- 값 추가2 & 테이블 조회
INSERT INTO classmates VALUES (2, '이동희');
SELECT * FROM classmates;
-- 1|조세호
-- 2|이동희

-- 테이블 삭제 & 남은 테이블 목록 조회
DROP TABLE classmates;
.tables
-- examples