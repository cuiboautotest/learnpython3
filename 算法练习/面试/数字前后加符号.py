s='Jkdi234klowe90a3'
s1=''
for i in s:
    if i.isdigit():
        s1+='*'+ i +'*'
    else:
        s1+=i
print(s1)
s2=s1.replace('**','')
print(s2)


