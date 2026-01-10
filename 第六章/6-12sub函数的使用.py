import re
pattern='黑客|破解'
s=('我想学习python破解一些视频')
news=re.sub(pattern,'xxx',s)
print(news)
#
s2='asdasd?asdsaddsa&dsadsa'
pattern2='[?|&]'#分割以这两个字符为标准，拆分成为一个列表
lst=re.split(pattern2,s2)
print(lst)