# 16진수(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F)

n = int(input(), 16)

for i in range(1, 16):
    print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')
