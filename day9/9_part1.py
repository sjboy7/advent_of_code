import re

with open('9_input_example') as f:
    data = f.readlines()[0].strip()

# with open('9_input') as f:
    # data = f.readlines()[0].strip()[:20]

# extract blocks
blocks = ""
for index, num in enumerate(data):
    if (index & 1):
        blocks = blocks + int(num)*'.'
    else:
        blocks = blocks + int(num)*str(index>>1)
# print(blocks)

# # move blocks
# while re.search(r'\.+\w', blocks):
#     blocks = re.sub(r'^(\w+)(\.)(.+)(\w)(\.*)$', r'\g<1>\g<4>\g<3>\g<2>\g<5>', blocks)

dots=[dot.start() for dot in list(re.finditer(r'\.', blocks))]
# print(dots[0].start())
dot_index=0
# print(dots)
# exit()
# print(blocks[dots[dot_index]])
# exit()
len_numbers=len(blocks)-len(dots)
# print(len_numbers)
# exit()
# for i in range(1,len(blocks)+1):
for i in range(1,len(dots)+1):
    # print(blocks[i*-1])
    if not (blocks[i*-1] == '.'):
        blocks=blocks[:dots[dot_index]]+blocks[i*-1]+blocks[dots[dot_index]+1:]
        # blocks[dots[dot_index]] = blocks[i*-1]
        dot_index+=1
        
    # if i==len_numbers:
    #     break
        # if dot_index == len(dots):
        #     break
    # print(i)
    # print(blocks)
    # input()
        # print()
# print(blocks)
blocks=blocks[:len(blocks)-len(dots)]
print(blocks)
# exit()
# for dot in dots:
    # print(dot.start())

# print(dots)
# exit()
# print(blocks)

# calc checksum
checksum=0
# for index, num in enumerate(blocks[:re.search(r'\.', blocks).start()]):
for index, num in enumerate(blocks):
    checksum+=index*int(num)
print(checksum)