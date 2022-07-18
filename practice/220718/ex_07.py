# 문제
# 아래 코드는 평균을 구하는 논리적으로 오류가 있는 코드입니다. 
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.
# Output: 5.5

# 오류 코드
# number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# total = 0
# count = 0
# for number in number_list:
#     total += number
# count += 1
# print(total // count)

# 오류 원인
# (평균)=(전체 합계)/N 의 논리여야 하는데
# 위의 코드는 (평균)=(전체 합계) 결과가 도출됨
# // 는 소수점 이하 부분을 표기하지 않으므로 / 로 수정

# 수정 코드
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0
count = 0

for number in number_list:
    total += number
    count += 1

average = total / count
print(average)