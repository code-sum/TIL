# 문제
# 문자열 word가 주어질 때, 해당 문자열에서 모음의 갯수를 출력하시오. 
# 모음 : a, e, i, o, u count() 사용 금지
# Input: apple
# Output: 2
# 아래의 테스트 케이스로도 확인 해보세요.
# aeiou # 5 
# zxcvb # 0

# 접근방법
# 모음 값들을 하나씩 지정

# 코드
word = 'apple'
count = 0

for i in range(len(word)):
    if word[i] == 'a' or word[i] == 'e' or word[i] == 'i' or word[i] == 'o' or word[i] == 'u':
        count += 1
print(count)

# 다른 코드
word = 'apple'
count = 0

for i in word:
    if i in 'aeiou':
        count += 1
print(count)