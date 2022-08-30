# 문제
# 아래 코드는 문자열에서 모음의 개수를 찾는 코드입니다. 
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.
# Output: 3

# 오류 코드
# word = "HappyHacking"
# count = 0
# for char in word:
#     if char == "a" or "e" or "i" or "o" or "u":
#         count += 1
# print(count)

# 오류 원인
# if char == "a" or "e" or "i" or "o" or "u":  코드에서
# == 연산이 or 연산보다 먼저 처리되기 때문에 수정해야 함

# 수정 코드
word = "HappyHacking"
count = 0

for char in word:
    if char in "aeiou":
        count += 1
print(count)

