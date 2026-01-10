i=0
while i<3:
    user_name=input('name:')
    user_password=input('password:')
    if user_name=='zyz' and user_password=='275513':
        print('loading')
        i=8
    else:
        if i<2:
            print('Enter again')
        i=i+1
if i==3:
    print('30s后再次尝试')