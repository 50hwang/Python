# Header

#Part 01 파이썬 기초 핵심 과정
#Chapter 04 파이썬 데이터 타입
print('')
print('Part 01 파이썬 기초 핵심 과정')
print('Chapter 02 파이썬 데이터 타입')
print('')

# /Header



# 데이터 타입, 숫자형 및 연산자(1)
print('\n\n\n데이터 타입, 숫자형 및 연산자(1)\n')

# 종류별 변수 선언
v_str1 = "Niceman"	#문자열
v_boo1 = True		#불리언
v_str2 = "Goodboy"	#문자열
v_float = 10.3		#숫자값 - 실수
v_int = 7			#숫자값 - 정수
v_list = [3,5,7]	#리스트
v_tuple = (3,5,7)	#튜플
v_set = {3,5,7}		#셋
v_dict = {
	"name" : "Kim", "age" : 25
}

# 각 변수 타입 식별
print('\n\n\n각 변수 타입 식별\n')
print("v_str1 = ", type(v_str1))
print("v_boo1 = ", type(v_boo1))
print("v_str2 = ", type(v_str2))
print("v_float = ", type(v_float))
print("v_int = ", type(v_int))
print("v_list = ", type(v_list))
print("v_tuple = ", type(v_tuple))
print("v_set = ", type(v_set))
print("v_dict = ", type(v_dict))

# 숫자 연산자
print('\n\n\n숫자 연산자\n')
i1 = 39
i2 = 939
big_int1 = 999999999999999999999999999
big_int2 = 777777777777777777777777777
f1 = 1.234
f2 = 3.784
f3 = .5
f4 = 10.

print(i1 * i2)
print(big_int1 * big_int2)
print(f1 ** f2)
print(f3 + i2) 				# 자동으로 형 변환 ; 실수 + 정수 ㅡ> 실수
print("f3 + i2의 종류는 : ", type(f3 + i2))


# 형 변환
print('\n\n\n형 변환\n')

a = 5.
b = 4
c = 10
sum = a + b
print('a = ', type(a))
print('b = ', type(b))
print('sum = ', type(sum))

# float에서 int로 형변환
print(int(sum))

# int에서 float로 형변환
print(float(c))

# int에서 complex로 형변환
print(complex(1.2))

# bool을 int, complex로 형변환
print(int(True))
print(int(False))
print(complex(False))

# 단항 연산자
print('\n\n\n단항 연산자\n')

y = 100				# y 초기값
y += 100 			# y = y + 100
print("y = ", y) 	# 200
y *= 50 			# y = y * 50
print("y = ", y) 	# 10000


# 수치 연산 함수
print('\n\n\n수치 연산 함수\n')

print(abs(-7)) 			# 절댓값
n = divmod(100, 8)		# divmod = 100을 8로 나눈 몫과 나머지를 한 tuple로 보낸다.
n1, n2 = divmod(100, 8)	# divmod = 100을 8로 나눈 몫과 나머지를 각각 두 int로 보낸다.
print("mok = ", 100//8, type(100//8))	# 100을 8로 나눈 몫만 추출
print("namoji", 100%8, type(100%8))		# 100을 8로 나눈 나머지만 추출
print(n, type(n))		# 단일계산값
print(n1, type(n1), n2, type(n2))

import math

print(math.ceil(5.12))	# 올림 ; math 모듈 필수!!
print(round(5.12))		# 반올림 ; math 모듈 가져올 필요 없이 본래 round다.
print(math.floor(5.12))	# 버림 ; math.floor을 써도 되고, 그냥 int(5.12)로 정수부만 빼내도 되고.

# End of this chapter
print('\n\n\n< That\'s all, folks!! >\n')