# 문제
# 주어진 리스트의 요소 중에서 5의 개수를 출력하시오.
# numbers = [7, 17, 10, 5, 4, 3, 17, 5, 2, 5]

# 접근방법
# '5'를 특정해서 그 수를 세기: .count 활용하기!

# 코드

numbers = [7, 17, 10, 5, 4, 3, 17, 5, 2, 5]
count_5 = numbers.count(5)

print(count_5)