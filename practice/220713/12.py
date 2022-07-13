# 문제
# 주어진 문자열 word가 주어질 때, 
# 해당 단어에서 ‘a’를 모두 제거한 결과를 출력하시오.
# Input : apple
# Output : pple

# 접근방법
# 1. 주어진 문자열 : Input()
# 2. for문으로 한바퀴 돌리기
# 3. a 삭제 명령
# 4. 최종 출력 print

# 코드

word = input()
result = word

for i in word:
    if i in 'a':
        result = result.replace(i,'')
print(result)


# 선생님 코드
# 시퀀스를 끝까지 가는 거니까 while 보다 for 가 좋다!

word = 'apple'
result = ''

for char in 'apple':
    if char != 'a':
        result = result + char
print(result)
