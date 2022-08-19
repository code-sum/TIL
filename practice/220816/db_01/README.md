# 1. 2022-08-16 /사전 설정



## 실행

```bash
$ sqlite3 healthcare.sqlite3 
```

## Column 출력 설정

```sql
sqlite3> .headers on 
sqlite3> .mode column
```

## table 및 스키마 조회

```sql
sqlite3> .tables
healthcare

sqlite3> .schema healthcare
CREATE TABLE healthcare (
id PRIMARY KEY,        
sido INTEGER NOT NULL, 
gender INTEGER NOT NULL,
age INTEGER NOT NULL,  
height INTEGER NOT NULL,
weight INTEGER NOT NULL,
waist REAL NOT NULL,   
va_left REAL NOT NULL, 
va_right REAL NOT NULL,

blood_pressure INTEGER 
NOT NULL,
smoking INTEGER NOT NULL,
is_drinking BOOLEAN NOT NULL
);
```

# 문제

### 1. 추가되어 있는 모든 데이터의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare;
```

```
COUNT(*)
--------
1000000
```

### 2. 나이 그룹이 10(age)미만인 사람의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare WHERE age < 10;
```

```
156277
```

### 3. 성별이 1인 사람의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare WHERE gender=1;
```

```
510689
```

### 4. 흡연 수치(smoking)가 3이면서 음주(is_drinking)가 1인 사람의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare WHERE smoking=3 AND is_drinking=1;
```

```
150361
```

### 5. 양쪽 시력이(va_left, va_right) 모두 2.0이상인 사람의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare WHERE va_left >= 2.0 AND va_right >= 2.0;
```

```
2614
```

### 6. 시도(sido)를 모두 중복 없이 출력하시오.

```sql
SELECT DISTINCT sido FROM healthcare;
```

```
sido
----
36
27
11
31
41
44
48
30
42
43
46
28
26
47
45
29
49
```

### 자유롭게 조합해서 원하는 데이터를 출력해보세요.

> 예) 허리 둘레가 x이상이면서 몸무게가 y이하인 사람





---





# 2. 2022-08-17 / 2일차 실습



## 사전 확인

### 실행

```bash
$ sqlite3 healthcare.sqlite3 
```

### Column 출력 설정

```sql
sqlite3> .headers on 
sqlite3> .mode column
```

### table 및 스키마 조회

```sql
sqlite3> .tables
healthcare

sqlite3> .schema healthcare
CREATE TABLE healthcare (
    id PRIMARY KEY,        
    sido INTEGER NOT NULL, 
    gender INTEGER NOT NULL,
    age INTEGER NOT NULL,  
    height INTEGER NOT NULL,
    weight INTEGER NOT NULL,
    waist REAL NOT NULL,   
    va_left REAL NOT NULL, 
    va_right REAL NOT NULL,

    blood_pressure INTEGER 
    NOT NULL,
    smoking INTEGER NOT NULL,
    is_drinking BOOLEAN NOT NULL
);
```

## 문제

### 1. 추가되어 있는 모든 데이터의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare;
```

```sql
COUNT(*)
--------
1000000
```

### 2. 연령 코드(age)의 최대, 최소 값을 모두 출력하시오. 

```sql
SELECT MAX(age), MIN(age) FROM healthcare;
```

```sql
MAX(age)  MIN(age)
--------  --------
18        9
```

### 3. 신장(height)과 체중(weight)의 최대, 최소 값을 모두 출력하시오.

```sql
SELECT MAX(height), MIN(height), MAX(weight), MIN(weight) FROM healthcare;
```

```sql
MAX(height)  MIN(height)  MAX(weight)  MIN(weight)
-----------  -----------  -----------  -----------
195          130          135          30
```

### 4. 신장(height)이 160이상 170이하인 사람은 몇 명인지 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare WHERE height BETWEEN 160 AND 170;
```

```sql
COUNT(*)
--------
516930
```

### 5. 음주(is_drinking)를 하는 사람(1)의 허리 둘레(waist)를 높은 순으로 5명 출력하시오. 

(추가 조건: 공백 제거하는 조건 추가) NULL 이랑 공백이랑 다른 개념

```sql
SELECT id, waist FROM healthcare WHERE is_drinking=1 and waist !='' ORDER BY waist DESC LIMIT 5;
```

```sql
waist
-----
146.0
142.0
141.4
140.0
140.0
```

### 6. 시력 양쪽(va_left, va_right)이 1.5이상이면서 음주(is_drinking)를 하는 사람의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare WHERE (va_left>=1.5 AND va_right>=1.5) AND is_drinking=1;
```

```sql
COUNT(*)
--------
36697
```

### 7. 혈압(blood_pressure)이 정상 범위(120미만)인 사람의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare WHERE blood_pressure<120;
```

```sql
COUNT(*)
--------
360808
```

### 8. 혈압(blood_pressure)이 140이상인 사람들의 평균 허리둘레(waist)를 출력하시오.

```sql
SELECT AVG(waist) FROM healthcare WHERE blood_pressure>=140;
```

```sql
AVG(waist)
----------------
85.8665098512525
```

### 9. 성별(gender)이 1인 사람의 평균 키(height)와 평균 몸무게(weight)를 출력하시오.

```sql
SELECT AVG(height), AVG(weight) FROM healthcare WHERE gender=1;
```

```sql
AVG(height)       AVG(weight)
----------------  ----------------
167.452735422145  69.7131620222875
```

### 10. 키가 가장 큰 사람 중에 두번째로 무거운 사람의 id와 키(height), 몸무게(weight)를 출력하시오.

```sql
SELECT id, height, weight FROM healthcare ORDER BY height DESC  LIMIT 1 OFFSET 1;
```

```sql
id     height  weight
-----  ------  ------
46642  195     100
```

### 11. BMI가 30이상인 사람의 수를 출력하시오. 

> BMI는 체중/(키*키)의 계산 결과이다. 
> 키는 미터 단위로 계산한다.

```sql
SELECT COUNT(*) FROM healthcare WHERE (weight/((height*0.01)*(height*0.01)))>=30;
```

```sql
COUNT(*)
--------
53121
```

### 12. 흡연(smoking)이 3인 사람의 BMI지수가 제일 높은 사람 순서대로 5명의 id와 BMI를 출력하시오.

> BMI는 체중/(키*키)의 계산 결과이다. 
> 키는 미터 단위로 계산한다.

```sql
SELECT id, (weight/((height*0.01)*(height*0.01))) FROM healthcare WHERE smoking=3 ORDER BY (weight/((height*0.01)*(height*0.01))) DESC LIMIT 5;

-- BMI 별칭 만들어서 사용하기
SELECT id, (weight/((height*0.01)*(height*0.01))) AS BMI FROM healthcare WHERE smoking=3 ORDER BY BMI DESC LIMIT 5;
```

```sql
id      (weight/((height*0.01)*(height*0.01)))
------  --------------------------------------
231431  50.78125
934714  49.9479708636837
722707  48.828125
947281  47.7502295684114
948801  47.7502295684114
```

### 13. 자유롭게 쿼리를 작성해주시고, 결과와 함께 공유해주세요. [나이가 제일 많은 사람의 sido]

```sql
SELECT sido, MAX(age) FROM healthcare; 
```

```sql
sido  MAX(age)
----  --------
27    18
```

### 14. 자유롭게 쿼리를 작성해주시고, 결과와 함께 공유해주세요. [술을 안마시는데 혈압 120 이상인 사람의 수]

```sql
SELECT COUNT(*) FROM healthcare WHERE is_drinking=0 AND blood_pressure>=120;
```

```sql
COUNT(*)
--------
268500
```

### 15. 자유롭게 쿼리를 작성해주시고, 결과와 함께 공유해주세요. [키가 170 이상인 사람 중에 몸무게가 두번째로 많은 사람의 체중]

```sql
SELECT weight FROM healthcare WHERE height >= 170 ORDER BY weight DESC LIMIT 1 OFFSET 1;
```

```sql
weight
------
135
```





---





# 3. 2022-08-18 / 3일차 실습



###  1. 흡연 여부(smoking)로 구분한 각 그룹의 컬럼명과 그룹의 사람의 수를 출력하시오.

```sql 
SELECT smoking, COUNT(*) FROM healthcare WHERE smoking !='' GROUP BY smoking;

smoking  COUNT(*)
-------  --------
1        626138
2        189808
3        183711
```

###  2. 음주 여부(is_drinking)로 구분한 각 그룹의 컬럼명과 그룹의 사람의 수를 출력하시오.

```sql 
SELECT is_drinking, COUNT(*) FROM healthcare WHERE is_drinking !='' GROUP BY is_drinking;

is_drinking  COUNT(*)
-----------  --------
0            415119
1            584685
```

### 3. 음주 여부로 구분한 각 그룹에서 혈압(blood_pressure)이 200이상인 사람의 수를 출력하시오.

```sql
SELECT is_drinking, COUNT(*) FROM healthcare WHERE blood_pressure>=200 AND is_drinking !='' GROUP BY is_drinking;

is_drinking  COUNT(*)
-----------  --------
0            6064
1            1770
```

### 4. 시도(sido)에 사는 사람의 수가 50000명 이상인 시도의 코드와 그 시도에 사는 사람의 수를 출력하시오.

```sql
SELECT sido, COUNT(*) FROM healthcare GROUP BY sido HAVING COUNT(*)>=50000;

sido  COUNT(*)
----  --------
11    166231
26    69025
28    58345
41    247369
47    54438
48    68530
```

### 5. 키(height)를 기준으로 구분하고, 각 키와 사람의 수를 출력하시오.

> 단, 사람의 수를 기준으로 내림차순으로 5개까지 출력하시오.

```sql
SELECT height, COUNT(*) FROM healthcare GROUP BY height ORDER BY COUNT(*) DESC LIMIT 5;

height  COUNT(*)
------  --------
160     184993
155     181306
165     179352
170     152585
150     128555
```

### 6. 키(height)와 몸무게(weight)를 기준으로 구분하고, 몸무게와, 키, 해당 그룹의 사람의 수를 출력하시오. 

> 단, 사람의 수를 기준으로 내림차순 5개까지 출력하시오.

```sql
SELECT weight, height, COUNT(*) FROM healthcare GROUP BY weight, height ORDER BY COUNT(*) DESC LIMIT 5;

weight  height  COUNT(*)
------  ------  --------
55      155     45866
60      160     42454
65      165     40385
50      155     38582
55      160     38066
```

### 7. 음주여부에 따라 평균 허리둘레(waist)와 사람의 수를 출력하시오.

```sql 
SELECT is_drinking, AVG(waist), COUNT(*) FROM healthcare WHERE is_drinking !='' GROUP BY is_drinking;

is_drinking  AVG(waist)        COUNT(*)
-----------  ----------------  --------
0            81.2128249971711  415119
1            83.1541594191841  584685
```

### 8. 각 성별(gender)의 평균 왼쪽 시력(va_left)과 평균 오른쪽 시력(va_right)를 출력하시오.

> 단, 평균 왼쪽 시력과 평균 오른쪽 시력의 컬럼명을 '평균 왼쪽 시력' '평균 오른쪽 시력'로 표시하고, 평균 시력은 소수점 둘째 자리까지 출력하시오.

```sql
SELECT gender, ROUND(AVG(va_left), 2) "평균 왼쪽 시력", ROUND(AVG(va_right), 2) "평균 오른쪽 시력" FROM healthcare WHERE va_left !='' AND va_right !='' GROUP BY gender;

gender  평균 왼쪽 시력  평균 오른쪽 시력
------  --------  ---------
1       0.98      0.99
2       0.88      0.88
```

### 9. 각 나이대(age)의 평균 키와 평균 몸무게를 출력하시오.

> 단, 평균 키와 평균 몸무게의 컬럼명을 '평균 키' '평균 몸무게'로 표시하고, 평균키가 160 이상 평균 몸무게가 60 이상인 데이터만 출력하시오.

```sql
SELECT age, AVG(height) "평균 키", AVG(weight) "평균 몸무게" FROM healthcare WHERE height !='' AND weight !='' GROUP BY age HAVING AVG(height)>=160 AND AVG(weight)>=60;

age  평균 키              평균 몸무게
---  ----------------  ----------------
9    165.66545300972   67.2402208898302
10   164.119689244962  65.677140776194
11   162.111550610398  63.9036737713782
12   160.653006214415  62.5955563062588
```

### 10. 음주 여부(is_drinking)와 흡연 여부(smoking)에 따른 평균 BMI를 출력하시오.

> 단, 음주 여부 또는 흡연 여부가 공백이 아닌 행만 사용하세요.

```sql
SELECT is_drinking "음주 여부", smoking "흡연 여부", AVG((weight/((height*0.01)*(height*0.01)))) "평균 BMI" FROM healthcare WHERE is_drinking !='' AND smoking !='' AND weight !='' AND height !='' GROUP BY "음주 여부", "흡연 여부";

음주 여부  흡연 여부  평균 BMI
-----  -----  ----------------
0      1      23.8724603942955
0      2      24.6073677352564
0      3      24.3193273448558
1      1      23.9341328992508
1      2      25.0333550564281
1      3      24.6363247421328
```

