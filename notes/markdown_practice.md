# Python



### 1. 개요

![](https://wikidocs.net/images/page/5/pahkey_KRRKrp.png)

파이썬(Python)은 1990년 암스테르담의 귀도 반 로섬(Guido Van Rossum)이 개발한 인터프리터 언어이다. 귀도는 파이썬이라는 이름을 자신이 좋아하는 코미디 쇼인 "몬티 파이썬의 날아다니는 서커스(Monty Python’s Flying Circus)"에서 따왔다고 한다.

> 인터프리터 언어란 한 줄씩 소스 코드를 해석해서 그때그때 실행해 결과를 바로 확인할 수 있는 언어이다.



### 2. 특징

​	**1. 파이썬은 인간다운 언어이다. 아래 코드는 쉽게 해석된다.**

​		`if 4 in [1,2,3,4]: print("4가 있습니다")`

​		*만약 4가 1, 2, 3, 4 중에 있으면 "4가 있습니다"를 출력한다. 라고 말이다.*

​	**2. 파이썬은 간결하다.**

```python
# simple.py
languages = ['python', 'perl', 'c', 'java']

for lang in languages:
    if lang in ['python', 'perl']:
        print("%6s need interpreter" % lang)
    elif lang in ['c', 'java']:
        print("%6s need compiler" % lang)
    else:
        print("should not reach here")
```


​	**3. 공식문서가 자세히 제공된다.**

​		[파이썬 공식문서 링크](https://docs.python.org/3/)
