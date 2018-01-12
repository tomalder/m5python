number = int(input('input a number:\n'))
list = []
while number > 0:
    a = number % 2
    number = number // 2
    list.append(a)
list.reverse()
print(list)
