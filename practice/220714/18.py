# 문제
# 문자열 word가 주어질 때, Dictionary를 활용해서 
# 해당 문자열에서 등장한 모든 알파벳 개수를 구해서 출력하세요.
# Input: banana
# Output: 
# b 1
# a 3
# n 2

# 접근방법
# 1. 결과를 나타내는 딕셔너리에 키가 없을 때: 키-값을 0으로 초기화
# 2. 결과를 나타내는 딕셔너리에 키가 있을 때

# 코드
word = 'banana'
result = {}

for i in word:
    if not i in result:   
        result[i] = 1     # 초기값 1
    else:
        result[i] = result[i] + 1
print(result)

# 다른 코드
word = 'banana'
result = {}

for i in word:
    result[i] = result.get(i, 0) + 1
print(result)

# 출력 부분
for key in result:
    print(key, result[key])