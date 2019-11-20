numbers = [-5, 23, 0, -9, 12, 99, 105, -43]

avg = 0

for i in range(len(numbers)):
    avg += numbers[i]

avg = avg/len(numbers)

print(avg)
print('====')

numbers = [-5, 23, 0, "kitten", -9, 12, 99, [2, 44], None, 105, -43]

cleared_numbers = []

for i in range(len(numbers)):
    if type(numbers[i]) == type([]):
        for j in range(len(numbers[i])):
            cleared_numbers.append(numbers[i][j])
    elif type(numbers[i])==type(1):
        cleared_numbers.append(numbers[i])


print(cleared_numbers)



    
    

    






