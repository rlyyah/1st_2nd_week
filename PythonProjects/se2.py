list_of_food = []
food = ''

while food != 'quit':
    food = input('Which food do you enjoy the most?')
    if food in list_of_food:
        print('This dish is already on the list')
    else:
        list_of_food.append(food)
        print('List of food so far:')
        for element in list_of_food:
            print(element)


