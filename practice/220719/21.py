# 문제
# 주어진 숫자를 뒤집은 결과를 출력하시오. 
# * 문자열이 아닌 숫자로 활용해서 풀어주세요. str() 사용 금지
# Input: 1234
# Output: 4321

# 코드
number = 1234
result = 0
while number:
    result *= 10          # 이전 결과에 10을 곱하고
    result += number%10   # 나머지를 더해주고
    number //= 10         # number를 깎는다.
print(result)

# 다른 코드
number = 1234
print(int(str(number)[::-1]))
