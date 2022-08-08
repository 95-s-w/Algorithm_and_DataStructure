# Generator? 루프의 반복(Iteration) 동작을 제어할 수 있는 루틴 형태를 말한다.
# 임의의 조건으로 숫자 1억 개를ㄷㄱ 만들어내 계산하는 프로그램을 작성한다고 가정했을 때, 이 경우 Generator가 없다면 메모리 어딘가에 숫자 1억 개를 보관하고 있어야 함
# Generator를 이용한다면 단순히 Generator만 생성해두고 필요할 때 언제든 숫자를 만들어낼 수 있다. 
# ex1) yield에 대한 이해
# yield란 Generator가 여기까지 실행 중이던 값을 내보낸다는 의미(단어의 사전적 의미처럼 '양보하다')로 
# 중간값을 리턴한 다음 함수는 종료되지 않고 계속해서 맨 끝에 도달할 때까지 실행된다.
def get_natural_number():
    n = 0
    while True:
        n += 1
        yield n

# 함수 get_natural_number의 경우 리턴 값은 다음과 같이 Generator가 된다.
# <generator object get_natural_number at 0x7fb7a816aba0>
# 만약 Generator를 토대로 다음 값을 출력하고 싶다면 next()를 활용하면 된다.

g = get_natural_number()
g
for _ in range(0, 100):
    print(next(g))
# generator와 next를 토대로 1~100까지 출력하는 반복문이다.

# generator를 토대로 여러 타입의 값을 하나의 함수에서 생성하는 것도 가능하다. 다음 예시를 살펴보자
# ex2
def generator():
    yield 1
    yield 'string'
    yield True

g = generator()
g
# 변수 g에 generator가 반환된 것을 확인할 수 있다.
# next를 토대로 하나의 함수 내 선언된(yield로) 변수들을 차례로 출력할 수 있다.
next(g)
next(g)
next(g)

