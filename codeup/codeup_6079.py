# 정수 1개가 입력된다.
# 1, 2, 3, 4, 5 ... 를 순서대로 계속 더해 합을 만들어가다가,
# 입력된 정수와 같거나 커졌을 때, 마지막에 더한 정수를 출력한다.

n = int(input())
count = 0
sum = 0

while True:
    sum += count
    if sum >= n:
        print(count)
        break
    count += 1
