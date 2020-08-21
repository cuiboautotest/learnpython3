nums=[1,2,3]
dic={}
for i in nums:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
#print(dic)
du=max(dic.values())
#print(du)
L=[]
for k,v in dic.items():
    if dic[k]==du:
        start=nums.index(k)
        end=len(nums)-nums[::-1].index(k)
        L.append(len(nums[start:end]))
    else:
        continue
print(min(L))
