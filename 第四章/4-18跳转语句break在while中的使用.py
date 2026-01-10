#if和break通常一起使用
sum=0
i=0
while i<11:
    sum=sum+i;

    if sum>20:
        break
    i=i+1
print(i)
