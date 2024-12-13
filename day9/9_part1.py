with open('9_input_example') as f:
    data = f.readlines()[0].strip()

blocks = ""
for index, num in enumerate(data):
    
    if (index & 1):
        blocks = blocks + int(num)*'.'

    else:
        blocks = blocks + int(num)*str(index>>1)


print(blocks)