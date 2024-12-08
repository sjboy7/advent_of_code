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
            obstructions.append(np.array([obstruction_col.start()+1,-row_index-1]))
            # obstructions.append(complex(obstruction_col.start(),-row_index))
    if not np.any(guard):
        if re.search(regex_guard,line):
            guard_col = re.finditer(regex_guard,line)
            # guard=complex(list(guard_col)[0].start(),-row_index)
            guard=np.array([list(guard_col)[0].start()+1,-row_index-1])
        
max_x=len(data)+1
min_y=len(data[0].strip())*-1
# print(max_x)
# print(min_y)

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
rotation_matrix=np.array([[0,1],[-1,0]])
positions=[]
# print(positions)
# exit()

positions.append([guard,step_index])
# print(positions)
# print(obstructions)
# exit()
loop_obstructions=[]

while(1):
    # print(guard)
    # exit()
    print(f"{guard}\t{step[step_index]}")
    # print(guard*step[step_index])
    
    
    # print(positions[-1])
    hit_obstruction_flag=False
    loop_obstruction_flag=False
    guard_next=guard+step[step_index]
    # print(guard_next)

    # check if guard has left map
    if guard[0]==0 or guard[0]>=max_x or guard[1]<=min_y or guard[1]==0:
        print("out")
        break
    
    # check if guard hit obstruction
    for obstruction in obstructions:
        # print(obstruction)
        # exit()
        if (guard_next==obstruction).all():
        # if (guard_next==obstruction):

            hit_obstruction_flag=True
            step_index=(step_index+1)%4
            print()
            break
        # exit()

    if hit_obstruction_flag:
        continue
    
    # check if loop obstruction exists
    #   > if we turn right, we'll go back onto the existing path without hitting an obstruction

    print(guard*np.absolute(step[step_index]))
    # print(np.matmul(guard,rotation_matrix))
        
    for position in positions:
        # print(position[0].imag)
        # print(position[0].real)
        # separation_vector=position[0]-guard
        
        # print(position)
        # print(np.dot(guard,np.transpose(step[position[1]])))
        # print(separation_vector)
        # print(separation_vector)
        # exit()
        # if position[0][0]==guard[0] or position[0][1]==guard[1]: # guard is aligned with position in x or y
        # if (position[1] == (step_index+1)%4): # turning right with would set us on that path
        if (guard*np.absolute(step[step_index])==position[0]).any():
        # if (np.matmul(guard,rotation_matrix)==position[0]).any():
        
            if (position[1] == (step_index+1)%4): # turning right with would set us on that path
            
                print(f"Hit\t{position[0]}")
                separation=np.dot(position[0],np.transpose(step[position[1]]))-np.dot(guard,np.transpose(step[position[1]]))
                # print(f"{guard}\t{position}\t{separation}")
                print(separation)
                if separation<0:
                    continue
                elif separation<2:
                    loop_obstruction_flag=True
                    break
                else:
                    for i in range(separation):
                        for obstruction in obstructions:
                            if (guard+i*step[position[1]]==obstruction).all():
                                loop_obstruction_flag=True
                                break
                        if loop_obstruction_flag:
                            break
                if loop_obstruction_flag:
                    break
        
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
    # print(positions)
    # print()

# print(len(set([positions[i][0] for i in range(len(positions))])))
print()
print(loop_obstructions)