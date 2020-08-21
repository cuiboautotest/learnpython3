def solution(target):
    #滑动窗口方法解决
    #左右边界
    i,j=1,1
    sum=0
    res=[]
    while i<=target//2:
        #窗口和小，右边界向右移动扩大窗口
        if sum<target:
            sum+=j
            j+=1
        #窗口和大，左边界向右移动缩小窗口
        elif sum>target:
            sum-=i
            i+=1
        #相等，开始记录结果，并寻找下一个窗口
        else:
            arr=list(range(i,j))
            res.append(arr)
            #继续寻找下一个窗口
            sum-=i
            i+=1
    return res
print(solution(9))