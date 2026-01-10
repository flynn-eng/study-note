fp=open('note.txt', 'w')#打开文件写write
print('北京欢迎你',file=fp)#将文字输入到nott.txt文件中
fp.close()#关闭文件