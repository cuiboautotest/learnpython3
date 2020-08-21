res=[]
def choushu(num):
    while num > 1 and (num % 2 == 0 or num % 3 == 0 or num % 5 == 0):
        if num % 2 == 0:
            num //= 2
        if num % 3 == 0:
            num //= 3
        if num % 5 == 0:
            num //= 5
    return num ==1

for i in range(1690*2*3*5):
    if choushu(i)==True:
        res.append(i)
        print(i)