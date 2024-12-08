# import cmath
import re
import numpy as np


regex_obstruction = r'\#'
regex_guard = r'\^'

with open('6_input_example') as f:
# with open('6_input') as f:
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
positions=[]
positions.append([guard,step_index])
loop_obstructions=[]

while(1):
    print(f"{guard}\t{step[step_index]}")
    hit_obstruction_flag=False
    loop_obstruction_flag=False
    guard_next=guard+step[step_index]

    # check if guard has left map
    if guard_next.real<0 or guard_next.real>=max_real or guard_next.imag>0 or guard_next.imag<=min_imag:
        break
    
    # check if guard hit obstruction
    for obstruction in obstructions:
        if guard_next==obstruction:
            hit_obstruction_flag=True
            step_index=(step_index+1)%4
            print()
            break

    if hit_obstruction_flag:
        continue
    
    # check if loop obstruction exists
    #   > if we turn right, we'll go back onto the existing path without hitting an obstruction

    for position in positions:
        # print(position[0].imag)
        # print(position[0].real)

        if (position[0].real == guard.real): # guard is same x axis as existing position
            if (position[1] == (step_index+1)%4): # turning right with would set us on that path
                
                if position[0].imag*step[(step_index+1)%4].imag>=guard.imag: # guard is not ahead of position
                    
                    for obstruction in obstructions:
                        if(int(obstruction.imag) in range(int(min(position[0].imag,guard.imag)), int(max(position[0].imag,guard.imag))+1)): # no obstructions between us and position
                            loop_obstruction_flag=True
                            print(f"HIT\n{position}\t{[guard,step_index]}")
                            break
                    if loop_obstruction_flag:
                        break
        if (position[0].imag == guard.imag): 
            if (position[1] == (step_index+1)%4): 
                
                if position[0].real*step[(step_index+1)%4].real>=guard.real:
                    for obstruction in obstructions:
                        if(int(obstruction.real) in range(int(min(position[0].real,guard.real)), int(max(position[0].real,guard.real))+1)): # no obstructions between us and position
                            loop_obstruction_flag=True
                            print(f"HIT\n{position}\t{[guard,step_index]}")
                            break
                    if loop_obstruction_flag:
                        break

        #     for obstruction in obstructions:
        #         if(int(obstruction.imag) in range(int(min(position[0].imag,guard.imag)), int(max(position[0].imag,guard.imag)))):
        #             loop_obstructions.append(guard_next)
        #             loop_obstruction_flag=True

        # if (position[0].imag == guard.imag):
        #     for obstruction in obstructions:
        #         if(int(obstruction.real) in range(int(min(position[0].real,guard.real)), int(max(position[0].real,guard.real)))):
        #             loop_obstructions.append(guard_next)
        #             loop_obstruction_flag=True

    if loop_obstruction_flag:
        loop_obstructions.append(guard_next)
        
    #             if any([obstruction.imag == i for i in range(position.imag-guard.imag)]):




    #     if position==[guard,(step_index+1)%4]:
    #         print("HIT")
    #         loop_obstructions.append(guard_next)
    #         break
    #     elif         # real component matches guard real and no obstructions between guard and position
    #     elif # same but imag component
    

    guard=guard_next
    positions.append([guard,step_index])



print(len(set([positions[i][0] for i in range(len(positions))])))
print(loop_obstructions)
exit()