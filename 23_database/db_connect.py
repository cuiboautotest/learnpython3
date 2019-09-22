#coding=utf-8

import pymysql

def db_connect():
    #连接数据库，用户名root 密码123456 数据库名mysql
    db=pymysql.connect("localhost","root","123456","mysql")
    #使用cursor()方法创建一个游标对象cursor
    cursor=db.cursor()
    #定义查询语句
    sql_query="select * from user"
    #执行sql语句
    cursor.execute(sql_query)
    #获取单条记录
    result=cursor.fetchone()
    print(result)
    #关闭数据库连接
    db.close()

def main():
    db_connect()

if __name__=='__main__':
    main()
