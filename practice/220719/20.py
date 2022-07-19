# 문제
# 정수 number가 주어질 때, 각 자릿수의 합을 구해서 출력하세요. 
# Input: 123
# Output: 6

# 접근방법
# 10으로 나눈 나머지의 합을 더해나가기

# 코드
number = 123
result = 0
while number:       # number가 0일 때 Stop <- int 는 0일 때 False 니까
    result += number%10    # 몫은 다음 number
    number //= 10          # 나머지는 더해나가기
print(result)

# 다른 코드
number = 123
result = 0
while number:
    number, remainder = divmod(number, 10)   # divmod(x, y)는 x 를 y로 나누고,
    result += remainder     # 결과를 튜플로 반환
print(result)
