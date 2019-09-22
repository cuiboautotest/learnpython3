#coding = utf-8
if __name__ == '__main__':
    print("九九乘法口诀")
    for i in range(1,10):
        for j in range(i,10):
              print(u"%d * %d = %2d" % (i, j, i * j), end="  ")
        print("")