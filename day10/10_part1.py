import re
from collections import deque

# dict_test={}
# dict_test[0]=5
# dict_test[1]=3
# print(dict_test[1])

# a=(1,0)
# b=(2,1)
# print(a[0])
# exit()


trailheads={}
unchecked={}
existing_paths=[]
dead_ends=[]
map_all={}


def check_step(node, trailhead):
    # input(f"check_step\t{node}\t{trailhead}")
    print(f"check_step\t{node}\t{trailhead}")
    # input()
    if node in existing_paths:
        trailheads[trailhead]+=1
        print("\texisting path")
        return 1 # End recursion
    elif node in dead_ends:
        print("\tdead end")
        return 0 # End recursion
    else:
        next_val=map_all[node]+1

        test_points=[(node[0]-1,node[1])]
        test_points.append((node[0]+1,node[1]))
        test_points.append((node[0],node[1]-1))
        test_points.append((node[0],node[1]+1))
        
        path_good=False
        
        for test_point in test_points:
            if on_the_map(test_point):
                if map_all[test_point]==next_val:
                    if check_step(test_point,trailhead):
                        existing_paths.append(node)
                        path_good=True
                    else:
                        dead_ends.append(node)
    if path_good:
        return 1
    else:
        return 0

def on_the_map(node):
    max_x=len(data[0].strip())-1
    max_y=len(data)-1
    if ((node[0]<0) or (node[0]>max_x) or (node[1]<0)  or (node[1]>max_y)):
        return 0
    else:
        return 1
    
with open("10_input_example") as f:
    data=f.readlines()


# num_cols=len(data[0].strip()
for j in range(len(data)):
    for i,num in enumerate(data[j].strip()):
        num=int(num)
        if num==0:
            trailheads[(i,j)]=0
        elif num==9:
            existing_paths.append((i,j))
        else:
            unchecked[(i,j)]=num
        map_all[(i,j)]=num

    # for one in re.finditer(r'1',data[i].strip()):
    #     ones.append((i,one.start()))
    # input()



     
sum=0
for trailhead in trailheads:
    check_step(trailhead, trailhead)

print("done")
# for x,y in trailheads:
#     test_points=[(x-1,y)]
#     test_points.append((x+1,y))
#     test_points.append((x,y-1))
#     test_points.append((x,y+1))

#     print(test_points)
#     for test_point in test_points:
#         if test_point in map_dict:
#             print(map_dict[test_point])
#             del map_dict[test_point]
        
#     print(map_dict)

#     input()

# print(trailheads)