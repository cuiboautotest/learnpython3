#coding =utf-8
import requests
import urllib
import unittest
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
        print('executing testcase test_search_tags_movie...')
        return resp

    def test_search_tags_hot(self):
        method = 'search_tags'
        url = 'https://%s/j/%s' % (self.host, method)
        post_data = {
            'type': 'movie',
            'tag': urllib.parse.quote('热门')
        }
        resp = self.get_response(url=url, data=post_data)
        print('executing testcase test_search_tags_hot...')
        return resp

    def test_search_tags_tv(self):
        method = 'search_tags'
        url = 'https://%s/j/%s' % (self.host, method)
        post_data = {
            'type': 'tv',
            'source': 'index'
        }
        resp = self.get_response(url=url, data=post_data)
        print('executing testcase test_search_tags_tv...')
        return resp


class Douban_Testcase(unittest.TestCase):
    """A class for setting up test and collecting test cases"""

    @classmethod
    def setUpClass(cls):
        cls.douban_obj = Douban()

    def setUp(self):
        print('...creating test...')

    def tearDown(self):
        print('...closing test...')

    def test_001(self):
        ret = self.douban_obj.test_search_tags_movie()
        self.assertTrue(ret)

    def test_002(self):
        ret = self.douban_obj.test_search_tags_hot()
        self.assertTrue(ret)

    def test_003(self):
        ret = self.douban_obj.test_search_tags_tv()
        self.assertTrue(ret)


if __name__ == '__main__':
    unittest.main()

