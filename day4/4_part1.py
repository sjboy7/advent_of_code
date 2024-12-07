import re
import cProfile

regex_xmas = r'(XMAS)|(SAMX)'

with open('4_input') as f:
    data=f.readlines()


# def check_match(test_string):
#     if(re.search(regex_xmas, test_string)):
        # print(test_string)
        # count+=1


# print(data[0])
count=0
for i in range(len(data)):
    for j in range(len(data[0])):
        
        # left right
        try:
            test_string=data[i][j:j+4]
            if(re.search(regex_xmas, test_string)):
                count+=1
        except:
            pass

        # up down
        try:
            test_string=""
            for k in range(4):
                test_string=test_string + data[i+k][j]

            if(re.search(regex_xmas, test_string)):
                count+=1
        except:
            pass

        try:
            # down right
            test_string=""
            for k in range(4):
                test_string=test_string + data[i+k][j+k]
            
            if(re.search(regex_xmas, test_string)):
                count+=1
        except:
            pass

        try:
            # down left
            test_string=""
            for k in range(4):
                test_string=test_string + data[i+k][j-k]

            if(re.search(regex_xmas, test_string)):
                count+=1
        except:
            pass

print(count)
