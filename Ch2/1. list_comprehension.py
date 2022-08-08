# list comprehension이란? 기존의 list를 기반으로 새로운 list를 생성하는 구문
# 다방면에서 유용하게 활용할 수 있으며 map, filter를 섞어서 사용하면 가독성이 훨씬 좋아짐

# ex1) 홀수인 경우 2를 곱해 출력하라는 리스트 컴프리헨션이다.
[n*2 for n in range(1, 10+1) if n%2 == 1]

# ex1-1) 만약 리스트 컴프리헨션을 사용하지 않고 풀어서 작성한다면 다음과 같이 코드 작성을 할 수 있음
# 작성해야 되는 코드 길이가 상대적으로 길어지기에 효율성이 떨어지는 것을 확인할 수 있음
# 그렇기에 리스트 컴프리헨션을 토대로 리스트 생성이 가능하다면 가급적 리스트 컴프리헨션을 사용하자!
a1 = []
for n in range(1, 10+1):
    if n%2 == 1:
        a1.append(n*2)
a1

# Python Version 2.7 이후 딕셔너리 등에도 비슷한 방식 사용 가능
# a2, a3는 서로 같은 결과물을 출력함
original = {1:'one', 2:'two', 3:'three'}
a2 = {}
# dictionary items method는 key:value 쌍을 내보내는 역할 수행
for key, value in original.items():
    a2[key] = value
a2

a3 = {key: value for key, value in original.items()}
a3

