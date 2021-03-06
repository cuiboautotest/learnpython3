#整数输出
"""
格式化符号格式说明备注 %o 八进制 oct%d 十进制 dec%x 十六进制 hex
"""
print('%o' % 20) # 八进制24
print('%d' % 20) # 十进制24
print('%x' % 24) # 十六进制18

#浮点数输出
"""
 %f 保留小数点后面六位有效数字 float
 %e 保留小数点后面六位有效数字 
 %g 在保证六位有效数字的前提下，使用小数方式，否则使用科学计数法
"""
print('%f' % 1.11)         # 默认保留6位小数1.110000
print('%.1f' % 1.11)       # 取1位小数1.1
print('%e' % 1.11)         # 默认6位小数，用科学计数法1.110000e+00
print('%.3e' % 1.11)       # 取3位小数，用科学计数法1.110e+00
print('%g' % 1111.1111)    # 默认6位有效数字1111.11
print('%.7g' % 1111.1111)  # 取7位有效数字1111.111
print('%.2g' % 1111.1111)  # 取2位有效数字，自动转换为科学计数法1.1e+03

#字符串输出
"""
格式化符号说明备注 %s 字符串输出 string%10s 右对齐，占位符 10位%-10s 左对齐，占位符 10 位 %.2s 截取 2 位字符串 %10.2s10 位占位符，截取两位字符串。
"""
print('%s' % 'hello world')       # 字符串输出hello world
print('%20s' % 'hello world')     # 右对齐，取20位，不够则补位         hello world
print('%-20s' % 'hello world')    # 左对齐，取20位，不够则补位hello world
print('%.2s' % 'hello world')     # 取2位he
print('%10.2s' % 'hello world')   # 右对齐，取2位        he
print('%-10.2s' % 'hello world')  # 左对齐，取2位he