# 문자들이 1개씩 계속해서 입력된다.
# 영문 소문자 'q'가 입력될 때까지 입력한 문자를 계속 출력한다.


while True:
    word = input()
    if word == 'q':
        print(word)
        break
    print(word)
