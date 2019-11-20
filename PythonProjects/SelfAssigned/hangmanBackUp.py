import random
import time

#function which we call to draw a hangman
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
        print('|       RIP')
    else:
        print('')


def Clear_Terminal():
    print(chr(27) + "[2J")
   

#set up passwords list
countrylist_filename = 'countrylist.txt'
f = open(countrylist_filename, 'r')

countrylist = []
countrylist_fixed = []

for el in f:
    countrylist.append(el)

for i in range(len(countrylist)): 
    
    splitted = countrylist[i].split('|')
    splitted[1] = splitted[1].replace(' ','').replace('\n','').upper()
    countrylist_fixed.append(splitted)

f.close()

#set up inicial variables
restart = True

story_a = "Evil SKYNET is trying to take control over the world. And guess who is the only hope for mankind?"
story_b = "Yes, you're right - it's you!"
story_c = "You must prove your skills, knowledge and intelligence by showing that you are smart and able to guess words!"
story_list = [story_a, story_b, story_c]

Clear_Terminal()

#menu loop
while restart:
    
    #set up variables before game
    hp = 7
    guess_count = 0
    pass_array = []
    shown_pass_aray = []
    chosen_letters = []
    not_in_password = []
    guess = ''
    score = 0
    end = False

    #choose password and country
    password_db = countrylist_fixed
    password_draw = random.randint(0, len(password_db)-1)
    password = password_db[password_draw][1]
    country = password_db[password_draw][0]

    #fill list with password letters
    for letter in password:
        pass_array.append(letter)
        shown_pass_aray.append('x')

    #chose a random number from the password
    #letter_draw = random.randint(0, len(pass_array)-1)
    #shown_letter = pass_array[letter_draw]
    #shown_pass_aray[letter_draw] = shown_letter     

    #before the game starts--
    for elem in story_list:
        print(elem)

    print('')
    input('press any key to start the game...')
    
    
    start_time = time.time()

    print('no time for u kid this time')    
    Clear_Terminal()
    #before the game starts--
    
    #main loop of the game
    
    #Lol musze to zrobic ladnie
    while not end:
        
        user_letters = ''
        for letter in shown_pass_aray:
            if letter == 'x':
                user_letters += '-'
            else:
                user_letters += letter

        #print(password)
        instruction = 'The capital of ' + country + ' | ' + 'Password: ' + str(user_letters)
        show_hp = 'Health Points: ' + str(hp) + ' | Missed letters: ' + str(not_in_password)    
        print(instruction)
        print(show_hp)
        
        #user enter his/her guess
        guess = input('enter a letter or a word: ')
        guess = guess.upper()
        guess_count += 1
        Clear_Terminal()
        
        if len(guess) > 1:
            if guess == password:
                score += 100
                end = True
            else:
                hp -= 2
                score -= 10
                if hp <= 0:
                    end = True
        else:
            #check whether the letter has already been guessed
            if guess in chosen_letters:
                print("you've already chosen this letter")
            else:

                #checks whether guessed letter is in the password
                if guess in pass_array:
                    print('nice!')
    
                    #checks whether there is more than 1 instance of particular letter
                    while guess in pass_array:
                        #show guessed letter to a user and delete this letter from hidden password 
                        position = pass_array.index(guess)
                        shown_pass_aray[position] = guess  
                        pass_array[position] = 'x'
                        score += 20
                else:
                    hp -= 1
                    score -= 5
                    not_in_password.append(guess)
                    if hp <= 0:
                        end = True

                #All letters has been guessed
                if 'x' not in shown_pass_aray:
                    end = True

                #add a letter that user guessed to the list
                chosen_letters.append(guess)

        #draw a hangman
        Draw_Hangman(hp+1)

    #GAME IS FINISHED
    if hp <= 0:
        print('you lose!')
        print('The password is: ' + password)
    else:
        print('Well played, you win!')
        print('The password is: ' + password)

    

    #after the game is finished
    elapsed_time = time.time() - start_time
    score = score - round(elapsed_time*3)
    if score < 0:
        score = 0

    print('')
    print('Game took ' + str(round(elapsed_time)) + " seconds.")
    print('You guessed ' + str(guess_count) + ' times.')
    print('Your score is ' + str(score) + ' points.')
    print('')
    #print('Press any key to continue...')
    #input()    

    #Highscore init
    highscore_filename = "highscore.txt"
    highscore_read = []
    highscore_write = []
    entrance = []
    date = str(time.localtime().tm_mday) + '/' + str(time.localtime().tm_mon) + '/' + str(time.localtime().tm_year)
    hour = str(time.localtime().tm_hour)
    minutes = str(time.localtime().tm_min)
    if len(minutes)<2:
        minutes = '0' + minutes
    hour_min = hour + ':' + minutes

    #Highscore read
    rf = open(highscore_filename, 'r')

    for lines in rf:
        arr = lines
        highscore_read.append(lines)

    rf.close()

    #Highscore format
    for els in highscore_read:
        splitted = els.split(' ')
        splitted[0] = int(splitted[0])
        splitted[-1] = splitted[-1].replace('\n', '')
        highscore_write.append(splitted)
    
    #populate if empty
    if len(highscore_write) < 2:
        for i in range(9):
            word = password_db[random.randint(0,len(password_db))][1]
            number = random.randint(10, 150)
            player_name = 'Player' + str(i)
            entrance = [number, player_name, date, hour_min, word]
            highscore_write.append(entrance)
    else:
        word = password.lower().capitalize()
        number = score
        player_name = input('Enter your player_name: ')
        entrance = [number, player_name, date, hour_min, word]
        highscore_write.append(entrance)

    #sorting highscore
    highscore_write.sort(reverse=True)

    #save highscore to txt
    wf = open(highscore_filename,'w+')

    for i in range(len(highscore_write)):

        line = f"{highscore_write[i][0]} {highscore_write[i][1]} {highscore_write[i][2]} {highscore_write[i][3]}"
        line = line + f" {highscore_write[i][4]}\r\n" 
        wf.write(line)

    wf.close()

    #Show highscore
    Clear_Terminal()
    print('Hall of fame')
    for i in range(10):
        msg = f"{i+1}. {highscore_write[i][1]} | {highscore_write[i][0]} | {highscore_write[i][2]} {highscore_write[i][3]} | {highscore_write[i][4]}  "
        print(msg)
    
    print('')    
    print('Press r to restart the game or any other to turn off')
    decision = input()
    Clear_Terminal()
    if decision == 'r' or decision == 'R':
        print('')
    else:
        restart = False    


