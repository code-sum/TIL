-- 데이터베이스 생성하기
$ sqlite3 tutorial.sqlite3
.database

-- csv 파일을 table로 만들기
.mode csv
.import hellodb.csv examples
.table
-- examples

-- SELECT 확인하기
SELECT * FROM examples;
-- 1,"길동","홍",600,"충청도",010-0000-0000

-- 터미널 view 변경하기
.headers on
SELECT * FROM examples;
-- id,first_name,last_name,age,country,phone
-- 1,"길동","홍",600,"충청도",010-0000-0000
.mode column
SELECT * FROM examples;
-- id  first_name  last_name  age  country  phone
-- --  ----------  ---------  ---  -------  -------------
-- 1   길동          홍          600  충청도      010-0000-0000