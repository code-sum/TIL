-- GROUP BY

-- 성씨마다 몇명의 사람이 있을까?
SELECT last_name, COUNT(*) 
FROM users 
GROUP BY last_name;

-- GROUP BY에서 활용하는 컬럼을 제외하고
-- 집계함수(COUNT, AVG) 사용하기
SELECT last_name, AVG(age), COUNT(*) 
FROM users 
GROUP BY last_name;

-- 참고
SELECT last_name, age 
FROM users 
WHERE last_name = '곽';
-- last_name  age
-- ---------  ---
-- 곽          25
-- 곽          30
-- 곽          28
-- 곽          15

-- GROUP BY절만으로는 결과를 정렬할 수 없음
-- 심지어 기존의 순서와 다르게 바뀔 수 있음
-- 따라서 정렬한 값들을 보고 싶으면 ORDER BY!

SELECT * 
FROM users 
LIMIT 5;
-- first_name  last_name  age  country  phone          balance
-- ----------  ---------  ---  -------  -------------  -------
-- 정호          유          40   전라북도     016-7280-2855  370
-- 경희          이          36   경상남도     011-9854-5133  5900
-- 정자          구          37   전라남도     011-4177-8170  3100
-- 미경          장          40   충청남도     011-9079-4419  250000
-- 영환          차          30   충청북도     011-2921-4284  220

SELECT last_name, COUNT(*) 
FROM users 
GROUP BY last_name 
LIMIT 5;
-- last_name  COUNT(*)
-- ---------  --------
-- 강          23
-- 고          10
-- 곽          4
-- 구          2
-- 권          17

-- 여기서 GROUP BY WHERE 를 쓰고 싶다면?
-- 예시) 100번 이상 등장한 성만 출력하고 싶다면?
SELECT last_name, COUNT(last_name) 
FROM users 
WHERE COUNT(last_name) > 100 
GROUP BY last_name;
-- 위와 같이 쿼리를 작성하면 오류 발생!
-- Parse error: misuse of aggregate: COUNT()
--   SELECT last_name, COUNT(last_name) FROM users WHERE COUNT(last_name) > 100 GROUP

-- 오류가 생기지 않으려면 아래와 같이
-- HAVING절을 활용하기
-- [주의] HAVING절에는 집계함수만 사용해야 함
-- 집계함수를 사용하지 않고 조건을 넣으려면 WHERE절!
SELECT last_name, COUNT(last_name) 
FROM users 
GROUP BY last_name 
HAVING COUNT(last_name) > 100;
-- last_name  COUNT(last_name)
-- ---------  ----------------
-- 김          268
-- 이          179