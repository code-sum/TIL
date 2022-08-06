
n = int(input())

cnt = 0

for i in range(1, n+1):
    if i % 3 == 0:
        continue
    else:
        print(i, end=' ')
    cnt += 1
