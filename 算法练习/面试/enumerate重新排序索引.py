s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
L=list(s)
for i,v in enumerate(indices):
    L[v]=s[i]
print(L)
print("".join(L))