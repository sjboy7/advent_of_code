import re

regex_mul = r'mul\(\d{1,3},\d{1,3}\)'
regex_num = r'(\d{1,3})'
regex_do = r'(do\(\))'
regex_dont = r'(don\'t\(\))'
# regex_valid_start = r'(.+?)^don\'t\(\)'
regex_valid_start = r"^(.*?)don\'t\(\)"
regex_valid_middle = r"do\(\)(.+?)don't\(\)"
# regex_valid_end = r'do\(\)(.+?)'
regex_valid_end = r'(?<=do\(\)).*$'

# regex_valid_end = r'(^(don\'t\(\))(.+?)$'
# regex_valid_all = r'^(.+)don\'t\(\)'
# regex_valid_all = r'(.+)do\(\)$(.+)don\'t\(\)(.+)'
regex_valid_all = r''

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
# valid_extracted = [re.findall(regex_valid_all, data[i]) for i in range(len(data))]
valid_extracted=[]
for line_no, line in enumerate(data):
    valid_start= list(re.findall(regex_valid_start, line))
    if len(valid_start): # (there is a don't)
        valid_extracted.append(valid_start)
        valid_end =  list(re.findall(regex_valid_end, line))
        if len(valid_end): # (there is a do)
            valid_middle = list(re.findall(regex_valid_middle, line))
            if (re.search(regex_do, valid_start[0])): # (there is a do in the first extract)
                valid_middle = valid_middle[1:] # drop the first extract in the middle
            if(re.search(regex_dont, valid_end[0])): # (there is a don't in the last extract)
                valid_end=None # drop the end extract
            if (valid_middle): valid_extracted.append(valid_middle)
            if (valid_end): valid_extracted.append(valid_end)

    else: # there aren't any don't, the whole line is valid
        valid_extracted.append(line)

    # print(f"{line_no}\t{valid_extracted}")
    # print()
    # print(valid_end)
    # exit()
    # print(valid_start[0])
    # exit()
    
    # break
    
# so now valid_extracted is just the valid sections of the input
# exit()
# print(len(valid_extracted))
# print(valid_extracted[0])
# print(valid_extracted[1])
# print(valid_extracted[2])

# exit()
muls_extracted=[]

# print(len(valid_extracted))
# print(valid_extracted[0])
# exit()
for line in valid_extracted:
    # print(line)
    # print()
    for extract in line:
        mul_extracted=re.findall(regex_mul, extract)
        if (mul_extracted):
            muls_extracted.append(mul_extracted)
    
# exit()
print(muls_extracted)
# exit()
# print(muls_extracted[0])
sum=0
for muls in muls_extracted:
    for mul in muls:
        print(mul)
        vals_extracted=list(map(int, re.findall(regex_num,mul)))
        sum+=vals_extracted[0]*vals_extracted[1]

print(sum)



exit()

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