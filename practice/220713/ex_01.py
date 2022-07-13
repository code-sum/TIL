# 문제
# 숫자 n을 받아 세제곱 결과를 반환하는 함수 cube를 정의하시오
# cube 함수를 호출하여 12의 세제곱 결과를 출력하시오

# 접근방법
# 1. 숫자 n을 받아: input
# 2. 세제곱 결과를 반환하는 함수 cube를 정의하시오: def
# 3. cube 함수를 호출하여: return
# 4. 12의 세제곱 결과를 출력하시오: print

# 코드
n = int(input())

def cube(n):
    return n*n*n

result = cube(n)
print(result)

# 출력값: 1728