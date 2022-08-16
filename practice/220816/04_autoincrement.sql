-- id 응용: autoincrement

CREATE TABLE members(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

INSERT INTO members VALUES
(1, '홍길동'),
(2, '김철수'),
(3, '이호영'),
(4, '박민희'),
(5, '최혜영');

SELECT * FROM members;
-- id  name
-- --  ----
-- 1   홍길동
-- 2   김철수
-- 3   이호영
-- 4   박민희
-- 5   최혜영

DELETE FROM members WHERE rowid=5;
INSERT INTO members (name) VALUES ('뿡뿡이');
SELECT * FROM members;
-- id  name
-- --  ----
-- 1   홍길동
-- 2   김철수
-- 3   이호영
-- 4   박민희
-- 6   뿡뿡이

-- rowid 를 활용하지 않고 이런 식으로
-- id 를 지정하여 시작하면, 5행의 데이터를 삭제하고
-- 새로운 데이터(뿡뿡이)를 추가했을 때, 
-- 새로운 데이터의 id 값이 5가 아닌 6인 것을 확인할 수 있다