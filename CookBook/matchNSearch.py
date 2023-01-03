text = 'yeah, but no, but yeah, but no. but yeah'
print(text == 'yeah')
print(text.startswith('yeah'))
print(text.endswith('no'))
print(text.find('no'))

import re

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

if re.match(r'\d+/\d+/\dx', text1):
    print('yes')
else:
    print('no')
