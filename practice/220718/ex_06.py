# 문제
# 아래 코드는 1부터 N까지의 숫자에 2를 곱해서 변수에 저장하는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.
# Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# 오류 코드
# N = 10
# answer = ()
# for number in range(N + 1):
#     answer.append(number * 2)
# print(answer)

# 오류 원인
# AttributeError: 'tuple' object has no attribute 'append'
# 주어진 for문 실행은 튜플 생성으로 이어지는데,
# .append 는 리스트에 값을 추가하는 함수라서 오류
# 따라서 answer 을 리스트로 변환하기

# 수정 코드
N = 10
answer = []
for number in range(N + 1):
    answer.append(number * 2)
print(answer)