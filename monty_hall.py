import random

# things = ["car","goat","goat"]
# doors = []

#print(random.randint(0,2))
#things.pop(1)
#doors.append("apple")

# doors.append(things.pop(random.randint(0,2)))
# doors.append(things.pop(random.randint(0,1)))
# doors.append(things.pop(random.randint(0,0)))


switch_door_wins = 0 
keeping_door_winds = 0
for a in range(10000):
    things = ["car","goat","goat"]
    doors = []

    doors.append(things.pop(random.randint(0,2)))
    doors.append(things.pop(random.randint(0,1)))
    doors.append(things.pop(random.randint(0,0)))

    chosen_door = random.randint(0,2)

    free_door = random.randint(0,2)

    while chosen_door == free_door:
        free_door = random.randint(0,2)

    if doors[chosen_door] == "car":
        keeping_door_winds += 1
    else:
        switch_door_wins += 1

print("switch_door: ",switch_door_wins, " keeping_wins:",keeping_door_winds) 


    



