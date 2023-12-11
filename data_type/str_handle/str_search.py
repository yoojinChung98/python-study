'''
* 문자열 관리 함수, 메서드

- 함수: 모듈 내부에서 공용적으로 사용할 수 있는 기능의 집합.(단독 호출)
- 메서드: 클래스에 소속된 함수, 특정 자료형 전용 함수. (클래스 전용 함수)
'''

# 내장 함수 len(): 순차형 자료(sequence)의 내부 데이터 개수를 구함.
# len()은 문자열에서만 쓸 수 있는게 아니에요. 함수에요.
s = 'python programming'

count = 0
# for c in s:
#     count += 1
# print('s의 글자수: ', count)
print('s의 글자수: ', len(s))

'''
# 문자열 메서드 find(), rfind() # r = rear 라는 뜻!
- 문자열 내부에 특정 문자를 검색하여 해당 문자의
인덱스 번호를 알려줍니다.
- find()는 앞에서부터, rfind()는 뒤에서부터 탐색
'''

print('-' * 40)
print(s.find('o'))
print(s.rfind('o')) #뒤에서 부터 o 를 찾고, 그 글자의 인덱스값을 알려줌

# program이 문자열 변수 s에 있다면 해당 단어의 첫번째 인덱스를 반환
print(s.find('program')) # 7 : 해당 단어는 s 라는 문자열의 7번 인덱스부터 시작합니당!

print(s.find('메롱')) # -1: 탐색 시 문자를 발견하지 못했다면 -1 반환.



message = """
    내가 그린 기린 그림은 목이 긴 기린 그림이고
    니가 그린 기린 그림은 목인 안 긴 기린 그림이다.
"""
print('"기린" 단어의 출현 횟수: ', message.count('기린'))


'''
- 특정 문자가 있는 인덱스나 번호 및 횟수는 관심 없고
단순히 포함 여부만 빠르게 확인하고 싶다면 in 키워드를 사용합니다.
'''
print('-' * 40)

# True / False 값이 옴
print('a' in s) # 다 필요없고 존재 유무만 보고 싶다면 in 을 때려버리면 됨.
print('q' in s) 
print('z' not in s) 


'''
- 사용자에게 데이터를 입력받을 때 입력값의 형태를 검사하는 메서드

1. isdecimal(): 모든 문자가 숫자 형태인지를 검사.
2. isalpha(): 모든 문자가 영문 알파벳인지를 검사.
3. islower(): 모든 문자가 영문 소문자인지를 검사.
4. isupper(): 모든 문자가 영문 대문자인지를 검사.
'''

print('-' * 40)

print('15 + 8 = ???')

while True:
    answer = input('> ')

    if answer.isdecimal():
        answer = int(answer)
    else:
        print('정답은 숫자로만 입력하세요!')
        continue

    if answer == 23:
        print('정답입니다!')
        break
    else:
        print('틀렸습니다ㅜ')

