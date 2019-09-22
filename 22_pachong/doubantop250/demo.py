import requests
import re
#'url=https://movie.douban.com/top250?start=25&filter='  start代表第一页展示25条数据
class MovieTop(object):
    def __int__(self):
        self.start=0
        self.param='&filter='
        self.header={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

    def get_page(self):
        page_content=[]
        try:
            while self.start<=225:
                url='https://movie.douban.com/top250?start='+str(self.start)
                req=requests.Request(url,headers=self.header)
                response=request.urlopen(req)
                page=response.read.decode('urf-8')
                page_num=(self.start+25)//25
                print("正在抓取第+str(page_num)+页数据...")
                self.start+=25
                page_content.append(page)
            return page_content
        except requests.URLErro as e:
            if hasattr(e,'reason'):
                print('抓取失败，失败原因：',e.reason)

def get_movie_info(self):
    pattern=re.compile(u'<div.*?class="item">.*?'+
u'')

def main(self):
    print('开始从豆瓣电影抓取数据...')
    self.get_page()
    print('抓取完毕')

#if __name__=='__main__':
#    main(self=self)
