import re
line = 'asdf fjdk; afed, fjek,asdf,     foo'

n = re.split(r'[:,\s]\s*', line)
print(n)