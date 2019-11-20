def convert_to_C(temp_in_F):
    temp_in_C = (5/9)*(temp_in_F-32)
    return temp_in_C


proper_unit = True

while proper_unit:
    try:
        temperature = float(input('Enter temperature in Fahrenheit: '))
    except ValueError:
        print('You have to provide a number...')
    else:
        print(f"{temperature} F is {round(convert_to_C(temperature),2)} C")
        proper_unit = False


