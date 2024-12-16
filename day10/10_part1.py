import re
from collections import deque

with open("10_input_example") as f:
    data=f.readlines()

trailheads={}
map_dict={}
# num_cols=len(data[0].strip()
for i in range(len(data)):
    for j,num in enumerate(data[i].strip()):
        num=int(num)
        if num==0:
            trailheads[(i,j)]=0
        else:
            map_dict[(i,j)]=num

    # for one in re.finditer(r'1',data[i].strip()):
    #     ones.append((i,one.start()))
    # input()

for x,y in trailheads:
    test_points=[(x-1,y)]
    test_points.append((x+1,y))
    test_points.append((x,y-1))
    test_points.append((x,y+1))

    print(test_points)
    for test_point in test_points:
        if test_point in map_dict:
            print(map_dict[test_point])
            del map_dict[test_point]
        
    print(map_dict)

    input()

print(trailheads)
