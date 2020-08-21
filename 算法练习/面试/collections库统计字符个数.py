from collections import Counter
s="adsadasmdlajdlasdkladsjakld,asda1errew"
res=Counter(s)
print(res)
k=res.most_common(3)#取排名前3位
print(k)