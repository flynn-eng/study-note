#fruits = {'apple', 'banana', 'cherry'}集合无序，所以对应case不一定对得上，列表有序
fruits =['apple', 'banana', 'cherry']
counts=[1,2,3]
for f,c in zip(fruits,counts):
    match f,c:
        case 'apple',1:
            print('1 apple')
        case 'banana',2:
            print('2 banana')
        case 'cherry',3:
            print('3 cherry')