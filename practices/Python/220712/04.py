# 문제
# 1부터 n까지의 곱을 구하여 출력하는 코드를 
# 1) while 문 2) for 문으로 각각 작성하시오.

# 접근방법
# 1. while 문
#    1) 시작 값 초기화
#    2) 사용자 입력 변수 지정(b_input)
#    3) 매 회 거듭될수록 n 는 1씩 증가해야하고
#    4) result 에 n 을 곱해가야 함
#    5) 종료조건은 n = b_input
# 2. for 문
#    1) 시작 값 초기화
#    2) 숫자의 나열인 range 활용

# 코드

# 1. while 문
n = 1
result = 1
b_input = int(input())

while n <= b_input:
    result *= n
    n += 1
print(result)

# 2. for 문
n = 1
result = 1
b_input = int(input())

for n in range(b_input):
    n += 1
    result *= n
print(result)
