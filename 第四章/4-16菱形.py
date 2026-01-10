row=eval(input("Enter a row: "))
while row%2==0:
    print('Enter again')
    row=eval(input("Enter a row: "))
#输出菱形
top_row=(row+1)//2
for i in range(1,top_row+1):
    for j in range(0,top_row-i):
        print(' ',end='')
    for j in range(0,2*i-1):
        print('*',end='')
    print()
for i in range(1,top_row):
    for j in range(1,i+1):
        print(' ',end='')
    for j in range(0,2*top_row-1-2*i):
        print('*',end='')
    print()