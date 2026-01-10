row=eval(input("Enter a row: "))
while row%2==0:
    print('Enter again')
    row=eval(input("Enter a row: "))
#输出空心菱形，只需注意首尾为*即可，其余用空格补上
top_row=(row+1)//2
for i in range(1,top_row+1):
    for j in range(0,top_row-i):
        print(' ',end='')
    for j in range(0,2*i-1):
        if j==0 or j==2*i-2:
            print('*',end='')
        else:
            print(' ',end='')
    print()
for i in range(1,top_row):
    for j in range(1,i+1):
        print(' ',end='')
    for j in range(0,2*top_row-1-2*i):
        if j==0 or j==2*top_row-2*i-2:
            print('*',end='')
        else:
            print(' ',end='')
    print()