# 문제
# 아래 코드는 리스트에서 최댓값을 구하는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.
# Output: 두 번째 리스트의 최댓값이 더 큽니다.

# 오류 코드
# number_list = [1, 23, 9, 6, 91, 59, 29]
# max = max(number_list)
# number_list2 = [2, 5, 100, 20, 50, 10, 91, 82]
# max2 = max(number_list2)
# if max > max2:
#     print("첫 번째 리스트의 최댓값이 더 큽니다.")
# elif max < max2:
#     print("두 번째 리스트의 최댓값이 더 큽니다.")
# else:
#     print("첫 번째 리스트의 최댓값과 두 번째 리스트의 최댓값은 같습니다.")

# 오류 원인
# TypeError: 'int' object is not callable
# 2개의 리스트에서 각각 최댓값을 뽑아내고
# 그 크기를 비교해야하는데, 주어진 오류 코드에서는
# if문에 int형 변수들을 비교하는 연산이 들어있어서 처리가 안됨

# 수정 코드
# number_list 에서 29 부분을 290 으로 바꾸면
# "두 번째 리스트의 최댓값이 더 큽니다." 가 그대로 출력되는 현상은
# 어떻게 해결해야할까? 고민해보기
number_list = [1, 23, 9, 6, 91, 59, 29]
max = number_list[0]

number_list2 = [2, 5, 100, 20, 50, 10, 91, 82]
max2 = number_list2[0]

if max > max2:
    print("첫 번째 리스트의 최댓값이 더 큽니다.")
elif max < max2:
    print("두 번째 리스트의 최댓값이 더 큽니다.")
else:
    print("첫 번째 리스트의 최댓값과 두 번째 리스트의 최댓값은 같습니다.")

