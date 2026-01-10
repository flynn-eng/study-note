#使用小括号创建
t=('hello',[10,20,30],'python','world')#元组是不可变数据类型
print(t)
#使用内置函数tuple（）创建元组
t=tuple('helloworld')
print(t)

t=tuple('123456')
print(t)
print('10 exist in t?',(10 in t))
print('10 not exist in t?',(10 not in t))
print('max',max(t))
print('min',min(t))
print('len',len(t))
#如果元组中只有一个值
t=(10)
print(t,type(t))#认为是这个值的数据类型
t=(10,)
print(t,type(t))#不省逗号还是元组类型
#删除
del(t)
#print(t)#此时报错元组已经消失了