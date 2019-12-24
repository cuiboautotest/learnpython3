from collections import Counter
words=['a','b','c','a','d','e','a','b','e']
count_words=Counter(words)
top_three=count_words.most_common(3)
print(top_three)#[('a', 3), ('b', 2), ('e', 2)]