import re

regex_mul = r'mul\(\d{1,3},\d{1,3}\)'
regex_num = r'(\d{1,3})'

with open('3_input', 'r') as file:
    data = file.readlines()

lines_extracted = [re.findall(regex_mul, data[i]) for i in range(len(data))]

sum=0
for line in lines_extracted:
    for mul in line:
        vals_extracted=list(map(int, re.findall(regex_num,mul)))
        sum+=vals_extracted[0]*vals_extracted[1]

print(sum)