doors = [False]*100
open_doors = []

for i in range(1,101):
    for x in range(i-1,100,i):
        doors[x] = not doors[x]

print(doors)

for i in range(len(doors)):
    if doors[i]==True:
        open_doors.append(i+1)         

print(open_doors)
  




