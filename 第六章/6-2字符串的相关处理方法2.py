s='HelloPython'
#字符串的替换
s1=s.replace('o','你好',1)#count决定替换次数，没写默认全换
print(s1)
#指定宽度内居中
print(s.center(20,'*'))#宽度20，空的位置添加*号
#去掉字符串左右的空格
s='   HelloPython   '
print(s.strip())
print(s.rstrip())#去掉右边空格
print(s.lstrip())
#去除指定字符
s3='dl-helloworld'
print(s3.strip('ld'))#与顺序无关，dl和ld都删去
print(s3.rstrip('ld'))
print(s3.lstrip('ld'))