def WelcomeMessage():
    print('Welcome to your IdeaBank TM')
    print('How can I help you today')
def Instruction():
    print('Enter A to add new idea')
    print('Enter X to exit')
    print('Enter S to show your ideas')
def ConnectFile():  
    return open("./codecool/PythonProjects/SelfAssigned/ideabank.txt", "w+")    

idea_list = []
new_idea = ''
decision = ''
is_running = True
file_link = ConnectFile()

WelcomeMessage()

while is_running:

    Instruction()
    decision = input()

    if decision == 'A' or decision == 'a':
        new_idea = input('Enter new idea: ')
        idea_list.append(new_idea)
        file_link.write('%s\n' % idea_list)
    elif decision == 'X' or decision == 'x':
        print('Bye bye. It was nice to meet you!')
        is_running = False
    elif decision == 'S' or decision == 's':
        print('Your Idea_List:')
        for idea in idea_list:
            print(idea)
    else:
        print('Incorrect operation... Try Again!')

    



