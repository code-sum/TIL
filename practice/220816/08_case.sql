-- 단순 조회
SELECT id, gender 
FROM healthcare 
LIMIT 5;
-- id  gender
-- --  ------
-- 1   1
-- 2   2
-- 3   2
-- 4   1
-- 5   2

-- 성별 1(남자), 2(여자)
SELECT
    id,
    CASE
        WHEN gender = 1 THEN '남자'
        WHEN gender = 2 THEN '여자'
        -- ELSE
    END AS 성별
FROM healthcare
LIMIT 5;
-- id  성별
-- --  --
-- 1   남자
-- 2   여자
-- 3   여자
-- 4   남자
-- 5   여자

-- 흡연(smoking)
SELECT DISTINCT smoking
FROM healthcare;
-- smoking
-- -------
-- 1
-- 3
-- 2
-- 공~~~~~~~백
-- 이렇게 공백이 함께 출력되는 경우
-- CASE절에 ELSE절을 추가해서 공백을 어떤 식으로
-- 네이밍해서 출력할 것인지를 정해야함

-- 흡연(smoking)의 1, 2, 3 값들을 각각 이름 붙여서 출력
SELECT
    id, 
    smoking, 
    CASE
        WHEN smoking = 1 THEN '비흡연자'
        WHEN smoking = 2 THEN '흡연자'
        WHEN smoking = 3 THEN '헤비스모커'
        ELSE '무응답'
    END
FROM healthcare
LIMIT 50;

-- 나이(age)에 따라서 구분 출력하기
-- 청소년(~18살), 청년(~40살), 중장년(~90살)
SELECT
    first_name,
    last_name, 
    age, 
    CASE
        WHEN age <= 18 THEN '청소년'
        WHEN age <= 40 THEN '청년'
        WHEN age <= 90 THEN '중장년'
        ELSE '노년'
    END
FROM users
LIMIT 10;