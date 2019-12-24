#列表推导式
list=[x *10 for x in range(0,21) if x %2 ==0]
print(list)

list1=[x * 10 if x%2==0 else x *100 for x in range(0,21)]
print(list1)