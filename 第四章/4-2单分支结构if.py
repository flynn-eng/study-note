number=eval(input("Enter a number:"))
# 使用if语句
if number==987654 :
    print("The number is 987654")
if number!=987654:
    print("The number is not 987654")
#if判断表达式，是通过比较运算符计算出来的，结果是bool类型
n=98
if n%2:
    print("The number is odd")
if not n%2:
    print("The number is even")
#判断一个字符串为空字符串
s=input("Enter a string:")
if s:
    print('s not empty')
if not s:
    print("s empty")
#表达式也可以是一个单纯的bool值变量
flag=eval(input("Enter a bool:"))
if flag:
    print('flag is True')
if not flag:
    print('flag is False')
#使用if语句时，如果语句块中只有一句代码，可以将语句直接写在冒号后面
a=10
b=5
if a>b:max=a
print('最大值',max)
