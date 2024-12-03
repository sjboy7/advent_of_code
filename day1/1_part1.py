list1 = []
list2 = []
distances = []

with open('1_input', 'r') as f:
    for line in f:
        list1.append(int(line.split()[0]))
        list2.append(int(line.split()[1]))

# print(list1[:5])
list1.sort()
list2.sort()

# print(list1[:5])

for i in range(len(list1)):
    distances.append(abs(list1[i] - list2[i]))

print(sum(distances))
