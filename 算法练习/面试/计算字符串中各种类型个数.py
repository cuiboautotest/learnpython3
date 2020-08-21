n1,n2,n3,n4=0,0,0,0
#s=input()
s='1qazxsw23 edcvfr45tgbn hy67uj m,ki89ol.\\/;p0-=\\]['
for i in s:
    if i.isalpha()==True:#字母
        n1+=1
    elif i.isspace()==True:
        n2+=1
    elif i.isdigit()==True:
        n3+=1
    else:
        n4+=1
print(n1,n2,n3,n4)
