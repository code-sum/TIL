a, m, d, n = map(int, input().split())

# 1부터 시작해 이전에 만든 수에 -2를 곱한 다음 1을 더해 다음 수를 만듬
# n번째 수를 출력하자

# 1(시작값a) * (-2)(곱할값m) + 1(더할값d) ... 몇번째인지 나타내는 정수 8(n)

for i in range(1, n):
    cycle = (a * m) + d
    a = cycle

print(a)