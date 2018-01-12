'''for loops work for a set number of times
for item in SOMETHING:
    do something
'''
for letter in 'Thomas':
    print(letter)

for item in range(3,6):
    print(item)
#the above will print 3,4,5

for item in range(10):
    print(item)
#prints 0 to chosen number

animals = ['mouse', 'cat', 'dog', 'sheep']
for item in range(len(animals)):
    print(item, animals[item])
#printed out 0 mouse 1 cat 2 dog 3 sheep

#there is also a do while loop, it will work atleast once
'''this is a java script example(won't run)
of a while loop'''

'''
var i = 0;
do {
    i += 1;
    console.log(i);
} while (i <5);

'''
