correct_input = False # this is a boolean value -- it can be either true or false.


def some_function():
    global a
    a = 10
    

while not correct_input: # this is a while loop
    try:
        height = int(input("Enter height of rectangle: "))
        width = int(input("Enter width of rectangle: "))
    except ValueError:
        print("Please enter valid integers for the height and width.")
    else: # this will be executed if there is no value error
        correct_input = True

print(a)
