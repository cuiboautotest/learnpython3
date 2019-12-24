
import xlrd
def read_excel(filename,index):
    xls=xlrd.open_workbook(filename)
    sheet=xls.sheet_by_index(index)
    print(sheet.ncols)#输出列数
    print(sheet.nrows)#输出行数，2列3行，列索引从0开始
    dic={}
    for j in range(sheet.ncols):
        data=[]
        for i in range(sheet.nrows):
            data.append(sheet.row_values(i)[j])
            dic[j]=data
    #print(dic)
    return dic

print (read_excel('./testdata.xlsx',0))
