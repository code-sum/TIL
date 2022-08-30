-- [0822 필기에 첨부된 엑셀 시트 참조]
-- 새로운 DB를 만들고 그 안에 몇개의 TABLE 생성하기
-- $ sqlite3 project.sqlite3

-- 표1 스키마 작성
CREATE TABLE users (
    id INT PRIMARY KEY,
    name TEXT, 
    role_id INT
);

-- 표1 레코드 채우기
INSERT INTO users VALUES
    (1, '관리자', 1),
    (2, '김철수', 2),
    (3, '이영희', 3);

-- 표2 스키마 작성
CREATE TABLE role (
    id INT PRIMARY KEY,
    title TEXT
);

-- 표2 레코드 채우기
INSERT INTO role VALUES
    (1, 'admin'),
    (2, 'staff'),
    (3, 'student');

-- 표3 스키마 작성
CREATE TABLE articles (
    id INT PRIMARY KEY,
    title TEXT,
    content TEXT,
    user_id INT
);

-- 표3 레코드 채우기
-- 후에 NULL값을 직접 다루는 쿼리를 작성하기 위해
-- 스키마를 작성할 때부터 NOT NULL 조건을 넣지 않음
INSERT INTO articles VALUES
(1, '1번글', '111', 1),
(2, '2번글', '222', 2),
(3, '3번글', '333', 1),
(4, '4번글', '444', NULL);

-- 확인
.headers on
.mode column
SELECT * FROM users;
SELECT * FROM role;
SELECT * FROM articles;