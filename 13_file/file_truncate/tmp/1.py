import os
import time


class deletefunc(object):
    def __init__(self):
        pass

    def cleartext(self):

        with open('filename','r+') as f2:
            res=f2.readlines()
            print(res)
            f2.seek(0,0)
            f2.truncate()

if __name__ == "__main__":

    test = deletefunc()
    test.deletetype()
