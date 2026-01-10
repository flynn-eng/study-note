s1='hello'
s2='world'
print(s1+s2)
#使用join操作
print(''.join([s1,s2]))#使用空字符串进行拼接
print('*'.join([s1,s1,s2]))#前面的符号代替逗号
#直接拼接
print('hello''world')
#使用格式化字符串进行拼接
print('%s%s'%(s1,s2))
print(f'{s1} {s2}')
print('{0}{1}'.format(s1,s2))