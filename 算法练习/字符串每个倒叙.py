s="Let's take LeetCode contest"
s1=s.split(' ')
#print(s1)
L=[]
for i in s1:
    L.append(i[::-1])
#print(L)
print(' '.join(L))
