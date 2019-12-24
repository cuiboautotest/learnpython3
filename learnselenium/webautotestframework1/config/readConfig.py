import os
import configparser


config=configparser.ConfigParser()
config.read()
class ReadConfig(object):

    def get_http(self,name):
        value=config.get('http',name)
        return value

    def get_email(self,name):
        value=config.get('EMAIL',name)
        return value

    def get_sql(self,name):
        value=config.get('DATABASE',name)
        return value

    def get_cmd(self,name):
        value=config.get
