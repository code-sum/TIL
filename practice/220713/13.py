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
