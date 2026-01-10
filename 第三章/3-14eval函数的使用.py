s='3.14+3'
print(s,type(s))
x=eval(s)#eval去掉引号，执行语句，通常与input一起使用，用来获得用户输入的数值
print(round(x,1),type(x))#round保留几位小数
age=eval(input('Enter your age:'))#相当于直接赋值为数值而不是字符串
height=eval(input('Enter your height:'))
print(age,height,type(age))
print('----')
hello='北京欢迎你'
print(hello)
print(eval('hello'))#去引号后内部hello仍是字符串
print(eval(hello))#去掉引号后不再是字符串了