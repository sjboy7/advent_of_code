import re

regex = r'mul\(\d{1,3},\d{1,3}\)'

with open('3_input', 'r') as file:
    data = file.readlines()

# print(data[0])

match = re.findall(regex, data[0])
# print(match)

# test_string = "abcmul(2,5)gc"
# match = re.findall(r'mul\(\d{1,3},\d{1,3}\)',test_string)
print(match)
print(len(match))