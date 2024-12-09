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
            obstructions.append(np.array([obstruction_col.start()+1,-row_index-1]))
            # obstructions.append(complex(obstruction_col.start(),-row_index))
    if not np.any(guard):
        if re.search(regex_guard,line):
            guard_col = re.finditer(regex_guard,line)
            # guard=complex(list(guard_col)[0].start(),-row_index)
            guard=np.array([list(guard_col)[0].start()+1,-row_index-1])
        
max_x=len(data)
min_y=len(data[0].strip())*-1
print(max_x)
print(min_y)

step = np.array([[0,1],
                 [1,0],
                 [0,-1],
                 [-1,0]])
# print(step[0])
# print(step[0]+step[1])
# print(np.dot(step[0],np.transpose(step[1])))
# exit()

step_index=0
step_count=0
positions=[]

positions.append([guard,step_index])

loop_obstructions=[]

while(1):
    # print(f"{guard}\t{step[step_index]}")
    
    hit_obstruction_flag=False
    loop_obstruction_flag=False
    guard_next=guard+step[step_index]

    # check if guard has left map
    if guard_next[0]==0 or guard_next[0]>max_x or guard_next[1]<min_y or guard_next[1]==0:
        break
    
    # check if guard hit obstruction
    for obstruction in obstructions:
        if (guard_next==obstruction).all():
            hit_obstruction_flag=True
            step_index=(step_index+1)%4
            break

    if hit_obstruction_flag:
        continue
    
    # check if loop obstruction exists
    #   > if we turn right, we'll go back onto the existing path without hitting an obstruction

    # pre-calcs for loop
    right_step_index=(step_index+1)%4
    right_step=step[right_step_index]
    guard_right_position=guard*np.absolute(step[step_index])
    guard_dot_product = np.dot(guard,np.transpose(step[right_step_index]))
    obstruction_before_position=False

    for position in positions:
        if (guard_right_position==position[0]).any(): # if position is left/right of the guard
            # print(guard)
            # print(f"{guard_right_position}\t{step[step_index]}")
            # print(f"{position[0]}")
            # print(guard_right_position==position[0])
            # print(f"{step[position[1]]}\t{right_step}")
            # print()
            if position[1] == right_step_index: # if step vector in the same direction
            
                
                separation=np.dot(position[0],np.transpose(step[position[1]]))-guard_dot_product
                if separation<0: # guard is in front of position, try next position
                    continue
                elif separation<2: # guard is on or 1 step behind position, can't be any obstructions there
                    loop_obstruction_flag=True
                    break
                else:
                    # check if there's an obstruction between the guard and the position
                    for i in range(1,separation): # take a right step and check for obstructions
                        guard_right_step=guard+i*right_step
                        for obstruction in obstructions:
                            # if (guard_right_position==obstruction).any(): # if the obstruction is line with the guard
                            if (guard_right_step==obstruction).all(): # if the guard steps into an obstruction
                                obstruction_before_position=True
                                break
                    
                        if obstruction_before_position: # there was an obstruction between the guard and the position, stop stepping towards the position
                            break
                    else: # no obstructions between guard and position
                        loop_obstruction_flag=True
                        break
                if loop_obstruction_flag:
                    break
        
    if loop_obstruction_flag:
        loop_obstructions.append(guard_next)

    guard=guard_next
    positions.append([guard,step_index])

# print(len(np.unique(positions,axis=1)))
# print([positions[i] for i in range(len(positions))])
# unique_positions=[]
# for position in positions:
#     # print(f"{position[0],step[position[1]]}")
#     for unique_position in unique_positions:
#         if (unique_position==position[0]).all():
#             break
#     else:
#         unique_positions.append(position[0])
# print(unique_positions)
# print(len(unique_positions))
# print(len(np.unique([positions[i][0] for i in range(len(positions))],axis=1)))
# print()
# print(loop_obstructions)
print(len(loop_obstructions))
# print(len(np.unique(loop_obstructions,axis=1)))