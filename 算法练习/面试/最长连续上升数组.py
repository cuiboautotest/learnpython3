nums=[1,3,5,7,9,11,2,4]

if not nums or nums == []:
    print(0)

# 元素个数>1
res = 1
max_res=1
for i in range(len(nums)-1):
    if nums[i+1]>nums[i]:
        res+=1
        if res>max_res:
            max_res=res
    else:
        res=1
print(max_res)



    
