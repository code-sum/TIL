# 문제
# 아래 코드는 숫자의 길이를 구하는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.
# Output: 8

# 오류 코드
# number = 22020718
# print(len(number))

# 오류 원인
# TypeError: object of type 'int' has no len()
# len()는 문자열의 길이를 변환하는 함수
# 따라서 정수값을 문자열로 변환하여 len() 적용

# 수정 코드
number = 22020718
result = len(str(number))
print(result)