print('This is a one line calculator where you can make (+, -, *, /). Enter first and second number and chose the operation')

number1 = float(input('Enter first number: '))
number2 = float(input('Enter secong number: '))

operation = input('Chose the operation: ')

if operation == '+':
    print('Your answer is: ', (number1 + number2))
elif operation == '-':
    print('Your answer is: ', (number1 - number2))
elif operation == '*':
    print('Your answer is: ', (number1 * number2))
elif operation == '/' and number2 == 0:
    print('You can not divide by zero, sorry')
elif operation == '/' and number2 != 0:
    print('Your answer is: ', (number1 / number2))
else:
    print('I cannot understand what operation you want me to do, next time chose something from (+, -, *, /)')