nums = [1,1,1,1]
res=0
for i in range(len(nums)):
    for j in range(1,len(nums)):
        if nums[i]==nums[j] and i<j:
            res+=1
            print((i,j))
print(res)
