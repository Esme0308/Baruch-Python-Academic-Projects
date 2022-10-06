#Place your age
age=float(input('Enter your age\n'))
#To decide who can vote and who is to young. As well as who register
if age<=18:
    print('You are too young to Vote')
else:
    register=input('Are you registered to vote? Yes or No\n')
    if register=="Yes":
        print('You can Vote!')
    else:
        print('You need to register before you can vote')
