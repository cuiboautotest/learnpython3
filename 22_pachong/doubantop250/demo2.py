#coding=utf-8
'''

用chrome打开豆瓣电影Top250页面， https://movie.douban.com/top250。如下图第一部电影，肖申克的救赎，电影名称、导演、主演、年份、评分、评价人数这些信息是我们需要的。我们用浏览器或者python向浏览器发送请求的时候，返回的是html代码，我们平时用浏览器浏览网页看到的这些图文并茂的规整的页面其实是html代码在经过浏览器渲染后的结果。所以我们需要找到要抓取信息在html代码中的位置。这就叫html解析，解析的工具有很多。比如：正则表达式、Beautifulsoup、Xpath、css等，这里采用xpath方法


用xpath查找元素就是按照路径一层层找下去，[@id="wrapper"]表示查找的标签的属性，用标签加上属性，我们可以更方便的定位，不用从头找到尾。div[1]、span[1]表示要查找的是该标签下的第1个div标签，第1个span标签。找到span标签可以用方法span[1]/text()取出其中的内容，pan[1]/@class可以取出属性值。


 电影封面的下载，只要找到图片的链接地址，就可以调用urllib库中的函数urllib.request.urlretrieve()直接下载。找到图片链接的方法和上面一样，把鼠标移动到封面上，右边就会显示链接的位置。

 每一页网址的变化规律，一页可以显示25部电影，就是说这250部电影一共有10页。观察前几页的网址很容易发现规律：就是start后面跟的参数变化，等于（页数-1）*25，而且发现后面的filter去掉也不影响。

第一页：https://movie.douban.com/top250
第二页：https://movie.douban.com/top250?start=25&filter=
第三页：https://movie.douban.com/top250?start=50&filter=


先用urllib发送请求，获得返回的源代码html。返回的html是字符串格式，需要用tree.HTML转化成xpath能处理的对象。观察html代码，每一个<li> ...</li>,标签刚好对应一部电影，所以我们先定位到每一个li标签，在对每一个li标签解析获得这个电影的各个信息。

data_title ---电影名称
data_info  ---电影信息（导演、主演、上映时间）
data_quote ---电影引言
data_score ---电影评分
data_num   ---电影评论人数
data_picurl---电影封面链接

'''
from urllib import request
from lxml import etree#html第三方库
#构造函数函数，抓取第i页信息
def crow(i):
    #构造第页的网址
    url='https://movie.douban.com/top250?start='+str(25*i)
    #发送请求，获得返回的html代码保存在html变量中
    html=request.urlopen(url).read().decode('utf-8')
    #将返回的字符串格式的html代码转换成xpath能处理的对象
    html=etree.HTML(html)
    #先定位到li标签，datas是一个包含25个li标签的list，就是包含25部电影信息的list
    datas=html.xpath('//ol[@class="grid_view"]/li')
    a=0
    for data in datas:
        data_title = data.xpath('div/div[2]/div[@class="hd"]/a/span[1]/text()')
        data_info = data.xpath('div/div[2]/div[@class="bd"]/p[1]/text()')
        data_quote = data.xpath('div/div[2]/div[@class="bd"]/p[2]/span/text()')
        data_score = data.xpath('div/div[2]/div[@class="bd"]/div/span[@class="rating_num"]/text()')
        data_num = data.xpath('div/div[2]/div[@class="bd"]/div/span[4]/text()')
        data_picurl = data.xpath('div/div[1]/a/img/@src')
        print("No: " + str(i * 25 + a + 1))
        print(data_title)
        #保存电影信息到txt文档
        with open('douban250.txt','a',encoding='utf-8')as f:
            # 封面图片保存路径和文件名
            picname = 'E:/python/python3/learnpython/22_pachong/doubantop250/top250/' + str(i * 25 + a + 1) + '.jpg'
            f.write("No: " + str(i * 25 + a + 1) + '\n')
            f.write(data_title[0] + '\n')
            f.write(str(data_info[0]).strip() + '\n')
            f.write(str(data_info[1]).strip() + '\n')
            # 因为发现有几部电影没有quote，所以这里加个判断，以免报错
            if data_quote:
                f.write(data_quote[0] + '\n')
            f.write(data_score[0] + '\n')
            f.write(data_num[0] + '\n')
            f.write('\n' * 3)
            # 下载封面图片到本地，路径为picname
            request.urlretrieve(data_picurl[0], filename=picname)
        a+=1
#总共10页，每页25，循环10次，共250条数据
for i in range(10):
    crow(i)


