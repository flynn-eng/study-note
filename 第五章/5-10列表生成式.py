import random
lst=[item for item in range(1,11)]
print(lst)
lst1=[random.randint(1,100) for x in range(0,10)]#1-100之间的随机整数输出十个
print(lst1)
#从列表中选择符合条件的元素组成新的列表
lst=[i for i in range(1,11) if i%2==0]#lst=[取值 for加上取值范围 if 条件]
print(lst)