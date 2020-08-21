nums = [6]
nums.sort(reverse=True)
print(nums)
i=0
while i<len(nums):
    if sum(nums[0:i+1])<=sum(nums[i+1:]):
        i+=1
    else:
        print(nums[0:i+1])
        break
