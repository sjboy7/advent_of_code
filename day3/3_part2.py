import re

regex_mul = r'mul\(\d{1,3},\d{1,3}\)'
regex_num = r'(\d{1,3})'
regex_do = r'(do\(\))'
regex_dont = r'(don\'t\(\))'
regex_valid_start = r'^(.+)don\'\(\)'
regex_valid_middle = r'do\(\)(.+)don\'t\(\)'
regex_valid_end = r'do\(\)$(.+)'
regex_valid_all = r'^(.+)don\'t\(\)'
# regex_valid_all = r'(.+)do\(\)$(.+)don\'t\(\)(.+)'

do=True

with open('3_input', 'r') as file:
    data = file.readlines()

# extract groups that sit between a do (optional) and a don't
# starts as a do
# if (do), keep searching and extracting mul operations
# if (don't), bypass mul operations until re-activated by a do
# build up array that way, then pass through the same iterative calc

# lines_extracted = [re.findall(regex_mul, data[i]) for i in range(len(data))]
# lines_extracted_iter = [re.finditer(regex_mul, data[i]) for i in range(len(data))]
# do_extracted_iter = [re.finditer(regex_do, data[i]) for i in range(len(data))]
# dont_extracted_iter = [re.finditer(regex_dont, data[i]) for i in range(len(data))]
valid_extracted = [re.findall(regex_valid_all, data[i]) for i in range(len(data))]

print(list(valid_extracted)[0])

# print(list(lines_extracted_iter))
# mul_array=[]
# do_array=[]
# dont_array=[]
# for line in lines_extracted_iter:
#     span_array.append(m.span() for m in line)

# for line in do_extracted_iter:
#     do_array.append(m.span() for m in line)

# for line in dont_extracted_iter:
#     dont_array.append(m.span() for m in line)

# print(len(span_array))
# print(len(lines_extracted))
# print(list(span_array[0]))
# print()
# print(list(lines_extracted[0]))
# print()
# print(list(lines_extracted_iter[0]))
# print()
# print(list(do_array[0]))
# print()
# print(list(dont_array[0]))
# print(len(list(lines_extracted)))

# print(list(span)[0])
# print(lines_extracted[0][0])
exit()

sum=0
for line in lines_extracted:
    for mul in line:
        vals_extracted=list(map(int, re.findall(regex_num,mul)))
        sum+=vals_extracted[0]*vals_extracted[1]

print(sum)