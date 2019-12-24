#coding=utf-8
from datetime import datetime,date,timedelta
import time
from selenium import webdriver
import xlrd
import logging

driver=webdriver.Chrome()

#返回driver对象
def return_driver():
    return driver

#url
def open_base_site(url):
    driver.get(url)

#定义明天
def date_n(n):
    return str((date.today()+timedelta(days=+int(n))).strftime("%Y-%m-%d"))


def id(element):
    return driver.find_element_by_id(element)

def css(element):
    return driver.find_element_by_css_selector(element)

def xpath(element):
    return driver.find_element_by_xpath(element)

def js(element):
    driver.execute_script("document.getElementById("+"'" + element+"'"+").removeAttribute('readonly')")

def read_excel(filename,index):
    xls=xlrd.open_workbook(filename)
    sheet=xls.sheet_by_index(index)
    #print(sheet.nrows)
    #print(sheet.ncols)
    dic={}
    for j in range(sheet.ncols):
        data=[]
        for i in range(sheet.nrows):
            data.append(sheet.row_values(i)[j])#第1行第0列
        dic[j]=data
    return dic

def log(str):
    logging.basicConfig(level=logging.info,format='%(asctime)s %(filename)s %(levelname)s %(message)s',datafmt='%a,%d %b %Y %H:%M:%S',filename='log-selenium.log',filemode='a')
    console=logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter=logging.Formatter('%(name)-12s:%(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
    logging.info(str)

