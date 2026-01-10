import re
pattern=r'\d\.\d+'#r避免Python对反斜杠\进行转义处理,一个数字\d加一个点\.加多个数字\d+,若是字符的话用s*表示匹配零个或多个字符，*多个，+多一个
s='I study python 3.11 everyday'#待匹配
match=re.match(pattern,s,re.I)#忽略大小写,match是从头开始查找的
print(match)
s2='33.11 python everyday'
match2=re.match(pattern,s2)
print(match2)
s3='3.11 python everyday'
match3=re.match(pattern,s3)
print(match3)
print('匹配值起始位置',match3.start())
print('匹配值结束位置',match3.end())
print('匹配区间的位置元素',match3.span())
print('待匹配的字符串',match3.string)
print('匹配的数据',match3.group())