'''
functions help us to organsize our code.
if we need to reapeat a process multiple times, then we should put it in a function.
functions have two basic modes:
the first mode is that our function is that our function simply does something.
the second mode is where the function will do something but give us the result.
'''

#: means next line will be tabbed in

def myfunc():
    for letter in "hello":
        print(letter)

def myfunc2(word):
    for letter in word:
        spelling = word + letter
    return spelling


print("the above is my func",myfunc())
myword = input("please enter a word\n")
print(myword)