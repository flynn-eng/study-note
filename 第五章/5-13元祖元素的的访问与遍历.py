t=('python','java','ruby')
#根据索引访问元素
print(t[0])
t2=t[0:3:2]#支持切片操作
print(t2)
#元组的遍历
for item in t:
    print(item)
#索引加for，for +range()+len()
for i in range(len(t)):
    print(i,t[i])
#使用enumerate（）
for index,item in enumerate(t):
    print(index,item)
for index, item in enumerate(t,start=1):
    print(index, item)