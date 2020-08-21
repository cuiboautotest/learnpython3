nums=[0,1,0,3,12]
for i in nums:
    if i==0:
        nums.pop(nums.index(i))
        nums.append(0)
print(nums)


