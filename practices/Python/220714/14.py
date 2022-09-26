# 문제
# 문자열 word가 주어질 때, 
# 해당 문자열에서 a 개수를 구하세요. count() 메서드 사용 금지
# Input: apple
# Output: 1
# 아래의 테스트 케이스로도 확인 해보세요.
# banana # 3
# kiwi # 0

# 접근방법
# 1. 개수를 세주는 변수 count 생성
# 2. word 는 반복하되, 끝이 정해져있는 구조: for 문

# 코드
word = 'apple'
count = 0

for letter in word:
    if letter == 'a':
        count += 1
print(count)


