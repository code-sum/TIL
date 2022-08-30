# 문제가 좀 이상한듯
# 아래의 답안 코드대로 작성하면 33이 등장했을 때 XX 가 아닌 X만 뜸

# 30 보다 작은 정수 1개가 입력된다.
n = int(input())

# 1 부터 n까지 '공백을 두고' 순서대로 출력하되
# 3 or 6 or 9 가 포함되어 있는 수라면
# 그 수 대신 영문 대문자 X 를 출력

for i in range(1, n+1):

    if (i%10==3 or i%10==6 or i%10==9):
        print('X',end=' ')
        continue

    print(i,end=' ')