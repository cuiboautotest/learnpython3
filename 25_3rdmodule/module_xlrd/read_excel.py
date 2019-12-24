import xlrd
xls=xlrd.open_workbook('./test.xlsx')
sheet=xls.sheet_by_index(0)#通过索引方式0代表第一个sheet
sheet=xls.sheet_by_name('Sheet1')
print(sheet.nrows)#打印表格总行数
print(sheet.ncols)#打印表格总列数
print(sheet.row_values(1)[0])#打印表格第2行，第一列单元值