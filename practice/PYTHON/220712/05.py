# 문제
# 주어진 숫자의 평균을 구하는 코드를 작성하시오. 
# sum(), len()  함수 사용 금지
# numbers = [3, 20, 100]

# 접근방식
# result, count 의 2가지 변수를 만들어 기록하는 것이 핵심!

# 코드

numbers = [3, 10, 20]    # 문제제공

result = 0               # 값 초기화
count = 0                # 값 초기화

for number in numbers:               # 반복
    result = result + number
    count = count + 1

print(result/count)

# 쉬운 풀이: print(sum(numbers)/len(nembers))