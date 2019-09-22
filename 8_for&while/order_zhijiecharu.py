#coding:utf-8
"""
算法思想:

把待排序的元素插入已经排序的序列中。取第一个元素为有序序列。从剩下的元素中依次取值和相邻的元素作比较，找到合适的位置并插入。直至所有待排序的元素为有序序列。


"""
def inert_sort(lst):
    for i in range(1,len(lst)):
        if lst[i-1]>lst[i]:
            tmp=lst[i]
            seq=i
            while seq>0 and  lst[seq-1]>tmp:
                lst[seq]=lst[seq-1]
                seq-=1
            lst[seq]=tmp
    return lst

if __name__ == "__main__":
    a=inert_sort([1,5,7,6,2,0])
    print(a)