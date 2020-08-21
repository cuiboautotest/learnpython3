S="I speak Goat Latin"
res=''
L=['a','e','i','o','u','A','E','I','O','U']
l=S.split(' ')
print(l)
for i,v in enumerate(l):
    if v[0] in L:
        res += v + 'ma' + 'a' * (i + 1) + ' '
    else:
        res+=v[1:]+v[0]+'ma'+'a'*(i+1)+' '
print(res)
