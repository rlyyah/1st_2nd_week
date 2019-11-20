numbers = [-5, 23, 0, -9, 12, 99, 105, -43]

def Find_Min(num_list):
    minimum = num_list[0]
    for num in num_list:
        if num<minimum:
            minimum=num
    return minimum

def Find_Max(num_list):
    maximum = num_list[0]
    for num in num_list:
        if num > maximum:
            maximum = num
    return maximum

def Average(num_list):
    avg = 0
    for num in num_list:
        avg +=num
    avg= avg/len(num_list)
    return avg

    



min_num = Find_Min(numbers)
max_num = Find_Max(numbers)
average = Average(numbers)
print(min_num)
print(max_num)
print(average)

        