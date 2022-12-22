#Importing regular expressions
import re

with open('./Day5.txt', 'r') as file:
    data = file.readlines()
    data = data[10:]


for line in data:
    command = re.findall(r"\d+", line)

    print(command)