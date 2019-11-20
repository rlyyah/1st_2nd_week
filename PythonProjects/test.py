first = 10
second = 5
third = first//second
print(third)

if third == 2:
    print('int')
elif third >= 2:
    print('float')
else: 
    print("the fuck you lookin' at?!")

myForList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'finish']

for element in myForList:
    print(element)

myWhileList = [9, 8, 7, 6, 5, 4, 3, 2, 1]
index = 0
while index < len(myWhileList):
    print(myWhileList[index])
    index += 1

#filling list
fillTheList = []
for element in myWhileList:
    fillTheList.append(element)
    print(str(element) + ' has been added to the list')
#clearing list
index = len(fillTheList)-1
while index >= 0:
    print(str(fillTheList[index]) + ' is being removed...')
    fillTheList.pop(index)
    index -= 1
#for element in fillTheList:
 #   print(str(element) + ' has been deleted from the list')
  #  fillTheList.pop(0)    
#showing empty list


if len(fillTheList) == 0:
    print('list is empty')
else:
    for element in fillTheList:
        print(str(element) + ' is still in the list')