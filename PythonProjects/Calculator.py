def Addition(a, b):
    return str(a + b)
def Substraction(a, b):
    return str(a - b)
def Multiplication(a, b):
    return str(a * b)
def Division(a, b):
    try:
        value  = a / b
    except ZeroDivisionError:
        print('do not divide by 0 moron!')
        exit()
    return str(value)

num_a = 0
num_b = 0
operation = ''
result = 0

while True: 

    num_a = input('Enter a number(or a letter to exit) ')
    try:
        num_a = int(num_a)
    except ValueError:
        print('thanksie! BYE')
        exit()
    operation = input('Enter an operation (+,-,*,/) ')
    num_b = input('Enter another numer ')
    try:
        num_b = int(num_b)
    except ValueError:
        print('thanksie! Bye')
        exit()    
    

    if operation == '+':
        print('Result is: ' + Addition(num_a, num_b))
    elif operation == '-':
        print('Result is: ' + Substraction(num_a, num_b))
    elif operation == '*':
        print('Result is: ' + Multiplication(num_a, num_b))
    elif operation == '/':
        print('Result is: ' + Division(num_a, num_b))
    else:
        print('wrong operation :/')
