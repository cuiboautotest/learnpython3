#单个字符串分割
s='abcABCdef'
b=s.split('/')#切分成列表，“/”在字符串中不存在直接分割成整的字符串
print(b)

#只有字符串分割
s1='a,b,c'
res=s1.split(',')
print(res)
print(type(s1))



#分割取值
s='cuibo,cuibo2,cuibo3'
r=s.split(',')[0]
print(r)