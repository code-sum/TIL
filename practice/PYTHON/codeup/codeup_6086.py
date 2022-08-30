# 1, 2, 3 ... 을 순서대로 계속 더해 합을 만드는데,
# 그 합이 입력한 정수보다 작을 동안만 계속 더하는 프로그램을 작성해보자.


n = int(input())

num = 0
sum = 0

while True:
    sum += num
    num += 1
    if sum >= n:
        break

print(sum)