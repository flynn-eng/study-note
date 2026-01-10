lst=[88,89,99,00,78]#这个print出来00会变成0
print(lst)
for index in range(len(lst)):
    if lst[index]!=0:
        lst[index]=lst[index]+1900
    else:
        lst[index]=lst[index]+2000
print(lst)
for index,value in enumerate(lst):
    if lst[index]!=0:
        lst[index]=lst[index]+1900
    else:
        lst[index]=lst[index]+2000
print(lst)
