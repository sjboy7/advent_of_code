# spoilers for day 5 part 1











import cProfile

with open('5_input') as f:
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

def main():

    sum = 0

    for update in updates:
        valid=True
        for rule in rules:
            for i in range(len(update)-1):
                
                if update[i+1]==rule[0]:
                    for j in range(i+1):
                        if update[j]==rule[1]:
                            valid=False
                            break
            
                if(valid==False):
                    break

            if valid==False:
                break
            
        if(valid):
            sum+=update[int(len(update)/2)]

    print(sum)


cProfile.run('main()')