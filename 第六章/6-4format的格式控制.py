s='hello world'
print('{0:*<20}'.format(s))#显示宽度20，左对齐，空白用*填充,0即对应format中的第一个元素
print('{0:*>20}'.format(s))
print('{0:*^20}'.format(s))#居中对齐
print(s.center(20,'*'))
#千位分隔符，只适用于整数和浮点数,三位一个逗号
print('{0:,}'.format(987654321))
print('{0:,}'.format(987654321.7865))
#浮点数小数精度
print('{0:.2f}'.format(987654321.7865))
#字符串，表示的最大显示长度
print('{0:.5}'.format('helloworld'))
#整数类型
a=425
print('二进制:{0:b},十进制:{0:d},八进制:{0:o},十六进制:{0:x}'.format(a))
#浮点数类型，科学计数法，百分比形式
b=3.1415926
print('{0:.2f},{0:.2E},{0:.2e},{0:.2%}'.format(b))