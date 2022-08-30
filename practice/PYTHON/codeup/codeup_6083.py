'''
2 2 2

0 0 0
0 0 1
0 1 0
0 1 1
1 0 0
1 0 1
1 1 0
1 1 1
8

'''
r, g, b = map(int, input().split())

cnt = 0

for i in range(r):
    for j in range(g):
        for k in range(b):
            cnt += 1
            print(i, j, k)

print(cnt)


