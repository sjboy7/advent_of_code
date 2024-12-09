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
guard_start=None
for row_index,line in enumerate(data):
    if re.search(regex_obstruction,line):
        obstruction_cols = re.finditer(regex_obstruction,line)
        for obstruction_col in obstruction_cols:
            obstructions.append(complex(obstruction_col.start(),-row_index))
    if not guard_start:
        if re.search(regex_guard,line):
            guard_col = re.finditer(regex_guard,line)
            guard_start=complex(list(guard_col)[0].start(),-row_index)
        
max_real=len(data)
min_imag=len(data[0].strip())*-1
# print(obstructions)


step = [complex(0,1),
        complex(1,0),
        complex(0,-1),
        complex(-1,0),
        ]
def walk(obstructions,guard):

    step_index=0
    positions=[]
    positions.append([guard, step_index])
    while(1):
        
        guard_next=guard+step[step_index]
        for obstruction in obstructions:
            if guard_next==obstruction:
                step_index=(step_index+1)%4
                break
        else:
            
            guard=guard_next
            if guard.real<0 or guard.real>=max_real or guard.imag>0 or guard.imag<=min_imag:
                return positions # we made it out
            positions.append([guard, step_index])
        if [guard,step_index] in positions[:-1]:
            return 0 # we're in a loop
        
        
        
loop_obstructions=[]
positions=walk(obstructions,guard_start)
test_obstructions=[]

unique_positions=set(list(positions[i][0] for i in range(len(positions))))
# print(len(unique_positions))
for index, loop_obstruction in enumerate(unique_positions):
    test_obstructions=obstructions.copy()
    test_obstructions.append(loop_obstruction)
    if not(walk(test_obstructions,guard_start)):
        loop_obstructions.append(loop_obstruction)
        # print(f"{index}\t{len(loop_obstructions)}")
    
print(len(loop_obstructions))