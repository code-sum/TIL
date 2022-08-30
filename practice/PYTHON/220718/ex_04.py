# 문제
# 아래 코드는 문자열을 입력받아 단어별로 나누는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.
# Input: I'm Tuotur 6
# Output: ["I'm", 'Tutor', '6']

# 오류 코드
# words = list(map(int, input().split()))
# print(words)

# 오류 원인
# ValueError: invalid literal for int() with base 10: "I'm"
# Input 과 Output 이 int type 이 아니라 문자열이기 때문에
# map 으로 int 변환을 진행할 필요가 없음

# 수정 코드
words = list(input().split())
print(words)

