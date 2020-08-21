n=28
res = ""
while n:
    n -= 1
    n, y = divmod(n, 26)
    res = chr(y + 65) + res
print(res)