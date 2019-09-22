import xlrd
import os
class ExcelUtil(object):
    def __init__(self,excelpath,sheetname='Sheet1'):#注意是两个下滑线，且init不要写成int
        self.data=xlrd.open_workbook(excelpath)
        self.table=self.data.sheet_by_name(sheetname)
        #获取第一行作为key
        self.keys=self.table.row_values(0)
        #获取总行数
        self.rowNum=self.table.nrows
        #获取总列数
        self.colNum=self.table.ncols

    def dict_data(self):
        if self.rowNum<=1:
            print('总行数小于1')
        else:
            r=[]
            j=1
            for i in range(self.rowNum-1):
                s={}
                #从第二行取对应的value
                values=self.table.row_values(j)
                for x in range(self.colNum):
                    s[self.keys[x]]=values[x]
                r.append(s)
                j+=1
            return r

if __name__=='__main__':
    filepath="E:\\python\\python3\\learnpython\\21_opcsv\demo_1\\datas.xlsx"
    data=ExcelUtil(filepath)
    print(data.dict_data())

'''
如果报错take no arguments
这里的   __init__下划线是左右两边各两个，不是一个
看是不是把__init__写成了__int__
'''


