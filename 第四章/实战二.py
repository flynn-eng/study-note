answer='y'
while answer=='y':
    print('welcome to 10086')
    print('1.查询当前余额')
    print('2.查询当前剩余流量')
    print('0.退出系统')
    choice=input('请输入您要执行的操作')
    if choice=='1':
        print('当前余额:200')
    elif choice=='2':
        print('当前剩余流量:100g')
    elif choice=='0':
        print('退出系统')
        break
    else:
        print('unlegal number,enter again')
