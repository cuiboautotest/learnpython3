s=[]
s.append('a')#空列表新增元素，加到最后一个，每次只能加一个
print(s)

L=[]
for i in range(10):
    L.append(i)
    if i<10:
        print(L)
    else:
        print('超出范围')



