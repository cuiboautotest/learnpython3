"""
实现需求：
1.Python模拟HTTP接口请求
2.通过修改post参数验证参数合法性
"""
import requests
import sys, io
# 解决console显示乱码的编码问题
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

url = 'https://movie.douban.com/j/search_tags'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
'Referer':'https://movie.douban.com/',
}
# 修改'type'，'source'参数值验证参数合法性
post_data = {
	'type':'movie',
	'source':'index'
}

response = requests.post(url=url, data=post_data, headers=headers).content.decode('utf-8')
print('result:\n', response)

