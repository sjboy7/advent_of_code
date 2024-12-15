import re
from collections import deque

# with open('9_input_example') as f:
#     data = f.readlines()[0].strip()

with open('9_input') as f:
    data = f.readlines()[0].strip()

# extract blocks
dots = deque() # [index, num blocks]
blocks_original = deque() # [index, num blocks, value]
blocks_rearranged = deque() # [index, num blocks, value]
block_index=0
for index, num in enumerate(data):
    num=int(num)
    if (index & 1):
        dots.append((block_index, num))
    else:
        blocks_original.append((block_index, num, index>>1))
    block_index+=num

# rearrange blocks
while(1):
    dot_index, dot_count = dots[0]
    block_index, block_count, block_value = blocks_original[-1]
    if block_index<dot_index:
        break
    if block_count==dot_count:
        blocks_rearranged.append((dot_index, block_count, block_value))
        dots.popleft()
        blocks_original.pop()
    elif block_count>dot_count:
        blocks_rearranged.append((dot_index, dot_count, block_value))
        dots.popleft()
        blocks_original.pop()
        blocks_original.append((block_index, block_count-dot_count, block_value))
    elif block_count<dot_count:
        blocks_rearranged.append((dot_index, block_count, block_value))
        blocks_original.pop()
        dots.popleft()
        dots.appendleft((dot_index+block_count, dot_count-block_count))

# calc checksum
checksum=0
for block in blocks_original:
    checksum+=sum([(block[0]+i)*block[2] for i in range(block[1])])

for block in blocks_rearranged:
    checksum+=sum([(block[0]+i)*block[2] for i in range(block[1])])

print(checksum)