# 문제
# 주어진 리스트 numbers에서 최댓값을 구하여 출력하시오.
# 주의 ! max() 함수 사용 금지
# numbers = [0, 20, 100]

# 접근방식
# !. 처음부터 끝까지 돌아야하니까 for문 쓴다.
# 2. 비교할 변수 이름 지정(max_num)
# 3. 비교가 참인 경우는 max_num < n
#          거짓인 경우는 max_num = n

# 코드
numbers = [0, 20, 100]
max_num = float("-inf")     # 파이썬에서 가장 작은 수를 초기값에 입력
                            # 혹은 max_num = numbers[0] 하면 편하다!
for n in numbers:     # 반복
    if max_num < n:   # 만약, max값이 n보다 작으면 바꾼다.
        max_num = n
print(max_num)

