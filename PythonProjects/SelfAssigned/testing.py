import time
import random

highscore_read = []
highscore_write = []
date = str(time.localtime().tm_mday) + '/' + str(time.localtime().tm_mon) + '/' + str(time.localtime().tm_year)
time = str(time.localtime().tm_hour) + ':' + str(time.localtime().tm_min)
word = 'Warsaw'

filename = "./marimba.txt"



rf = open(filename, 'r')

for lines in rf:
    arr = lines
    highscore_read.append(lines)

rf.close()

for els in highscore_read:
    splitted = els.split(' ')
    splitted[0] = int(splitted[0])
    splitted[-1] = splitted[-1].replace('\n', '')
    print(splitted)
    highscore_write.append(splitted)
    


if len(highscore_write) < 2:
    for i in range(9):
        number = random.randint(10,150)
        name = 'Player' + str(i)
        entrance = [number, name, date, time, word]
        highscore_write.append(entrance)
else:
    number = random.randint(10,150)
    name = input('Enter your name: ')
    entrance = [number, name, date, time, word]
    #highscore_write.append(entrance)

highscore_write.sort(reverse=True)




wf = open(filename,'w+')

for i in range(len(highscore_write)):

    line = f"{highscore_write[i][0]} {highscore_write[i][1]} {highscore_write[i][2]} {highscore_write[i][3]}"
    line = line + f" {highscore_write[i][4]}\r\n" 
    wf.write(line)

    
wf.close()
