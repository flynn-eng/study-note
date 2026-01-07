# study-note
s='hello world'
print('e在s中存在吗？',('e'in s))#判断字符e是否在字符串中存在
print('v在s中存在吗？',('v'in s))#判断字符v是否在字符串中存在
#not in的使用
print('e在s中不存在吗？',('e'not in s))#判断字符e是否在字符串中存在
print('v在s中不存在吗？',('v'not in s))#判断字符v是否在字符串中存在
#内置函数的使用
print('len():',len(s))#求长度
print('max():',max(s))#求最大值，ascii值
print('min():',min(s))
#序列对象的方法，使用序列的名称，打点调用
print('index():',s.index('e'))#e在字符串中第一次出现的索引位置
#print('index():',s.index('v'))报错v不存在，无索引
print('s.count():',s.count('e'))#统计e在字符串中出现的次数
