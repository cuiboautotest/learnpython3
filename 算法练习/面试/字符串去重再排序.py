s='ajldjlajfdljfddd'
#字符串转集合
s=set(s)
#print(s)
#集合转列表再排序
s=list(s)
s.sort(reverse=False)
print(s)
res="".join(s)
print(res)
