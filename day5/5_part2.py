# with open('5_input') as f:
with open('5_input_example') as f:
    data = f.readlines()

# extract rules and updates arrays
rules = []
updates = []

rules_flag=True
for line in data:
    if rules_flag:
        if line=="\n":
            rules_flag=False
        else:
            rules.append(list(map(int,line.strip().split('|'))))
    else:
        updates.append(list(map(int,line.strip().split(','))))


sum = 0
# median_array=[]

for update in updates:
    
    update_valid=False
    rule_valid=True
    while not update_valid:
        # print(update)
        for rule in rules:
            # print(rule)
            for i in range(len(update)-1):
                if(not rule_valid):
                    break

                if update[i+1]==rule[0]:
                    # print(update[i+1])
                    for j in range(i+1):
                        # print(rule)
                        if update[j]==rule[1]:
                            
                            update[i+1], update[j] = update[j], update[i+1]
                            # print(update)
                            rule_valid=False
                            
                            exit()
                            break
            
            if (not rule_valid):
                break
        if (not rule_valid):
            break
        else:
            valid=True
            
        # print()
    sum+=update[int(len(update)/2)]

# print(median_array)
print(sum)