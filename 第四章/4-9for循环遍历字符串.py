#遍历字符串
for i in 'hello':
    print(i)
#range函数，range(n,m)产生一个(n,m)的整数序列，包含n不包含m
for i in range(1,11):
    if i%2==0:
        print(i,'even')
    else:
        print(i,'odd')
#累加和
s=0
for i in range(1,11):
    s=s+i
print('sum is:',s)
print('-------100-999之间的水仙花数--------')
for i in range(100,1000):
    a=i%10
    b=i//10%10
    c=i//100%10
    if i==a*a*a+b*b*b+c*c*c:
        print(i,'是水仙花数',sep='')
