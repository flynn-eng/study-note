s='hello world'
s1=s[0:5:2]#从0开始到5，不包括5，步长为2，进行切片
print(s1)
s1=s[:5:2]#省略开始位置从0开始
print(s1)
s1=s[:5:]#默认步长为1
print(s1)
s1=s[0::1]#默认到结尾
print(s1)
print(s[5::])
print(s[5:])#这两个一样
s1=s[::-1]#字符串逆序输出
print(s1)
s1=s[-1:-12:-1]#字符串逆序输出
print(s1)