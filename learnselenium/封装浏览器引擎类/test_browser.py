from browser_engine import *

class TestBrowserEngine(object):

    def open_browser(self):
        browserengine=BrowserEngine(self)
        driver=browserengine.start_browser()

test=TestBrowserEngine()
test.open_browser()