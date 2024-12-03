list1 = []
list2 = []
similarity = []

with open('1_input', 'r') as f:
    for line in f:
        list1.append(int(line.split()[0]))
        list2.append(int(line.split()[1]))

similarity_score = 0

for i in range(len(list1)):
    occurrence=0
    for j in range(len(list2)):
        if list2[j] == list1[i]:
            occurrence +=1
    similarity_score+=list1[i]*occurrence
    # print(f"{i}\t{list1[i]}\t{occurrence}\t{similarity_score}")




print(similarity_score)
