'''programs help us do human things, but faster.
we use them to solve human problems'''


def timesTable(multi): # def defines a function called timesTab
    answer = [] #LIST
    for numberOftimes in range (1,13): #sets up a for loop 1 to
        answer.append(numberOftimes * multi) # prints out item
    return answer


#takes an integer as input and makes it a number
multi = int(input('''please enter a number\n'''))

answer = timesTable(multi)
#so this is the same as saying timesTable(7)
print('For the number ' + str(multi) + ' The table is')
print(answer)