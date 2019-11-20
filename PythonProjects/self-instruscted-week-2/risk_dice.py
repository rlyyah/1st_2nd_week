import random


def Roll_Dice(units_amount):
    roll_list = []
    for i in range(0, units_amount, 1):
        if units_amount > i:
            dice = random.randint(1, 6)
            roll_list.append(dice)
    return roll_list


def Sort_Roll(roll_list):
    iteration = 1
    while iteration < len(roll_list):
        jteration = 0
        while jteration <= len(roll_list)-2:
            if roll_list[jteration] < roll_list[jteration + 1]:
                temp = roll_list[jteration + 1]
                roll_list[jteration] = roll_list[jteration + 1]
                roll_list[jteration + 1] = temp
            jteration = jteration + 1
        iteration += 1
    return roll_list
            

def Print_Rolls(roll_list):
    print_result = ''
    for i in range(len(roll_list)):
        print_result += str(roll_list[i])
        if i < len(roll_list)-1:
            print_result += '-'
    return print_result


def Define_Amount_of_Units(who):
    ask = True
    while ask:
        decision = input(f'How many units {who}: ')
        try:
            decision = int(decision)
            ask = False
        except ValueError:
            print('u have to enter a number!')
    return decision


attacker_roll = []
defender_roll = []
attacker_units = Define_Amount_of_Units('attack')
defender_units = Define_Amount_of_Units('defend')
attacker_deaths = 0
defender_deaths = 0
show_result = ''

attacker_roll = Roll_Dice(attacker_units)
defender_roll = Roll_Dice(defender_units)     

# attacker_roll = Sort_Roll(attacker_roll)
# defender_roll = Sort_Roll(defender_roll)
attacker_roll.sort(reverse=True)
defender_roll.sort(reverse=True)

print('Dice:')

show_result = Print_Rolls(attacker_roll)
print(f"    Attacker: {show_result}")

show_result = Print_Rolls(defender_roll)
print(f"    Defender: {show_result}")    

decider_roll = []
if len(defender_roll) > len(attacker_roll):
    decider_roll = attacker_roll 
else:
    decider_roll = defender_roll

for i in range(len(decider_roll)):
    if attacker_roll[i] <= defender_roll[i]:
        attacker_deaths += 1
    else:
        defender_deaths += 1
print('Outcome:')
print(f"    Attacker: Lost {attacker_deaths} units.")
print(f"    Defender: Lost {defender_deaths} units.")
