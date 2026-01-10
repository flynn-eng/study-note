data=eval(input("Enter data: "))#去引号输入
match data:
    case{'name':'zyz','age':18}:
        print("Hello Zyz,字典")
    case[10,20,30]:
        print('列表')
    case(10,20,30):
        print('元组')
    case _:
        print('none')#相当于else

