-- 가장 나이가 작은 사람의 수
-- 1
SELECT age, COUNT(*)
FROM users
GROUP BY age
ORDER BY age
LIMIT 1;
-- age  COUNT(*)
-- ---  --------
-- 15   39

-- 확인해보기
SELECT MIN(age)
FROM users;
-- MIN(age)
-- --------
-- 15

SELECT COUNT(*)
FROM users
WHERE age = 15;
-- COUNT(*)
-- --------
-- 39

-- 위의 내용을 종합해서 서브쿼리 작성
SELECT COUNT(*)
FROM users
WHERE age = (SELECT MIN(age) FROM users);
-- COUNT(*)
-- --------
-- 39

-- 평균 계좌 잔고가 높은 사람이 몇 명인지 찾아보자
SELECT COUNT(*)
FROM users
WHERE balance > (SELECT AVG(balance) FROM users);
-- COUNT(*)
-- --------
-- 222

-- 유은정과 같은 지역에 사는 사람의 수?
SELECT COUNT(*)
FROM users
WHERE country = (SELECT country FROM users 
WHERE last_name='유' AND first_name='은정');
-- COUNT(*)
-- --------
-- 101

-- 총인원과 평균 연봉, 평균 나이를 출력하세요
-- 모든 컬럼이 같은 테이블에 존재하고 있다면
-- 당연히 아래와 같이 쿼리를 작성
SELECT COUNT(*), AVG(balance), AVG(age)
FROM users;
-- COUNT(*)  AVG(balance)  AVG(age)     
-- --------  ------------  --------     
-- 1000      151456.89     27.346

-- 만약에 총인원과 평균연봉을 뽑을 수 있는
-- 테이블이 서로 다르다면, 서브쿼리가 유용하게 쓰임
-- 예를 들면 table이 게시글 테이블, 댓글 테이블 이런 식
SELECT
    (SELECT COUNT(*) FROM users) AS 총인원,
    (SELECT AVG(balance) FROM users) AS 평균연봉;
-- 총인원   평균연봉
-- ----  ---------
-- 1000  151456.89

-- 단일행 서브쿼리: UPDATE에서 활용
-- 모든 사람들의 계좌 잔액을 평균 금액으로 수정하고 싶다면?
UPDATE users
SET balance = (SELECT AVG(balance) FROM users);

-- 다중행 서브쿼리
-- users에서 이은정과 같은 지역에 사는 사람들의 수는?
-- 위 질문에 답할 수 있는 쿼리를 작성하기 전에,
-- 데이터에서 '이은정'이 단일한 값 1개인지 먼저 확인하자
SELECT
    country
FROM users
WHERE last_name = '이' AND first_name = '은정';
-- country
-- -------
-- 전라북도
-- 경상북도

-- 서브쿼리를 아래와 같이 작성하면,
-- '이은정'과 같은 지역(전북, 경북)에 사는 사람들 중에
-- 전라북도에 사는 사람들으 수만 출력됨
SELECT
    COUNT(*)
FROM users
WHERE country = (SELECT country FROM users
WHERE last_name = '이' AND first_name = '은정');
-- COUNT(*)
-- --------
-- 115

SELECT country, COUNT(*) 
FROM users 
GROUP BY country; 
-- country  COUNT(*)
-- -------  --------
-- 강원도      101
-- 경기도      114
-- 경상남도     106
-- 경상북도     103
-- 전라남도     123
-- 전라북도     115
-- 제주특별자치도  118
-- 충청남도     105
-- 충청북도     115

-- 그러므로 서브쿼리를 아래와 같이 바꿔야
-- 정확한 정보(전북+경북)를 확인할 수 있음
SELECT
    COUNT(*)
FROM users
WHERE country IN (SELECT country FROM users
WHERE last_name = '이' AND first_name = '은정');
-- COUNT(*)
-- --------
-- 218

-- 특정 성씨별로 가장 나이가 적은 사람들의 성, 이름, 나이 출력
-- 성씨 가나다순으로 정렬
SELECT
    last_name,
    MIN(age)
FROM users
GROUP BY last_name;

SELECT
    last_name,
    first_name,
    age
FROM users
WHERE (last_name, age) IN (
    SELECT
        last_name,
        MIN(age)
    FROM users
    GROUP BY last_name)
ORDER BY last_name;


