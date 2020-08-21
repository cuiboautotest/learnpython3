n = 2
m = 3
indices = [[0,1],[1,1]]
#两行三列
res=0
arr = [[False] * m for _ in range(n)]
for row, col in indices:
    for j in range(m):
        arr[row][j] = not arr[row][j]
    for i in range(n):
        arr[i][col] = not arr[i][col]
# 遍历矩阵，数True的个数
for row in arr:
    for i in row:
        if i:
            res += 1
print(res)



