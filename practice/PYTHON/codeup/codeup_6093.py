

n = int(input())
random = list(map(int, input().split()))

for i in range(n-1, -1, -1):
    print(random[i], end = ' ')