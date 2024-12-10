import re

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

for i in range(len(results_array)):
    
    operators_dec=1<<(len(values_array[i])-1)
    for j in range(operators_dec):
        result_attempt=values_array[i][0]
        
        operators_bin_array=list(map(int,bin(j)[2:].zfill(len(values_array[i])-1)))
        for k in range(len(operators_bin_array)):
            if operators_bin_array[k]:
                result_attempt+=values_array[i][k+1]
            else:
                result_attempt*=values_array[i][k+1]
            if result_attempt>results_array[i]:
                break
        if result_attempt==results_array[i]:
            sum+=result_attempt
            break
print(sum)