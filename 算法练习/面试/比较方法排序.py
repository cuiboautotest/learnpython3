import functools
def tcmp(a, b):
    if a > b:
        return -1
    elif a < b:
        return 1
    else:
        return 0

nums = [1, 2, 5, 4]
#functools.cmp_to_key只能传值1，-1，0
sorted_nums = sorted(nums, key=functools.cmp_to_key(tcmp))
print(sorted_nums)