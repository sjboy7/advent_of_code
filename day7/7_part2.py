import re
from itertools import product

# with open('7_input_example') as f:
with open('7_input') as f:
    data=f.readlines()


results_array=[]
values_array=[]
for line in data:
    result, values = line.strip().split(':')
    values = values.split()
    results_array.append(int(result))
    values_array.append(list(map(int,values)))



sum=0
operators_dict={}
operator_options=[-1,0,1]

for i in range(len(results_array)):
    num_operators=len(values_array[i])-1
    if num_operators not in operators_dict:
        operators_array=[operator_options for _ in range(num_operators)]
        full_factorial=list(product(*operators_array))
        operators_dict[num_operators] = [list(full_factorial[i]) for i in range(len(full_factorial))]

    operators_array=operators_dict[num_operators]
    for operators in operators_array:
        result_attempt=values_array[i][0]
        for j in range(len(operators)):
            if operators[j]==-1:
                result_attempt+=values_array[i][j+1]
            if operators[j]==0:
                result_attempt*=values_array[i][j+1]
            if operators[j]==1:
                result_attempt=int(str(result_attempt) + str(values_array[i][j+1]))
        if result_attempt==results_array[i]:
            sum+=result_attempt
            break

print(sum)
