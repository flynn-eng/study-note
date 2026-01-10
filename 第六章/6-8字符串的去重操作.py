s='adsdsadsadsaasdqqw'
#字符串的拼接及not in
s1=''
for item in s:
    if item not in s1:
        s1=s1+item
print(s1)
#索引加not in
s2=''
for i in range(0,len(s)):
    if s[i] not in s2:
        s2=s2+s[i]
print(s2)
#通过集合去重+列表排序
s3=set(s)
lst=list(s3)
print(lst)
lst.sort(key=s.index)
print(''.join(lst))