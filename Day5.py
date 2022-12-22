#Importing regular expressions
import re

with open('./Day5.txt', 'r') as file:
    data = file.readlines()
    cratesDiagram = data[:8]
    data = data[10:]

stackAmount = 9

#Initialize 2d list an add contents in it based on input
crates = []
for i in range(stackAmount):
    crates.append([])

for line in cratesDiagram:
    count = 0
    for i in range(0, len(line), 4):
        if not line[i:i+3].isspace():
            crates[count].append(line[i:i+3])
        count += 1

for stack in crates:
    stack.reverse()
    #print(stack)

#Do commands from data given
for line in data:
    command = re.findall(r"\d+", line)
    #print(command) #prints a list such as: ['3', '9', '4']
    move = int(command[0])
    #Must subtract 1 as diagram follows base 0
    start = int(command[1])-1
    end = int(command[2])-1
    """
    #Part 1
    for i in range(move):
        item = crates[start].pop()
        crates[end].append(item)
    """
    #Part 2
    itemsMoved = crates[start][-move:]
    del crates[start][-move:]
    #Must go through each item in a for loop
    #   Otherwise it just adds a whole list
    for item in itemsMoved:
        crates[end].append(item)

    # for stack in crates:
    #     print(stack)

#End result
for stack in crates:
   print(stack)