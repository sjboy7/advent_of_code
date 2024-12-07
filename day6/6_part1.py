# import cmath
import re
import numpy as np

regex_obstruction = r'\#'
regex_guard = r'\^'

# with open('6_input_example') as f:
with open('6_input') as f:
    data=f.readlines()

# locate obstructions and guard
obstructions=[]
guard=None
for row_index,line in enumerate(data):
    if re.search(regex_obstruction,line):
        obstruction_cols = re.finditer(regex_obstruction,line)
        for obstruction_col in obstruction_cols:
            obstructions.append(complex(obstruction_col.start(),-row_index))
    if not guard:
        if re.search(regex_guard,line):
            guard_col = re.finditer(regex_guard,line)
            guard=complex(list(guard_col)[0].start(),-row_index)
        
max_real=len(data)
min_imag=len(data[0].strip())*-1


step = [complex(0,1),
        complex(1,0),
        complex(0,-1),
        complex(-1,0),
        ]

step_index=0
step_count=0
unique_positions=[guard]
while(1):
    guard_next=guard+step[step_index]
    for obstruction in obstructions:
        if guard_next==obstruction:
            step_index=(step_index+1)%4
            break
    else:
        guard=guard_next
        if guard.real<0 or guard.real>=max_real or guard.imag>0 or guard.imag<=min_imag:
            break
        if not(np.isin(guard,unique_positions)):
            unique_positions.append(guard)


print(len(unique_positions))
exit()