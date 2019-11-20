def Draw_Hangman(phase):
    if phase == 7:  
        #1
        print(' ')
        print(' ')
        print(' ')
        print(' ')
        print('|')
        print('|')
        print('|')
    elif phase == 6:
        #2
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
    elif phase == 5:
        #3
        print('...........')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
    elif phase == 4:
        #4
        print('...........')
        print('|          ')
        print('|          ')
        print('|          ')
        print("|          ")
        print('|       TTT')
        print('|       |||')
        print('|       |||')
    elif phase == 3:
        #5
        print('...........')
        print('|         ')
        print('|        O')
        print('|       /|\\')
        print("|       /'\\")
        print('|       TTT')
        print('|       |||')
        print('|       |||')
    elif phase == 2:
        #6
        print('...........')
        print('|        |')
        print('|        O')
        print('|       /|\\')
        print("|       /'\\")
        print('|       TTT')
        print('|       |||')
        print('|       |||')
    elif phase <= 1:
        #7
        print('...........')
        print('|        |')
        print('|        |')
        print('|        O')
        print('|       /|\\')
        print("|       /'\\")
        print('|          ')
        print('|       RIP in pepperoni')
    else:
        print('')