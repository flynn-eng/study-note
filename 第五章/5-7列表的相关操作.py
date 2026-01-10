lst=['hello','world']
print('原列表',lst,id(lst))
#增加元素的操作，lst.append
lst.append('sql')
print('增加元素后',lst,id(lst))#增加元素后地址不变，可变数据类型，可以在内存对应位置进行修改
#使用insert(index,x)在index位置上插入元素x
lst.insert(1,'python')
print(lst)
#列表元素的删除操作，lst.remove('xxx'),删除xxx
lst.remove('python')
print(lst)
#使用pop(index)根据索引将元素取出，在进行删除
print(lst.pop(1))#此处index是索引
print(lst)
#清除列表中的所有元素lst.clear()，清空，输出为【】
#列表的反向
lst.reverse()
print(lst)
#列表的拷贝
new_lst=lst.copy()
print(new_lst,id(new_lst))
#列表元素的修改
#根据索引直接修改
lst[1]='mysql'
print(lst)


