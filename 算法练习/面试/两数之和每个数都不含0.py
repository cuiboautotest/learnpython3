n=1010
i=1
while i<n:
    j=n-i
    if '0' not in str(j) and '0' not in str(i):
        print([i,j])
        break
    else:
        i+=1
