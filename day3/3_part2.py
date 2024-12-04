import re

regex_mul = r'^mul\(\d{1,3},\d{1,3}\)'
regex_vals = r'(\d{1,3})'
regex_do = r'^do\(\)'
regex_dont = r'^don\'t\(\)'

do=True

with open('3_input', 'r') as file:
    data = file.readlines()


sum=0
for line in data:
    for i in range(len(line)):
        if re.search(regex_do,line[i:]):
            do=True
        if re.search(regex_dont,line[i:]):
            do=False
        mul_operation=re.search(regex_mul,line[i:])
        if(mul_operation) and do:
            mul_vals=list(map(int,re.findall(regex_vals,mul_operation.group())))
            sum+=mul_vals[0]*mul_vals[1]
print(sum)