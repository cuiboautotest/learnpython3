class Solution:
    def Find(self, target, array):
        if not array:
            return False
        row = len(array)                # 数组的行数
        col = len(array[0])             # 数组的列数
        i,j = row - 1,0          # i, j这样规定是从左下开始查找，也可以从右上
        while i >= 0 and j < col:       # 双指针来判断是否在array中
            if array[i][j] == target:
                return True             # 如果等于输出True
            elif array[i][j] > target:
                i -= 1                  # 如果大于则往上移一格
            else:
                j += 1                  # 如果小于则往右移一格
        return False                    #如果最后走到了边界仍没有，则输出False
