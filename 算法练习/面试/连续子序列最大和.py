nums=[-2,1,-3,4,-1,2,1,-5,4]
#求连续子序列和 [4,-1,2,1]
#动态规划
dp=0
res=float('-inf')#负无穷
for i in range(len(nums)):
    if dp>0:
        dp+=nums[i]
    else:
        dp=nums[i]
    res=max(res,dp)
print(res)
