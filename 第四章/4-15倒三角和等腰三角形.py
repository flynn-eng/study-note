#倒三角
print('----倒三角----')
for i in range(1,5):
    for j in range(1,6-i):
        print('*',end='')
    print()
#等腰三角形
print('----等腰三角形----')
for i in range(1,5):
    for j in range(1,5-i):
        print(' ',end='')
    for j in range(0,2*i-1):
        print('*',end='')
    print()