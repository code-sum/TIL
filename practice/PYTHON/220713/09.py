# 문제
# 주어진 리스트가 반장 선거 투표 결과일 때 이영희의 총 득표수를 출력하시오.
# Input
# students = ['이영희', '김철수', '이영희', '조민지', '김철수', '조민지', '이영희', '이영희']

# 접근방법
# '이영희'를 특정해서 그 수를 세기: .count 이용하기!

# 코드

students = ['이영희', '김철수', '이영희', '조민지', '김철수', '조민지', '이영희', '이영희']

votes_lee = students.count('이영희')
print(votes_lee)