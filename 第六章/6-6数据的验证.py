print('123'.isdigit())#只认阿拉伯数字
print('一二三'.isdigit())
print('0b0101'.isdigit())
#
print('123'.isnumeric())
print('一二三'.isnumeric())
print('0b0101'.isnumeric())#二进制不识别
#所有字符都是字母,包含中文字
print('hello你好'.isalpha())
print('hello你好123'.isalpha())
print('hello你好一二三'.isalpha())
print('hello你好123'.isalnum())#既认数字也认字母
#判断小写
print('HelloWorld'.islower())
print('HelloWorld'.isupper())
print('helloworld'.islower())
print('helloworld你好'.islower())
print('HE你好'.isupper())#认为中文既是大写也是小写
#所有字符都是首字母大写
print('HelloWorld'.istitle())#W不是首字母也大写了所以false
print('Hello'.istitle())
print('Hello World'.istitle())#加上空格认为world为新字符
#判断是否都是空白字符
print('-'*50)
print('\t'.isspace())
print(' '.isspace())
print('\n'.isspace())