import urllib.request
import urllib.parse

url = 'http://qspiders.com'
values = {'q': 'python'}
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
print(resp)
respData = resp.status
print(respData)