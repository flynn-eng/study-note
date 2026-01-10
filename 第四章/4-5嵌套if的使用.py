#一个条件判断下有另外几个条件，喝酒后对喝酒量的划分
answer=input('请问你喝酒了吗:')
if answer=='y':
    proof=eval(input('how much:'))
    if proof<20:
        print('no')
    elif proof<80:
        print('a little')
    else:
        print('big')
else:
    print('nothing')