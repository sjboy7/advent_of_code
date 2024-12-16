F,S,p=[],[],0
for i, c in enumerate(open('9_input').read().strip()):
    [F,S][i%2] += [[*range(p,p:=p+int(c))]]
for y in reversed(range(len(F))):
    for x in range(len(S)):
        if len(S[x]) >= len(F[y]) and F[y][0] > S[x][0]:
            F[y] = S[x][:len(F[y])]
            S[x] = S[x][len(F[y]):]
print(sum((i*j) for i,f in enumerate(F) for j in f))