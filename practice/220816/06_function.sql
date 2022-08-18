.headers on
.mode column

SELECT * FROM users LIMIT 1;

-- | (pipe sign) 활용해서 문자열 합치기
-- pipe sign 은 보통 엔터 키 위에 있음
-- (성+이름) 구조로 5명의 데이터만 출력하기
SELECT 
    last_name || first_name 이름,
    age, 
    country, 
    phone, 
    balance 
FROM users 
LIMIT 5;

-- 이름   age  country  phone          balance
-- ---  ---  -------  -------------  -------
-- 유정호  40   전라북도     016-7280-2855  370
-- 이경희  36   경상남도     011-9854-5133  5900
-- 구정자  37   전라남도     011-4177-8170  3100
-- 장미경  40   충청남도     011-9079-4419  250000
-- 차영환  30   충청북도     011-2921-4284  220

-- 문자열 길이 LENGTH
SELECT 
    LENGTH(first_name), 
    first_name 
FROM users 
LIMIT 5;
-- LENGTH(first_name)  first_name
-- ------------------  ----------
-- 2                   정호
-- 2                   경희
-- 2                   정자
-- 2                   미경
-- 2                   영환

-- 문자열 변경 REPLACE
-- 016-7280-2855 => 01672802855
SELECT 
first_name, 
phone, 
REPLACE(phone, '-', '') 
FROM users 
LIMIT 5;
-- first_name  phone          REPLACE(phone, '-', '')
-- ----------  -------------  -----------------------
-- 정호          016-7280-2855  01672802855
-- 경희          011-9854-5133  01198545133
-- 정자          011-4177-8170  01141778170
-- 미경          011-9079-4419  01190794419
-- 영환          011-2921-4284  01129214284

-- 숫자 활용
-- MOD(숫자1, 숫자2): 숫자1을 숫자2로 나눈 나머지
SELECT MOD(5, 2) 
FROM users 
LIMIT 1;
-- MOD(5, 2)
-- ---------
-- 1.0

-- 올림, 내림, 반올림
SELECT CEIL(3.14), FLOOR(3.14), ROUND(3.14) 
FROM users 
LIMIT 1;
-- CEIL(3.14)  FLOOR(3.14)  ROUND(3.14)
-- ----------  -----------  -----------
-- 4.0         3.0          3.0

-- 9의 제곱근
SELECT SQRT(9) 
FROM users 
LIMIT 1;
-- SQRT(9)
-- -------
-- 3.0

-- 9^2
SELECT POWER(9, 2) 
FROM users 
LIMIT 1;
-- POWER(9, 2)
-- -----------
-- 81.0