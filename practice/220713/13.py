# 문제
# 주어진 문자열 word가 주어질 때,
# 해당 단어를 역순으로 뒤집은 결과를 출력하시오.
# Input : apple
# Output : elppa

# 접근방법
# 1. 주어진 문자열 : Input()
# 2. for문으로 한바퀴 돌리기
# 3. 문자열 순서 뒤집도록 명령
# 4. 최종 출력 print

# 코드

word = input()
result = ''       # 기존 문자열을 역순으로 담아줄 빈 문자열 선언

for i in word:
    result = i + result
print(result)


# 선생님 코드

word = 'apple'
result - ''

for char in word:
    result = char + result
print(result)

# 선생님 코드2(index 활용): 알고리즘 코드 풀기 좋음!
word = 'apple'

for i in range(len(word)):
    print(word[len(word)-i-1], end='')