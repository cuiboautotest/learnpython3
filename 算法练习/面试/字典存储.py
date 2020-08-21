nums = [555,901,482,1771,1771]
dic={}
for i in nums:
    dic[i]=len(str(i))
print(dic)
#如果有重复数组元素，则字典统计会减少元素个数，因为相同key-value进行了去重