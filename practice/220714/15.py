# 문제
# 문자열 word가 주어질 때,
# 해당 문자열에서 a 가 처음으로 등장하는 위치(index)를 출력해주세요.
# a 가 없는 경우에는 -1을 출력해주세요.
# find() index() 메서드 사용 금지
# Input : banana
# Output : 1
# 아래의 테스트 케이스로도 확인 해보세요.
# apple # 0
# kiwi # -1

# 접근방법
# 1. 문자열 banana  입력
# 2. 위치(index)는 [0], [1] ... 인덱스 구조로 추정
# 3. 알파벳 하나하나에 0, 1, 2, 3, 4, 5 값을 지정해야함
#                                   : range(len()) 이용
# 4. word 는 반복하되, 끝이 정해져있는 구조: for 문

# 코드: for-else
word = 'banana'

for idx in range(len(word)):
    if word[idx] == 'a':
        print(idx)
        break
else:
    print(-1)

# 다른 코드
word = 'banana'

is_a = False
for idx in range(len(word)):
    if word[idx] == 'a':
        print(idx)
        is_a = True
        break
if not is_a:
    print(-1)

# 15번 추가문제
# 문자열 word가 주어질 때, 
# 해당 문자열에서 a 의 모든 위치(index)를 출력해주세요.
# find() index() 메서드 사용 금지
# Input : HappyHacking
# Output : 1 6
# 아래의 테스트 케이스로도 확인 해보세요.
# banana # 1 3 5
# kiwi # 

# 코드
word = 'HappyHacking'
result = []
for idx in range(len(word)):
    if word[idx] == 'a':
        result.append(idx)
print(result)
