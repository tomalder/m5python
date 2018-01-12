# there are 3 constructs in programming
# the 3 constructs are
# the first one is sequence
# the second one is selection ( selection is about making descions )
# the third one is iliteration ( repetition )

answer = input('are you a boy? ')

if answer == 'yes': # a condition
    print('ur a boy')
else:
    print('ur not a boy')




answer = input('are you a boy?\n ')

if answer in ('yes', 'Yes', 'YES', ):
    print('ur a boy')
else:
    print('ur not a boy')



# to find a single solution to our problem of dumb users
# we have to use built in methods to change the user's input
answer = input('are you a boy?\n ')

if answer.upper() == 'YES':
    print('ur a boy')
else:
    print('ur not a boy')



# .lower changes the input all to lower case letters
# .upper changes the input all to upper case letters
answer = input('are you a boy?\n ')

if answer.upper() == 'YES':
    print('ur a boy')
elif answer.lower() == 'no':
    print('ur a girl')
else:
    print('Please can you answer yes or no')
