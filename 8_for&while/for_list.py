#for循环列表
languages = ["c++","python","java","php","c"]
for language in languages:
   print(language,end=",")#打印一整行，并用，结尾

#range()和len()函数遍历列表索引

print("\n")

for i in range(len(languages)):
    print(i,languages[i])

