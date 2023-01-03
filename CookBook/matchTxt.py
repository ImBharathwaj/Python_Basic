import os
from urllib.request import urlopen

filenames = os.listdir('.')

name = [name for name in filenames if name.endswith(('.c', '.h','.py'))]
print(name)

def read_data(name):
    if name.startswith('https:','http:','ftp:'):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()
