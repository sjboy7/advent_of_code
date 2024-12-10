import re
import numpy as np


def append_node(node):
    if node[0]>=0 and node[0]<grid_limit_x and node[1]>=0 and node[1]<grid_limit_y:
        nodes.add((node[0],node[1]))
        # for existing_node in nodes:
        #     if (node==existing_node).all():
        #         break
        # else:
        #     nodes.append(node)
            

# with open('8_input_example') as f:
with open('8_input') as f:
    data=f.readlines()

antenna_dict = {}

for row, line in enumerate(data):
    antennas=re.finditer(r'(\d)|[A-Z]|[a-z]',line.strip())
    for antenna in antennas:
        antenna_name=antenna.group()
        antenna_location=np.array([antenna.start(),row])
        if antenna_name in antenna_dict:
            antenna_dict[antenna_name].append(antenna_location)
        else:
            antenna_dict[antenna_name]=[antenna_location]

grid_limit_x=len(data)
grid_limit_y=len(data[0].strip())


nodes=set()
for antenna_name in antenna_dict:
    for i in range(len(antenna_dict[antenna_name])):

        antenna1_pos=antenna_dict[antenna_name][i]
        for j in range(i):
            antenna2_pos=antenna_dict[antenna_name][j]
            separation=antenna1_pos-antenna2_pos
            append_node(antenna1_pos+separation)
            append_node(antenna2_pos-separation)

print(len(nodes))
