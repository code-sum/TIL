# 문제
# 아래 코드는 과일의 개수를 구하는 논리적 오류가 있는 코드의 일부분 입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.
# Output: {'Apricot': 1,
#          'Blackcurrant': 1,
#          'Cantaloupe': 1,
#          'Feijoa': 1,
#          'Grapefruit': 1,
#          'Juniper berry': 1,
#          'Salal berry': 1,
#          'Soursop': 1}

# 오류 코드
# from pprint import pprint
# fruits = [
#     "Soursop",
#     "Grapefruit",
#     "Apricot",
#     "Juniper berry",
#     "Feijoa",
#     "Blackcurrant",
#     "Cantaloupe",
#     "Salal berry",
# ]
# fruit_count = {}
# for fruit in fruits:
#     if fruit not in fruit_count:
#         fruit_count = {fruit: 1}
#     else:
#         fruit_count[fruit] += 1
# pprint(fruit_count)

# 오류 원인
# {'Salal berry': 1} 밖에 안뜸
# 리스트 안의 요소들이 새 딕셔너리에 들어가면 개수를 1씩 세야하는데
# 주어진 코드는 리스트 요소가 딕셔너리에 not in 이면 {fruit: 1}를
# 출력하게끔 논리가 구성되어 있음

# 수정 코드
from pprint import pprint
fruits = [
    "Soursop",
    "Grapefruit",
    "Apricot",
    "Juniper berry",
    "Feijoa",
    "Blackcurrant",
    "Cantaloupe",
    "Salal berry",
]

fruit_count = {}
def get_counts(seq):
    for x in seq:
        if x in fruit_count:
            fruit_count[x] += 1
        else:
            fruit_count[x] = 1
    return fruit_count

fruit_count = get_counts(fruits)
pprint(fruit_count)