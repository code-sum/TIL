alpha = input()
alpha = ord(alpha)
start = ord('a')

while start <= alpha:
    print(chr(start), end = ' ')
    start += 1

# 알파벳 문자 a의 정수값은 ord('a')로 알아낼 수 있다.
# chr(정수값)을 이용하면 다시 유니코드 문자를 출력할 수 있다.