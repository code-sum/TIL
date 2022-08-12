import sys

sys.stdin = open("codeup_6095.txt")

d=[]                   #대괄호 [ ] 를 이용해 아무것도 없는 빈 리스트 만들기
for i in range(20) :
    d.append([])         #리스트 안에 다른 리스트 추가해 넣기
    for j in range(20) : 
        d[i].append(0)    #리스트 안에 들어있는 리스트 안에 0 추가해 넣기
# 리스트 컴프리헨션 써서
# d = [[0 for j in range(20)] for i in range(20)]
# 이와 같이 간단히 작성할 수도 있음

n = int(input())

for i in range(n) :
    x, y = input().split()
    d[int(x)][int(y)] = 1

for i in range(1, 20) :
    for j in range(1, 20) : 
        print(d[i][j], end=' ')    #공백을 두고 한 줄로 출력
    print()                        #줄 바꿈