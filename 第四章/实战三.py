import random
rand=random.randint(1,100)  #产生1-100之间的随机整数
count=1#记录猜数次数
while count<=10:
    number=eval(input('Enter the number:' ))
    if number==rand:
        print('The number is equal to {}'.format(rand))#format后的内容补充花括号内部的空
        break
    elif number>rand:
        print('The number is less than {}'.format(number))
        count=count+1
    elif number<rand:
        print('The number is greater than {}'.format(number))
        count=count+1
