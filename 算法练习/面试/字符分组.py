import itertools
S="aabcccccaaa"
for k, v in itertools.groupby(S):
    print(k,list(v))