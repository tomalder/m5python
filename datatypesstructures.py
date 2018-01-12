'''data types apply to a single object
data types that are commonly used are
interger int, this is a whole number 
string str, a string is any character you can type using the keyboard in quotes
float, this is a number with a decimal point
boolean True False, this will only be either True or False'''

a = input('Please enter a number: ') #INPUTS ARE ALWAYS STRINGS, to make a input a number we use casting
#to do this we must wrap the input in the form we want
print('The number you entered was:',a) #The , automaticly places a space
b = a*5
print('Your number multiplied is:'+b) #The + does not place a space
c = int(a)*7 # makes a an interger and then multiplies it as an interger
print('Your number is now as an interger:',c) # a multiplied as an interger
#print('Your number is now as an interger:'+c)
# You cannot add differnet datatypes togther like in the code above
print('Your number is now as an interger: '+str(c))
'''datatypes can be collected togther into datastructures
there are 4 main datastructures
list, in python a list is a collection of multiple data types that can be edited
'''
list = ['hello',4.2,7,True]
print('my list is:',list)
list [0] = str('hi') # the str in the list has been replaced by a new string
# the 0 is the postion in the list so the first item in the list will be replaced (counting from 0)
print('my list is now:',list)
list.append(False) # adds an item to the end of a existing list
print('my list is now now:',list)

tuple = ('ok',4,9.8,False)
print('my tuple is:',tuple)
print(tuple[0]) # prints first term in tuple
# the differnece between a tuple and a list is that a list can be changed but a tuple cannot be changed