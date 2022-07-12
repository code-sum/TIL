# 문제
# 주어진 리스트 numbers에서 두번째로 큰 수를 구하여 출력하시오. 
# max() 함수 사용 금지
# numbers = [0, 20, 100, 40]

# 접근방식
# 1. 처음부터 끝까지 돌아야하니까 for문 쓴다.
# 2. 최대로 큰 숫자 찾는 변수 이름 지정(max_num)
# 3. 두번째로 큰 숫자 찾는 변수 이름 지정
# 4. 이전에 max_num 에 있던 수를 3. 으로 넘김

# 코드
numbers = [0, 20, 100]
max_number = numbers[0]
second_number = numbers[0]

for n in numbers:
    if max_number < n:             # 만약에 n이 최대보다 크다면
        second_number = max_number # 최대값이었던 두번째로 큰 수
        max_number = n
print(second_number)
# 그러나, 이 코드로 문제를 풀면
# numbers = [0, 20, 100, 40] 으로 40 이라는 수가
# 맨 뒤에 등장했을 때, 이를 제대로 반영하여 계산하지 못하는
# 상황이 발생한다(실제 답은 40 이지만, 출력은 20 으로 나옴)
# 따라서 하단의 코드를 참조도록 하자

# 다른 코드
numbers = [0, 20, 100, 40]
max_number = numbers[0]
second_number = numbers[0]

for n in numbers:
    if max_number < n:             # 만약에 n이 최대보다 크다면
        second_number = max_number # 최대값이었던 두번째로 큰 수
        max_number = n
    elif second_number < n and n < max_number:
        second_number = n
print(second_number)