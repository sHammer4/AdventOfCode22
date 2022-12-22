with open('./Day6.txt', 'r') as file:
    data = file.readline()

chrNum = 0

"""
#Part 1
for i in range(len(data[:-3])):
    topFour = data[i:i+4]
    #print(topFour)
    for letter in topFour:
        marker = set(topFour)
        if(len(marker) == 4 and chrNum == 0):
            chrNum = i + 4
            print(marker)
"""

#Part 2
for i in range(len(data[:-13])):
    topFourteen = data[i:i+14]
    #print(topFour)
    for letter in topFourteen:
        marker = set(topFourteen)
        if(len(marker) == 14 and chrNum == 0):
            chrNum = i + 14
            print(marker)

print(chrNum)