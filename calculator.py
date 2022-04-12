import math

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
def power(x, y):
    return x ** y

num1 = int(input('Enter a number: '))
num2 = int(input('Enter another number: '))
print('1. Add')
print('2. Subtract')
print('3. Multiply')
print('4. Divide')
print('5. Power')
op = input('Enter an operator: ')
if op == '1':
    print(str(num1) + ' + ' + str(num2) + ' = ' + str(add(num1, num2)))
elif op == '2':
    print(str(num1) + ' - ' + str(num2) + ' = ' + str(subtract(num1, num2)))
elif op == '3':
    print(str(num1) + ' * ' + str(num2) + ' = ' + str(multiply(num1, num2)))
elif op == '4':
    if num2 == 0:
        print("Imagine that you have zero cookies and you split them evenly among zero friends. How many cookies does each person get? See? It doesn't make sense. And Cookie Monster is sad that there are no cookies, and you are sad that you have no friends. Basically you're stupid.")
    else:
        print(str(num1) + ' / ' + str(num2) + ' = ' + str(divide(num1, num2)))
elif op == '5':
    print(str(num1) + ' ^ ' + str(num2) + ' = ' + str(power(num1, num2)))
else:
    print('Invalid operation.')
