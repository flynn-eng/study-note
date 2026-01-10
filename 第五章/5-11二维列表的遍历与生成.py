#创建
lst=[
    ['城市','环比','同比'],
    ['北京',102,103],
    ['上海',104,504],
    ['深圳',100,39]
]
print(lst)
#遍历使用双层for循环
for row in lst:#row行
    for item in row:
        print(item,end='\t')
    print()
#列表生成式生成一个四行五列的二维列表
lst2=[[j for j in range(6)] for i in range(4)]#列表中的元素为j，外侧为行数，内侧为列数
print(lst2)