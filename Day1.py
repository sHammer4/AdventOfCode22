#Takes the data from the text file Day1.txt as a read (use w for write and a for append)
with open('./Day1.txt', 'r') as file:
    #Stores each line in the txt as an array in data
    data = file.readlines()

group = []
maxSum = 0

#Part two
sumGroup = []

#Foreach loop 
for value in data:
    #rstrip takes out whitespace characters in the string from the Right side
        #Therefore it takes out the newline \n present
    number = value.rstrip()
    if(len(number) != 0):
        #Adds the int parsed number value to the group
        group.append(int(number))
    else:   #Runs when it finds a gap in the numbers
        #Grabs the sum of all numbers in the group
        totalSum = sum(group)
        #Checks if the sum is greater than the max recorded
        if(totalSum > maxSum):
            maxSum = totalSum

        #Part two - adds the total sum value to a new array of sum values
        sumGroup.append(totalSum)

        #Resets the group for the next batch
        group = []

#Part two - sorts the group descending, grabs the top three items, collects the 
#   sum of the top three items
sumGroup.sort(reverse=True)
topThree = sumGroup[:3]
topThreeSum = sum(topThree)

print(maxSum)

print(topThree)
print(topThreeSum)
