s=0
i=1
while i<101:
    if i%2==1:
        i=i+1
        continue#跳出本次循环
    s=s+i
    i=i+1
print('1-100 even sum:',s)