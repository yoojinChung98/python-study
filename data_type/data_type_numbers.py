'''
# 파이썬은 정수타입이 여러개가 아니구 전부 Integer로 받을 수 있다규 합니댱.
* 정수형 (Integer)
- 수치형 타입 중 정수형(int)은 양수, 음수의 정수값을 표현하며 소수점 이하 자리는 표현할 수 없습니다.

- 다른 언어는 저장 범위가 타입마다 정해져 있지만,
파이썬은 메모리가 허용하는 한 무수히 많은 정수를 저장할 수 있습니다.
'''

num = -4321
print(type(num))

# 다른 진법의 정수 표현하는 방법 : 접두어를 붙여줍니다
# 0b: inal : 2진수
# 0o: octa : 8진수
# 0x: hexa : 16진수
a = 0b1011
b = 0o77
c = 0xAC00

# 정수를 다른 진법으로 변경하려면,,,
# 2진수 bin(), 8진수 oct(), 16진수 hex() 를 사용합니다.
print(bin(33)) # 10진수 33을 이진수로 출력. # 0b100001
print(oct(0b100001)) # 2진수 100001을 8진수로 출력. # 0o41
print(hex(8923)) # 10진수 8923을 16진수로 출력. # 0x22db


'''
* 실수형 (floation point)

- 실수형 자료에는 10진수형 소수점 표현 방식과
지수형 표현방식을 사용한 실수값을 저장할 수 있습니다.
- 범위는 따로 없습니다.
'''

f = 85.432
print(type(f))

g = 9.832e13 # e13 : 10의 13승
print(g)

h = 9.832e-4
print(h)



'''
* 복소수형 (complex)

- 복소수는 제곱해서 음수가 되는 가상의 수
- 허수를 나타내는 접미사는 j를 사용합니다.
'''
i = 1 + 2j
print(type(i))


'''
* 논리형 (boolean)

- 논리형 데이터 타입은 명제가 참이면 True 거짓일 경우 False 값을 가집니다.

- 파이썬에서는 숫자(정수)를 논리판단에 사용하기 때문에 논리형을 숫자형으로 취급함
'''
b1 = True
b2 = False
# b3 = false # (X) : 첫글자를 소문자로 작성하면 변수로 인식함.


# 파이썬은 문자열도 동등, 비동등 비교가 가능합니다.
# 대/소문자까지 정확하게 일치해야먄 True 가 리턴됨.
password = 'abc1234!'
print(password == 'Abc1234!')



