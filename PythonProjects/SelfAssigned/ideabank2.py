import sys
import os

def FileConnection():
    return open('/home/ubuntuwanderer/codecool/PythonProjects/SelfAssigned/ideabankDB.txt', 'r+')

def ReadFile():
    return open('/home/ubuntuwanderer/codecool/PythonProjects/SelfAssigned/ideabankDB.txt', 'r')

def WriteFile():
    return open('/home/ubuntuwanderer/codecool/PythonProjects/SelfAssigned/ideabankDB.txt', 'w')


def FileConnection2():
    return open('/home/ubuntuwanderer/codecool/PythonProjects/SelfAssigned/ideabankDB.txt', 'w+')


def ShowList(given_list):
    index = 0
    print('Your ideabank: ')
    for elements in given_list:
        index += 1
        print(str(index) + '. ' + elements)

def Delete(list, db, command):
    delete = int(command)
    count = 0
    l.pop(delete)
    for line in l:
            print('wtf................')
            count += 1
            if count != delete:
                db.write(line + '\n')

def Add_To_List(l, db, idea):
    l.append(idea)
    db.write(idea + '\n')
  

text_db = ReadFile()
is_running = True
idea_list = []
idea_list = text_db.readlines()
text_db.close()

for el in idea_list:
    print(el)

if len(sys.argv) > 1:
    is_running = False
    if sys.argv[1] == '--list':
        ShowList(idea_list)
    elif sys.argv[1] == '--delete':
        text_db = WriteFile()
        Delete(idea_list, text_db, sys.argv[2])
        ShowList(idea_list)
        text_db.close()  
    else:
        print('wrong')

print('Enter e to exit...')
while is_running:
    index = 0  
    decision = input('What is your idea: ')
    if decision == 'e' or decision == 'E':
        is_running = False
    else:
        text_db = WriteFile()
        Add_To_List(idea_list, text_db, decision)
        ShowList(idea_list)
        text_db.close()

