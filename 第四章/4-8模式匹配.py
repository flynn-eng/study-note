score=input('Enter the level of the score:')
match score:
    case 'A':
        print('A')
    case 'B':
        print('B')
    case 'C':
        print('C')
    case _:#处理不在case范围内的值
        print('Invalid input')