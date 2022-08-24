-- INNER JOIN
-- A와 B테이블에서 값이 일치하는 것들만
-- 아래 쿼리에서 INNER 는 생략 가능
SELECT * 
FROM users INNER JOIN role 
    ON users.role_id = role.id;
-- id  name  role_id  id  title
-- --  ----  -------  --  -------
-- 1   관리자   1        1   admin
-- 2   김철수   2        2   staff
-- 3   이영희   3        3   student

-- 위 테이블에서 name, title 컬럼만 출력하고 싶을 때
SELECT
    users.name,
    role.title 
FROM users INNER JOIN role 
    ON users.role_id = role.id;
-- name  title
-- ----  -------
-- 관리자   admin
-- 김철수   staff
-- 이영희   student

-- 스태프(role_id = 2)인 경우만 출력
SELECT * 
FROM users INNER JOIN role 
    ON users.role_id = role.id
WHERE role.id = 2;
-- id  name  role_id  id  title
-- --  ----  -------  --  -----
-- 2   김철수   2        2   staff

-- users 와 role 2개의 표를 INNER JOIN 하면서
-- 사람들의 이름을 기준으로 내림차순 출력
SELECT *
FROM users INNER JOIN role
    ON users.role_id = role.id 
ORDER BY users.name DESC;
-- id  name  role_id  id  title
-- --  ----  -------  --  -------
-- 3   이영희   3        3   student
-- 2   김철수   2        2   staff
-- 1   관리자   1        1   admin

-- LEFT OUTER JOIN
SELECT *
FROM articles LEFT OUTER JOIN users
    ON articles.user_id = users.id;
-- id  title  content  user_id  id  name  role_id
-- --  -----  -------  -------  --  ----  -------
-- 1   1번글    111      1        1   관리자   1
-- 2   2번글    222      2        2   김철수   2
-- 3   3번글    333      1        1   관리자   1
-- 4   4번글    444

-- LEFT OUTER JOIN 에서
-- NULL값이 포함된 레코드는 출력 제외하고 싶다면?
SELECT *
FROM articles LEFT OUTER JOIN users
    ON articles.user_id = users.id
WHERE articles.user_id IS NOT NULL;
-- id  title  content  user_id  id  name  role_id
-- --  -----  -------  -------  --  ----  -------
-- 1   1번글    111      1        1   관리자   1
-- 2   2번글    222      2        2   김철수   2
-- 3   3번글    333      1        1   관리자   1

-- FULL OUTER JOIN
SELECT *
FROM articles FULL OUTER JOIN users
    ON articles.user_id = users.id;
-- id  title  content  user_id  id  name  role_id
-- --  -----  -------  -------  --  ----  -------
-- 1   1번글    111      1        1   관리자   1
-- 2   2번글    222      2        2   김철수   2
-- 3   3번글    333      1        1   관리자   1
-- 4   4번글    444
--                              3   이영희   3

-- CROSS JOIN
SELECT *
FROM users CROSS JOIN role;
-- id  name  role_id  id  title
-- --  ----  -------  --  -------
-- 1   관리자   1        1   admin
-- 1   관리자   1        2   staff
-- 1   관리자   1        3   student
-- 2   김철수   2        1   admin
-- 2   김철수   2        2   staff
-- 2   김철수   2        3   student
-- 3   이영희   3        1   admin
-- 3   이영희   3        2   staff
-- 3   이영희   3        3   student

-- 2개 이상(3개)의 테이블 조인
-- A ~ B ~ C 
-- JOIN절을 2개 작성합니다
SELECT * 
FROM articles
    JOIN users
        ON articles.user_id = users.id
    JOIN role 
        ON users.role_id = role.id;
-- id  title  content  user_id  id  name  role_id  id  title
-- --  -----  -------  -------  --  ----  -------  --  -----
-- 1   1번글    111      1        1   관리자   1        1   admin
-- 2   2번글    222      2        2   김철수   2        2   staff
-- 3   3번글    333      1        1   관리자   1        1   admin