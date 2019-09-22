# python 冒泡排序
"""
解析：很经典的排序方式，从数组中的第0个元素开始，与后面一个元素进行比较，
如果前面的元素大于后面的元素，就调换位置，循环到最后
（即：a0与a1比较得到结果后，a1与a2比较...），
最大的元素被换到数组最末尾，剔除掉最后一个元素，在余下的数组元素中进行上述操作，
到最后，整个数组呈现从小到大的排序
取第i元素和第i+1个元素做比较，假如第i+1个元素大于第i个元素，则交换两个元素。一直到待排序的集合是有序的为止。假设待排序的元素集合： 5 4  3 1 。

第一次冒泡后的序列：4 3 1 5
第二次冒泡的序列：3  1 4 5
第三次冒泡后的序列：1 3 4 5
N元素序列一共需要比较N-1轮。第i个元素需要比较N-i-1次。需要两层循环实现。
"""


def paixu(li):
    max = 0
    for ad in range(len(li) - 1):
        for x in range(len(li) - 1 - ad):
            if li[x] > li[x + 1]:
                max = li[x]
                li[x] = li[x + 1]
                li[x + 1] = max
            else:
                max = li[x + 1]
    print(li)


paixu([41, 23344, 9353, 5554, 44, 7557, 6434, 500, 2000])

"""
#!coding:utf-8
#冒泡排序
#输入：待排序的元素集合
#输出：已排序元素集合
def bubble_sort(lst):
    lst_len=len(lst)
    #控制循环次数，N个元素需要N轮比较
    for i in  range(lst_len-1):
        #第n个元素需要比较(N-n-1)次
        for j in  range(lst_len-i-1):
            if lst[j]>lst[j+1]:
                #如果第j个元素大于j+1,则交换
                lst[j],lst[j+1]=lst[j+1],lst[j]
    return lst

if __name__ == "__main__":
    a=bubble_sort([1,3,8,6,7,0])
    print(a)
"""
