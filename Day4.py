with open('./Day4.txt', 'r') as file:
    data = file.readlines()

contain = 0
overlap = 0

for pair in data:
    #line = line.split()
    pair = pair.replace("\n", "")
    pair = pair.split(',')
    #print(pair)

    START = 0
    END = 1

    first = pair[0].split('-')
    first[START] = int(first[START])
    first[END] = int(first[END])
    # print(first)

    second = pair[1].split('-')
    second[START] = int(second[START])
    second[END] = int(second[END])
    #print(second)

    #print(pair)
    if(first[START] == second[START]):
        contain += 1
        overlap += 1
        #print(f"MATCH 1: {first[START]} = {second[START]}")
    elif(first[START] < second[START]):
        if(first[END] >= second[START]):
            overlap += 1
        if(first[END] >= second[END]):
            contain += 1
            #print(f"MATCH 2: {first[START]} < {second[START]}-{second[START]} <= {first[END]}")
    elif(first[START] > second[START]):
        if(second[END] >= first[START]):
            overlap += 1
        if(first[END] <= second[END]): 
            contain += 1
            #print(f"MATCH 3: {second[START]} < {first[START]}-{first[START]} <= {second[END]}")
print(contain)
print(overlap)