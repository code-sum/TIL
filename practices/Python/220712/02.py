# 문제
# 문자열 word의 길이를 출력하는 코드를 
# 작성하시오
# 주의 ! len() 함수 사용 금지
# 입력: word = 'happly!'
# 출력: 6

# 코드
word = 'happy!'
count = 0

for char in word:       # 모든 문자를 돌면서 1씩 증가시킨다.
    count = count + 1   # count += 1
print(count)