nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
i=2
while i<len(nums):
    if nums[i-2]==nums[i]:
        #弹出重复项
        nums.pop(i)
    else:
        i+=1
print(nums)