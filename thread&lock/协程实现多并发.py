from gevent import monkey

monkey.patch_all()
import requests
import gevent
import sys, io

# 解决console显示乱码的编码问题
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


class Douban(object):
    """A class containing interface test method of Douban object"""

    def __init__(self):
        self.host = 'movie.douban.com'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
                        'Referer': 'https://movie.douban.com/',
                        }

    def get_response(self, url, data):
        resp = requests.post(url=url, data=data, headers=self.headers).content.decode('utf-8')
        return resp

    def test_search_tags_movie(self):
        method = 'search_tags'
        url = 'https://%s/j/%s' % (self.host, method)
        post_data = {
            'type': 'movie',
            'source': 'index'
        }
        resp = self.get_response(url=url, data=post_data)
        print(resp)
        return resp


if __name__ == '__main__':
    douban = Douban()
    threads = []
    for i in range(6):
        thread = gevent.spawn(douban.test_search_tags_movie)
        threads.append(thread)

    gevent.joinall(threads)
