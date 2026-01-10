import re
s='I study python 3.11 everyday 2.3 hour'
pattern=r'\d\.\d+'
result=re.findall(pattern,s)#findall得到的是一个列表类型
print(result)