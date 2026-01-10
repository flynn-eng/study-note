t=(i for i in range(1,4))
print(t)
#t=tuple(t)
#print(t)
#遍历
#for item in t:    print(item)
#__next__方法
print(t.__next__())
print(t.__next__())
print(t.__next__())#使用这种方法需要把其他遍历的注释掉，才能正常使用
t=tuple(t)#此时转为元组为空元组
print(t)