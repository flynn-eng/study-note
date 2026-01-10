d={'hello':1,'world':2}
#访问字典中的元素
#（1）使用d[key]
print(d['hello'])
#(2)d.get(key)
print(d.get('hello'))#get对应key的到对应value
#二者区别，如果key不存在，d[key]报错，get（key)可以指定默认值
#print(d['java']),报错
print(d.get('JAVA'))#得到none
print(d.get('java','不存在'))#不显示none此时显示默认值
#字典的遍历
for item in d.items():
    print(item)#key=value组成一个元素
#在使用for循环时，分别获得key，value
for key,value in d.items():
    print(key,value)



