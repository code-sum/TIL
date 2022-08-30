# 문제
# 주어진 리스트 numbers에서 최솟값을 구하여 출력하시오. 
# min() 함수 사용 금지
# numbers = [0, 20, 100]

# 접근방식
# !. 처음부터 끝까지 돌아야하니까 for문 쓴다.
# 2. 비교할 변수 이름 지정(min_num)
# 3. 비교가 참인 경우는 min_num > n
#          거짓인 경우는 min_num = n

# 코드
numbers = [0, 20, 100]
min_num = numbers[0]     # 주어진 수 가운데 가장 작은 수를 초기값에 입력

for n in numbers:     # 반복
    if min_num > n:   # 만약, min값이 n보다 크면 바꾼다.
       min_num = n
print(min_num)