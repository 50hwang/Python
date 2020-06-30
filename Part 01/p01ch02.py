# Header

#Part 01 파이썬 기초 핵심 과정
#Chapter 02 파이썬 기초 코딩
print('')
print('Part 01 파이썬 기초 핵심 과정')
print('Chapter 02 파이썬 기초 코딩')
print('')

# /Header

#Print 함수의 이해(1)
print('\n\n\nPrint 함수의 이해(1)\n')

# Q01
print('\n\nQ01\n')

print('Hello, World!')
print("Hello, World!")
print('''Hello, World!''')
print("""Hello, World!""")

# Q02
print('\n\nQ02\n')

print("Hello, World!")
print()
print('''Hello, World!''')

# Q03
print('\n\nQ03\n')

print('2020', '03', '29', sep='-')
print('gaenyum88', 'gmail.com', sep="@")

# Q04
print('\n\nQ04\n')

print('Welcome to ', end='')
print('the black paradise', end=', ')
print('friends.')

# Q05
print('\n\nQ05\n')

print('Hello, world!!')
print('\tMy name', 'Sooin', sep=" : ", end=".\n")
print('\t\tMy age' '33', sep=" is ", end=", OK?")

#Print 함수의 이해(2)
print('\n\n\nPrint 함수의 이해(2)\n')

# Q06
print('\n\nQ06\n')

print('{} and {}' .format('You', 'Me'))

# Q07
print('\n\nQ07\n')

print('{} and {}' .format('You', 'Me'))

# Q08
print('\n\nQ08\n')

print('{s} am {c}' .format(s='I', c='a boy'), end='.\n')

# Q09
print('\n\nQ09\n')

print("%s's favofite number is %d. And his number is %d" %('Sooin', 9, 50), end=".\n")

# Q10
print('\n\nQ10\n')

print("Test1: %5d, Price: %4.2f" %(2, 3.141592654))
print("Test2: %5d, Price: %4.2f" %(22222, 22333.1414213))

# Q11
print('\n\nQ11\n')

print("Test3: {0: 5d}, Price: {1: 4.2f}" .format(776, 6534.123))
print("Test4: {a: 5d}, Price: {b: 4.2f}" .format(a=776, b=6534.123))

#Print 함수의 이해(3)
print('\n\n\nPrint 함수의 이해(3)\n')

# Q12
print('\n\nQ12\n')

print('print(""you"")는 에러가 난다.')
print("'you'")
print('"you"')

# Q13
print('\n\nQ13\n')

print("\"you\"")

#몸 풀기 코딩 해보기(1)
print('\n\n\n몸 풀기 코딩 해보기(1)\n')

# Q14
print('\n\nQ14\n')

import sys

print("Input Encoding :")
print(sys.stdin.encoding, "\n")

print("Output Encoding :")
print(sys.stdout.encoding, "\n")

# Q15
print('\n\nQ15\n')

myName = "GoodBoy"

# Q16
print('\n\nQ16\n')

myName = "GoodBoy" #<ㅡ 값을 바꿀 수 있다.

if myName == "GoodBoy":
	print("Good!")
else:
	print("What?")

# Q17
print('\n\nQ17\n')

for i in range(2, 10):
	for j in range(1, 10):
		print('%d * %d = '%(i, j), i*j)

# Q18
print('\n\nQ18\n')
def greeting():
	print("Hello, Good to see you.")
	
greeting()


# End of this chapter
print('\n\n\n< That\'s all, folks!! >\n')