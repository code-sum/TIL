# ✅Python 데이터구조

>1. [중요] 문자열(String)
>2. [중요] 리스트(List)
>3. [생략] 세트(set)
>3. [중요] 딕셔너리(Dictionary)



**시퀀스(순서가 있는 데이터 구조)** / 문자열(String), 리스트(List)

**컬렉션(순서가 없는 데이터 구조)** / 세트(Set), 딕셔너리(Dictionary)



---



## 1. 문자열(String type)

* 문자열
  * 문자들의 나열(sequence of characters)
    * 모든 문자는 str 타입
  * 문자열은 작은 따옴표(')나 큰 따옴표(")를 활용하여 표기
    * 문자열을 묶을 때 동일한 문장부호를 활용
    * PEP8에서는 소스코드 내에서 하나의 문장부호를 선택하여 유지하도록 함



* `타입.메서드()`  :  타입 = 주어, 메서드() = 동사라고 이해하자

  ```python
  # 1. 리스트 메서드 활용
  a = [10, 1, 100]
  new_a = a.sort()
  print(a, new_a)
  
  # 2. 리스트에 sorted 함수를 활용
  b = [10, 1, 100]
  new_b = sorted(b)
  print(b, new_b)
  
  # 위 1. 과 2. 결과값을 비교해보면
  # 1. 은 원본이 변경됨!
  # return 되는 것은 None
  # 출력: [1, 10, 100] None
  
  # 그러나 2. 는 원본을 변경하지 않음
  # return 되는 것은 정렬된 리스트
  
  # 그래서 실제로 활용하려면 아래 코드로 작성해야함!
  a = [10, 1, 100]
  a.sort()
  
  b = [10, 1, 100]
  b = sorted(b)
  ```

  

#### 	1-1. 문자열 탐색/검증

* .isOOOO 이런식은 True / False 검증이라고 이해하자

  | 문법          | 설명                                                         |
  | ------------- | ------------------------------------------------------------ |
  | `s.find(x)`   | x의 첫 번째 위치를 반환. 없으면 -1을 반환                    |
  | `s.index(x)`  | x의 첫 번째 위치를 반환. 없으면 오류 발생                    |
  | `s.isalpha()` | 알파벳 문자 여부 (단순 알파벳이 아닌 유니코드 상 Letter, 한국어도 포함) |
  | `s.isupper()` | 대문자 여부                                                  |
  | `s.islower()` | 소문자 여부                                                  |
  | `s.istitle()` | 타이틀 형식 여부                                             |

* .find(x) : x의 첫번째 위치를 반환. 없으면 -1을 반환

  ```python
  print('apple'.find('p'))
  # 1
  print('apple'.find('k'))
  # -1
  ```

* .index(x) : x의 첫번째 위치를 반환. 없으면 오류 발생

  ```python
  print('apple'.index('p'))
  # 1
  print('apple'.index('k'))
  # 에러메세지 뜸!
  ```

* 문자열 관련 검증 메소드

```python
'abc'.isalpha()
# True
'abc'.isupper() 대문자야?
# False
'ab'.islower()
# True
'Title Title!'.istitle()
# True
```

* isdecimal() 만 쓰자



#### 	1-2. 문자열 변경(1-1. 보다 중요)

* .replace(old, new[,count])

  * 바꿀 대상 글자를 새로운 글자로 바꿔서 반환

  * count 지정하면, 해당 개수만큼만 시행

```python
'coone'.replace('o','a')
# caane
'wooooowoo'.replace('o', '!', 2)
# w!!ooowoo
```

* .strip([chars]) : 공백 제거할 때 유용!

  * 특정한 문자들을 지정하면,

  * 양쪽을 제거하거나(strip), 왼쪽을 제거하거나(lstrip), 오른쪽을 제거(rstrip)

  * 문자열을 지정하지 않으면 공백(개행, 엔터 포함)을 제거

```python
'       와우!\n'.strip()
# '와우!'
'       와우!\n'.lstrip()
# '와우!\n'
'       와우!\n'.rstrip()
# '       와우!'
'안녕하세요????'.rstrip(?)
# '안녕하세요'
```

* .split(sep=None, maxsplit=-1)
  * 문자열을 특정한 단위로 나눠 리스트로 반환
    * sep이 None이거나 지정되지 않으면 연속된 공백문자를 단일한 공백문자로 간주하고, 선행/후행 공백은 빈 문자열에 포함시키지 않음
    * maxsplit이 -1인 경우에는 제한이 없음

```python
'a,b,c'.split(' ')
# ['a,b,c']
'a b c'.split()
# ['a', 'b', 'c']
```

* 'separator'.join([iterable])

  * 반복가능한 컨테이너 요소들을 separator(구분자)로 합쳐 문자열 반환

  * iterable에 문자열이 아닌 값이 있으면 TypeError 발생

```python
''.join(['3', '5'])
# 35
```

* 기타 변경: 이런게 있다는 정도로만 이해하고 넘어가기

  print() 씌우는 이유? 문자열은 스스로 바뀌는 경우가 없기 때문!



---



## 2. 리스트(List)



* 리스트의 정의

  * 변경 가능한 값들의 나열된 자료형

  * 순서를 가지며, 서로 다른 타입의 요소를 가질 수 있음

  * 변경 가능하며(mutable), 반복 가능함(iterable)

  * 항상 대괄호 형태로 정의하며, 요소는 콤마로 구분

    * [0, 1, 2, 3, 4, 5]

      ​             .append(), .pop(), .sort(), .count() 를 많이 사용



#### 1. 값 추가 및 삭제

* .append(x)

  * 리스트에 값을 추가함

```python
cafe = ['starbucks', 'tomntoms', 'hollys']
# ['starbucks', 'tomntoms', 'hollys']
cafe.append('banapresso')
# ['starbucks', 'tomntoms', 'hollys', 'banapresso']
```

* .extend(iterable)

  * 리스트에 iterable 항목을 추가함

  * 함수에 어떤 값을 넣는지가 매우 중요!

```python
cafe = ['starbucks', 'tomntoms', 'hollys']
# ['starbucks', 'tomntoms', 'hollys']
cafe.extend(['cafe', 'test'])
# ['starbucks', 'tomntoms', 'hollys', 'cafe', 'test']

+++++++++++++++++++++++++++++++

[예시]
a = ['apple']
a.extend('banana', 'mango')
print(a)
# 이러면 타입 에러 발생!

따라서 아래 부분을 [] 로 묶어야 함
a.extend('banana', 'mango')      # 앞전 코드에서 이 부분을
a.extend(['banana', 'mango'])    # 이렇게 바꿔서 입력하자
```

* .insert(i, x)

  * 정해진 인덱스 위치 i에 값을 추가함

```python
cafe = ['starbucks', 'tomntoms']
# ['starbucks', 'tomntoms']
cafe.insert(0, 'start')
# ['start', 'starbucks', 'tomntoms']

+++++++++++++++++++++++++++++++

cafe = ['starbucks', 'tomntoms']
# ['starbucks', 'tomntoms']
cafe.insert(1000, 'start')
# ['starbucks', 'tomntoms', 'end']
리스트 길이보다 큰 경우(1000) 맨 뒤에('end') 오는 것을 알 수 있다
```

* .remove(x)

  * 리스트에서 값이 x인 것을 삭제

```python
numbers = [1, 2, 3, 'hi']
# [1, 2, 3, 'hi']
numbers.remove('hi')
# [1, 2, 3]

+++++++++++++++++++++++++++++++

numbers = [1, 2, 3]   # 위에서 'hi' 를 지운 상태에서
numbers.remove('hi')  # 이 명령어를 한 번 더 입력하면
# 값이 없으니까 ValueError !!
```

* .pop(i)

  * 정해진 위치 i에 있는 값을 삭제하고, 그 항목을 반환함

  * i가 지정되지 않으면, 마지막 항목을 삭제하고 반환함

```python
numbers = ['hi', 1, 2, 3]
# ['hi', 1, 2, 3]
pop_numbers = numbers.pop()
# 3
# ['hi', 1, 2]

+++++++++++++++++++++++++++++++

numbers = ['hi', 1, 2, 3]
# ['hi', 1, 2, 3]
pop_numbers = numbers.pop(0)
# 'hi'
# [1, 2, 3]
```

* .clear()

  * 모든 항목을 삭제함

```python
numbers = [1, 2, 3]
# [1, 2, 3]
numbers.clear()
# []
```

* index(x)

  * x값을 찾아 해당 index 값을 반환

```python
numbers = [1, 2, 3, 4]
print(numbers)
# [1, 2, 3, 4]
print(numbers.index(3))
# 2
print(numbers.index(100))
# ValueError: 100 is not in list !!
```

* .count(x)

  원하는 값의 개수를 반환

```python
numbers = [1, 2, 3, 1, 1]
numbers.count(1)
# 3
numbers.count(100)
# 0

# 이걸 if문으로 작성할 줄 알아야함!
```

* .sort()

  원본 리스트를 정렬함. None 반환

  sorted 함수와 비교할 것

```python
상황1) .sort() 
numbers = [3, 2, 5, 1]
result = numbers.sort()
print(numbers, result)
# [1, 2, 3, 5] None

+++++++++++++++++++++++++++++++

상황2) sorted
numbers = [3, 2, 5, 1]
result = sorted(numbers)
print(numbers, result)
# [3, 2, 5, 1] [1, 2, 3, 5]
```

* .reverse()

  순서를 반대로 뒤집음(정렬하는 것이 아님). None 반환

```python
numbers = [3, 2, 5, 1]
result = numbers.reverse()
print(numbers, result)
# [1, 5, 2, 3]
```



---



## 3. 컬렉션

⭐생략⭐ 중요하지 않음



---



## 4. 세트(set)

⭐생략⭐ 중요하지 않음



---



## 5. 딕셔너리(Dictionary)



#### 1. 조회

* .get(key[,default])
  * key를 통해 value를 가져옴
  * KeyError가 발생하지 않으며, 디폴트값을 설정할 수 있음(기본: None)

```python
방법1)
my_dict = {'apple': '사과', 'banana': '바나나'}
my_dict['pineapple']
# 무조건 에러가 발생

방법2) 에러가 발생하지 않음
my_dict = {'apple': '사과', 'banana': '바나나'}
print(my_dict.get('pineapple'))
# None
print(my_dict.get('apple'))
# 사과
print(my_dict.get('pineapple'), 0)
# 0
```



#### 2. 추가 및 삭제

* .pop(key[,default])

  * key가 딕셔너리에 있으면 제거하고 해당 값을 반환

  * 그렇지 않으면 디폴트를 반환

  * 디폴트값이 없으면 KeyError

```python
my_dict = {'apple': '사과', 'banana': '바나나'}
data = my_dict.pop('apple')
print(data, my_dict)
# 사과 {'banana': '바나나'}
```

* .update([other])
  * 값을 제공하는 key, value로 덮어씁니다.

```python
my_dict = {'apple': '사과', 'banana': '바나나'}
my_dict.update(apple='사과')
print(my_dict)
# {'apple': '사과', 'banana': '바나나'}
```

