# Output and input

print("Hello, world!")

print('Also a string')

print(input())
print(input("Type something: "))

# Variables

# Strings
string1 = "My variable"
print(string1)

# Various integers
a = 5
b = -10
c = 2300982930092848092830298309284290830280965672039874728937209873277840982377842998372774
d = 2

# Floats
pi = 3.1416

# Boolean


# Numeric Input
i1 = int(input("Type an integer: "))
i2 = float(input("Type a float: "))

# Arithmetic
print(a + b - c)
print(a / d)
print(pi * a ** 2)


# List Operations
list_a = [5, -10, 2, 12]
print(list_a[0])
print(list_a[2])
print(len(list_a))
list_a.append(8)

print(list_a)
print(sum(list_a))

list_a.sort()
print(list_a)

list_b = [0, 4, 2, 100, 20]
list_b.pop(2)
list_b.reverse()

# Flow control

## iterating from 0 -> 9
for i in range(10):
    print(i)

## iterating from 15 -> 99
for i in range(15, 100):
    print(i)

while True:
    print("")