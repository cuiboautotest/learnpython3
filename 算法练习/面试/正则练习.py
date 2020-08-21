import re
'''
匹配中国
'''
str='<div class="nam">中国</div>'
res=re.findall('<div class=".*">(.*?)</div>',str)
print(res)