# import time
import cProfile


def check_safe(line):
    ascending=False
    descending=False
    # print(line)
    for i in range(len(line)-1):
    
        # break if line isn't in order
        if line[i]>=line[i+1]:
            ascending=True
        if line[i]<=line[i+1]:
            descending=True
        if ascending and descending:
            return i

        # break if difference is 4 of higher
        difference=abs(line[i+1]-line[i])
        if difference>>2:
            return i
    return -1

def main():
    # time_initial=time.time()
    safe=0

    with open("2_input") as f:
        data = f.readlines()
        
    
    for line in data:
        # line=line.split()
        # line = [int(line[i]) for i in range(len(line))]
        line = list(map(int, line.split()))
        
        fail_index = check_safe(line)
        if fail_index>=0:
            # print(line)
            for i in range(fail_index,len(line)):     
                # line_mod = [line[j] for j in range(len(line)) if not(j == i)]
                # line_mod = line[:i] + line[i+1:]
                line_mod = line[:i] + line[i+1:]
                # print(line_mod)
                if check_safe(line_mod)<0:
                    safe+=1
                    # print(line_mod)
                    break
            # print()
        else:
            safe+=1

        
    # execution_time = (time.time()-time_initial)*1000
    # print(f"Execution time: {execution_time} ms")
    print(f"safe: {safe}")

    

cProfile.run('main()')

# if __name__ == "__main__":
#     main()

