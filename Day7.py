with open('./Day7Test.txt', 'r') as file:
    data = file.readlines()

dir = {}

temp = {}

currentDir = ""

for line in data:
    line = line.replace("\n", "")
    line = line.split(" ")
    if line[0] == "$":
        print(line)
        command = line[1]
        if command == "cd":
            currentDir = line[2]
            if(currentDir == "/"):
                currentDir = "base"
            print(currentDir)
    else:
        pass