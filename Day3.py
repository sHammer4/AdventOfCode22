with open('./Day3.txt', 'r') as file:
    data = file.readlines()

priorityCount = 0
groupPriorityCount = 0

def getPriority(letter):
    value = ord(letter)
    if(value > 90):
        value = value - ord('a') + 1
    else:
        value = value - ord('A') + 27
    return value

#Part Two
def findCommonValues(arr1, arr2, arr3):
    #As found through part one, set reduces the array to its unique values
    set1 = set(arr1)
    set2 = set(arr2)
    set3 = set(arr3)
    #Intersection will find common values between the given sets
    return set1.intersection(set2, set3)

group = []
commonValues = []

#Goes through each line
for input in data:
    input = str(input.split()) 
    rucksackLength = len(input)
    frontCompartment = input[2:int(rucksackLength/2)]
    backCompartment = input[int(rucksackLength/2):-2]
    cleanInput = input[2:-2]

    similarLetters = []
    #Goes through each letter of the first half
    for letter in frontCompartment:
        #Goes through each letter of the last half
        for compare in backCompartment:
            if(letter == compare):
                similarLetters.append(letter)
    similarLetters = list(set(similarLetters))    
    
    #matchingLetters = []
    for match in similarLetters:
        priorityCount += getPriority(match)
        count = [frontCompartment.count(match), backCompartment.count(match)]
        #for i in range(min(count)):
            #priorityCount += getPriority(match)
            #matchingLetters.append(match)

    print(cleanInput)
    group.append(cleanInput)
    if(len(group) == 3):
        groupBadge = list(findCommonValues(group[0], group[1], group[2]))
        for item in groupBadge:
            commonValues.append(item)
        group = []

for item in commonValues:
    groupPriorityCount += getPriority(item)

print(groupPriorityCount)

