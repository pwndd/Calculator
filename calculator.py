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
    print(num1 + ' + ' + num2 + ' = ' + add(num1, num2))
elif op == '2':
    print(num1 + ' - ' + num2 + ' = ' + subtract(num1, num2))
elif op == '3':
    print(num1 + ' * ' + num2 + ' = ' + multiply(num1, num2))
elif op == '4':
    print(num1 + ' / ' + num2 + ' = ' + divide(num1, num2))
elif op == '5':
    print(num1 + ' ^ ' + num2 + ' = ' + power(num1, num2))
else:
    print('Invalid operator')