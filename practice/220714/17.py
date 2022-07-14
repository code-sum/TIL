# 문제
# 소문자로 구성된 문자열 word가 주어질 때, 모두 대문자로 바꾸어 표현하시오. 
# .upper(), .swapcase() 사용 금지
# Input: banana
# Output: BANANA

# 접근방법
# 1. 알파벳을 숫자로 바꾸고
# 2. 그 숫자를 -32 하고
# 3. 다시 숫자를 알파벳으로 바꿈

# 코드
word = 'banana'
result = ''

for i in word:
    number = ord(i)
    number = number-32
    result += chr(number)
print(result)