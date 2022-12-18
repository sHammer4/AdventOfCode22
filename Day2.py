with open('./Day2.txt', 'r') as file:
    data = file.readlines()

points = 0

#Part Two
altPoints = 0
    
for input in data:
    input = input.strip()

    oppInput = input[:1]
    myInput = input[-1:]

    if(myInput == 'X'):
        points += 1
        altPoints += 0
        if(oppInput == 'A'):
            points += 3 #Draw
            altPoints += 3
        elif(oppInput == 'B'):
            points += 0 #Lose
            altPoints += 1
        elif(oppInput == 'C'):
            points += 6 #Win
            altPoints += 2
    elif(myInput == 'Y'):
        points += 2
        altPoints += 3
        if(oppInput == 'A'):
            points += 6
            altPoints += 1
        elif(oppInput == 'B'):
            points += 3
            altPoints += 2
        elif(oppInput == 'C'):
            points += 0
            altPoints += 3
    elif(myInput == 'Z'):
        points += 3
        altPoints += 6
        if(oppInput == 'A'):
            points += 0
            altPoints += 2
        elif(oppInput == 'B'):
            points += 6
            altPoints += 3
        elif(oppInput == 'C'):
            points += 3
            altPoints += 1

print(points)
print(altPoints)
