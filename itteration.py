'''a while loop will always test
that the condition set is True'''

count = 0
while count < 5:
    print(count)
    count = count + 1
# this will print out 0,1,2,3,4

count = 0
while count < 5:
    count = count + 1
    print(count)
# this will print out 1,2,3,4,5


new_user = True
while new_user:
    anwser = input('create new user? ')
    if anwser == 'y':
        print('new user added')
    else:
        print('thank you no more users will be added')
        new_user = False