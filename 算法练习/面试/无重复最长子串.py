s="abcabcbb"
max_len=0
cur_len=0
window=[]
n=len(s)
for i in range(n):
    val=s[i]
    if val not in window:
        window.append(val)
        cur_len+=1
    else:
        idx=window.index(val)
        window=window[idx+1:]
        window.append(val)
        cur_len=len(window)
    if cur_len>max_len:max_len=cur_len
print(max_len)
