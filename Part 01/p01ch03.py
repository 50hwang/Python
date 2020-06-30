# Header

#Part 01 파이썬 기초 핵심 과정
#Chapter 03 파이썬 가상 환경
print('')
print('Part 01 파이썬 기초 핵심 과정')
print('Chapter 02 파이썬 가상 환경')
print('')

# /Header

import simplejson as json


test_dict = {'1': 95, '4': 77, '3': 65, '5': 100, '2': 88}

#simplejson 실행
print(json.dumps(test_dict, sort_keys=True, indent=4 * ' '))


# End of this chapter
print('\n\n\n< That\'s all, folks!! >\n')