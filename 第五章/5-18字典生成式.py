import random
d={item:random.randint(1,100) for item in range(4)}
print(d)
#创建两个列表
lst1=[1,2,3]
lst2=[4,5,6]
d={key:value for key,value in zip(lst1,lst2)}
print(d)
