print('Please enter your name')
answer = str(input(' '))

while type(answer) != str:
    answer = str(input('Please enter your name'))

if len(answer) < 1:
    print('Hello stranger!')
else:
    print('Hello ' + answer)
 