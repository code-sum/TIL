# 문제
# 두 수를 Input으로 받아 합을 구하는 코드이다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.
# Input: 10 20
# Output: 30

# 오류 코드
# numbers = input().split()
# print(sum(numbers))

# 오류 원인
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# sum 은 리스트, 튜플 등을 연산하는 내장함수이기 때문에
# 정수 10, 20의 합을 구하고 싶다면, + 이용해야함

# 수정 코드
a, b = input().split()
a = int(a)
b = int(b)
print(a + b)
