lst=['hello','world','python','php']
for item in lst:
    print(item)
#使用for循环，range函数，len()函数，根据索引进行遍历
for i in range(0,len(lst)):
    print(i,'->',lst[i])
#使用enumearte()函数
for index,item in enumerate(lst):
    print(index,'->',item)#index在此处是序号不是索引，没定义时默认从零开始
#手动修改序号的初始值
for index,item in enumerate(lst,start=1):#从1开始的序号
    print(index,'->',item)