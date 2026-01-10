import re
#search只要能找到就行，match得从头开始
pattern=r'\d\.\d+'
s='I study python 3.11 everyday 2.3 hour'#search只搜索第一个匹配的值
search=re.search(pattern,s)
print(search)
s2='2.1 I study python 3.11 everyday '
search2=re.search(pattern,s2)
print(search2)
print(search2.group())#group输出查找到的内容