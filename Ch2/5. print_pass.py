# 코딩 테스트 문제 풀이 과정, 알고리즘 공부하는 과정에서 디버깅 작업을 수행할 때 가장 많이 쓰이는 명령은 print()다.
# print()를 통해 어떻게 값들을 확인할 수 있는지 다음 예시들을 통해 살펴보자.
print('A1', 'B2')
# 콤마(,)는 한 칸 공백이 Default로 설정되어 있으며, 그대로 출력하면 띄어쓰기로 값을 구분해줌
# 다음과 같이 sep parameter로 구분자를 콤마(,)로 지정해줄 수도 있음
print('A1', 'B2', sep=',')
# print() 함수는 항상 줄바꿈을 하기 때문에 긴 루프의 값을 반복적으로 출력하면 디버깅하기 어려움
# 줄바꿈을 희망하지 않는 경우 end parameter를 공백으로 처리해 줄바꿈을 할 수 없도록 설정할 수 있음. 다음 예시를 확인해보자.
print('aa', end=' ')
print('bb')
# list내 변수들을 출력하기 희망한다면 join을 이용해서 출력할 수 있음
a = ['AA', 'BB', 'CC']
print(' '.join(a))
# format을 활용해 변수들을 print() 함수에서 출력할 수 있음
idx = 1
fruit = 'Apple'
print('{0}: {1}'.format(idx+1, fruit))
# index를 생략해서 구현할 수 도 있음
print('{}: {}'.format(idx+1, fruit))
# f-string(formated string literal)을 토대로도 구현 가능. f-string은 python 3.6 이상에서만 구동 가능
print(f'{idx+1}: {fruit}')

# pass : python에서 pass는 아무 것도 하지 않는 기능. 보통 불필요한 오류를 방지하고자 사용
class MyClass(object):
    def method_a(self):
        pass

    def method_b(self):
        print("Method B")

c = MyClass()
c.method_b()

# locals() : local symbol table dictionary를 가져오는 method이다. 글만 봤을 때는 잘 이해가 안 될 수 있으니 예시를 통해 살펴보자.
import pprint
pprint.pprint(locals())
# locals()는 로컬에 선언된 모든 변수를 조회할 수 있는 강력한 명령이며 디버깅할 때 정말 많은 도움이 되는 method이다. 
# local scope에 제한해서 정보를 조회할 수 있기 떄문에 class 내 특정 메소드 내부에서나 함수 내부의 local 정보를 조회해 잘못 선언한 부분이 없는지 확인하는 용도로 활용 가능하다.
# 특히 변수명을 일일이 찾아낼 필요 없이 local scope에 정의된 모든 변수를 출력하기 때문에 편리하다.