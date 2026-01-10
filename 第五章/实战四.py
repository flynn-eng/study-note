s=set()
for i in range(6):
    info=input(f'请输入第{i}位好友的姓名和手机号')#花括号才进去值
    s.add(info)
for item in s:
    print(item)
