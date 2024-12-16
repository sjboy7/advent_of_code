import re
from collections import deque
from collections import OrderedDict

# with open('9_input_example') as f:
    # data = f.readlines()[0].strip()

with open('9_input') as f:
    data = f.readlines()[0].strip()

# extract blocks
dots = deque() # [index, num blocks]
dots=[]
blocks_original = deque() # [index, num blocks, value]
blocks_rearranged = deque() # [index, num blocks, value]
blocks_stuck=deque() # [index, num blocks, value]

block_index=0
for index, num in enumerate(data):
    num=int(num)
    if (index & 1):
        dots.append((block_index, num))
    else:
        blocks_original.appendleft((block_index, num, index>>1))
    block_index+=num


# rearrange blocks
for block_index, block_count, block_value in blocks_original:
    if block_index<dots[0][0]:
        # no more swaps, 
        blocks_stuck.append((block_index, block_count, block_value))
        continue

    for i in range(len(dots)):
        dot_index, dot_count = dots[i]
        if block_index<dot_index:
            blocks_stuck.append((block_index, block_count, block_value))
            break

        if block_count==dot_count:
            blocks_rearranged.append((dot_index, block_count, block_value))
            del dots[i]
            break

        elif block_count<dot_count:
            blocks_rearranged.append((dot_index, block_count, block_value))
            del dots[i]
            dots.append((dot_index+block_count, dot_count-block_count))
            dots.sort()
            break
    else:
        blocks_stuck.append((block_index, block_count, block_value))


# calc checksum
checksum=0
for block in blocks_stuck:
    checksum+=sum([(block[0]+i)*block[2] for i in range(block[1])])

for block in blocks_rearranged:
    checksum+=sum([(block[0]+i)*block[2] for i in range(block[1])])

print(checksum)