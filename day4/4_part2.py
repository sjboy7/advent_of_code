import re
import cProfile

regex_mas = r'(MAS)|(SAM)'

def main():
    with open('4_input') as f:
        data=f.readlines()


    count=0
    for i in range(len(data)-2):
        for j in range(len(data[0].strip())-2):
            # print(f"{i}\t{j}")
            string1=""
            string2=""

            for k in range(3):
                string1=string1+data[i+k][j+k]
                string2=string2+data[i+k][j+2-k]
                

                
            if(re.search(regex_mas, string1)):
                if(re.search(regex_mas, string2)):
                    count+=1

    print(count)


cProfile.run('main()')