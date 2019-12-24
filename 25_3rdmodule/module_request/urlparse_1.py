from urllib import request, parse #解析url

print(parse.urlparse('https://movie.douban.com/'))
print(parse.urlparse('https://movie.douban.com/', scheme='http'))
print(parse.urlparse('movie.douban.com/', scheme='http'))
