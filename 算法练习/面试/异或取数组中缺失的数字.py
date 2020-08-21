res=0
nums=[3,0,1]
for i in nums:
    res^=i
for i in range(len(nums)+1):
    res^=i
print(res)