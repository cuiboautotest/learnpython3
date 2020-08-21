text = "loonbalxballpoonno"
'''
计算能成为目标字符串的次数
'''
from collections import Counter
text_count=Counter(text)
#print(text_count)
s='ballon'
balloon_text={'b':1,'a':1,'l':2,'o':2,'n':1}
res=[]
for key in balloon_text:
    if key in text_count:
        res.append(int(text_count[key]/balloon_text[key]))
    else:
        continue
print(min(res))

















