# range : generator의 방식을 활용하는 대표적인 함수 
# 다음 예시를 통해 range() 함수의 쓰임을 확인해보자.

# list에서의 활용
list(range(5))
# 단순 range 구문
# range(5)의 경우 range(0, 5)와 동일
range(5)
range(0,5)
# range의 타입은? <class 'range'>
type(range(5))
# range를 활용해서 반복문 출력
for i in range(5):
    print(i, end=' ')
# for문에서 range를 사용할 경우 내부적으로는 generator의 next()를 호출하듯 매번 다음 숫자를 생성
# range 조건만으로도 큰 범위의 숫자를 만들어낼 수 있으며 저장 공간은 훨씬 더 적은 것을 확인할 수 있음. 다음 예시를 살펴보자.
a = [n for n in range(1000000)]
b = range(1000000)
a
b
# a에는 0~1000000까지의 자연수들이 담겨 있는 리스트 형태이며 b는 range 조건만 들어 있는 것을 확인할 수 있음
# a와 b를 비교해보자.
len(a) == len(b)
# True가 반환되는 것을 확인할 수 있음
# 크기를 살펴보자
import sys
sys.getsizeof(a)
sys.getsizeof(b)
# 압도적으로 range 조건만으로 생성한 변수 b의 크기가 작은 것을 확인할 수 있음
# range 조건만으로 생성한 변수 b의 경우 인덱스로도 접근이 가능함
b[999]

# enumerate() : 여러 가지 자료형(list, set, tuple)을 인덱스를 포함한 enumerate 객체로 return
# 사용 방식은 다음 예제를 통해 살펴보자.
a = [1,2,3,2,45,2,5]
# a는 list 객체이며 enumerate를 토대로 어떻게 반환되는지 살펴보자.
enumerate(a)
list(enumerate(a))
# 인덱스와 value가 매핑되어 나오는 것을 확인할 수 있다
# enumerate를 활용하면 깔끔하게 특정 자료형의 인덱스와 값을 출력할 수 있음. 다음 예시를 살펴보자.
for i, v in enumerate(a):
    print(i, v)
