# 문제
# 가로와 세로의 길이를 각각 a, b로 받아
# 사각형 넓이와 둘레를 함께 반환하는 함수 rectangle을 정의하시오. 
# 사각형이 가로가 20, 세로가 30일 때의 결과를 출력하시오.
# * 사각형 넓이 : 가로 * 세로 
# * 사각형 둘레 : (가로 + 세로) * 2

# 접근방법
# 1. 가로와 세로의 길이를 각각 a, b로 받아 : input
# 2. 사각형 넓이와 둘레를 함께 반환하는 함수 rectangle을 정의하시오. : def, return
# 3. 사각형이 가로가 20, 세로가 30일 때의 결과를 출력하시오. : print

# 코드
a = int(input())
b = int(input())

def rectangle(a, b):
    return a*b, (a+b)*2     # 함수 2개 사이에 , 찍으면 튜플()로 처리!

result = rectangle(a, b)
print(result)


