binary1 = int(input('input a 1-8 bit binary number:\n'))
binary2 = int(input('input a 1-8 bit binary number:\n'))
a = str(binary1)
b = str(binary2)
c = []
d = []
for digit in a:
    c.append(int(digit))
for digit in b:
    d.append(int(digit))
print(c)
print(d)
if c [0] == 1:
    if d [0] == 1:
        c[0] = 0
        d[0] = 0

print(c)
print(d)