'''
* 내장함수 range()

- 순차적으로 증가하는 정수의 순차적 자료형을 만들 때
대괄호 안에 데이터들을 콤마로 일일히 나열하는 것은
한계가 있기 때문에, range()함수를 통해 보다 쉽게
순차형 반복 범위를 지정할 수 있습니다.

ex) range(begin, end, step)
- begin은 값이 포함되지만(이상), end는 값이 포함되지 않습니다. (미만)
'''

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list1)

list2 = list(range(1,11, 1)) # 1 부터 11 미만(즉 10까지) 범위를 잡아서 list로 변환해줌 range(이상,미만,step)
print(list2)

list3 = list(range(4, 15)) # step 생략 시 디폴트 값은 1
print(list3)

# 이 방식은 index 잡고싶을 때 이런 모양을 사용한다고 함
list4 = list(range(5)) # range 괄호 안에 값을 한개만 주면 end 로 처리하여 0 부터 5 미만의 값을 범위로 잡음.
print(list4)

print('-' * 40)

# 1 ~ 100 까지의 누적합
total = 0
for n in range(1,101):
    total += n
print('1 ~ 100 까지의 누적 합: ', total)



