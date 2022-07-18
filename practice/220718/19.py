# 문제
# > 양의 정수 number가 주어질 때, 숫자의 길이를 구하시오. 
# **양의 정수number를 문자열로 변경하는 것은 금지입니다. str() 사용 금지**
# Input: 123
# Output: 3

# 접근 방법
# while문 이용하기

# 코드
number = 123
count = 0
# 몫이 0이 되면 종료해야하니까!
# int: 0이 아닌 다른 수면 무조건 True! -- while문
while number != 0:
    number //= 10
    count += 1
print(count)

# 파이써닉한 코드: 문자열로 형 변환
number = 123
print(len(str(number)))