str='lala,haha'
str1=str.split('h')#指定分割符
print(str1)

str2='do it now'
print(str2.split())#不指定分隔符默认使用空格

str3='hello world'
print(str3.split('o',1))#指定分隔符是o，分割一次,将第一个o分割
#['hell',' world']