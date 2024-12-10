import re
import numpy as np

with open('8_input_example') as f:
    data=f.readlines()

antenna_dict = {}

for row, line in enumerate(data):
    antennas=re.finditer(r'(\d)|[A-Z]|[a-z]',line.strip())
    # antennas=re.finditer(r'(\d)',line.strip())
    # antennas=re.finditer(r'[A-Z]',line.strip())
    # print(list(antennas.group()))
    # print(list(antennas).start())
    # if (antennas):
    for antenna in antennas:
        antenna_dict[antenna.group()]=np.array([antenna.start(),row*-1])
        # print(antenna.group())

print(antenna_dict)
exit()