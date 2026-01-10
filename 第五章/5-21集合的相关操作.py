s={10,20,30}
s.add(100)
print(s)
s.remove(20)
print(s)
#s.clear()
#print(s)
for item in s:
    print(item)
for index,item in enumerate(s,start=1):
    print(index,item)
#集合生成式
p={item for item in range(10) }
print(p)