import time
time_initial=time.time()


unsafe = 0
safe=0
line_no=0

with open("2_input") as f:
    data = f.readlines()

for line in data:
    # line_no+=1
    line = line.split()
    line = [int(line[i]) for i in range(len(line))]
    # check if ascending
    ascending=False
    descending=False
    for i in range(len(line)-1):
        
        # break if line isn't in order
        if line[i]>=line[i+1]:
            ascending=True
        if line[i]<=line[i+1]:
            descending=True
        if ascending and descending:
            # unsafe+=1
            # print(f"{line_no}\tnot sorted")            
            break

        # break if difference is 4 of higher
        difference=abs(line[i+1]-line[i])
        if difference>>2:
            # print(f"{line_no}\t{difference}\t{difference>>2}")
            # unsafe+=1
            break
    else:
        safe+=1

print(f"safe: {safe}")
# print(f"unsafe: {unsafe}")
# print(f"total: {len(data)}")
# print(f"unsafe, calc: {len(data)-unsafe}")

print(f"Execution time: {(time.time()-time_initial)*1000} ms")

