#coding=utf-8

import pymysql

def db_create():
    #连接数据库，用户名root 密码123456 数据库名mysql
    db=pymysql.connect("localhost","root","123456","mysql")
    print("数据库连接成功")
    #使用cursor()方法创建一个游标对象cursor
    cursor=db.cursor()
    #执行sql语句,如果EMPLOYEE表存在就删除
    cursor.execute("drop table if exists EMPLOYEE")#不区分大小写，数据库中都是小写
    '''
    第一次执行上述会报错，第二次就正常了
    由于刚开始的时候 TESTDB 数据库中没有 EMPLOYEE 表，所以程序在执行cursor.execute("DROP   TABLE IF EXISTS EMPLOYEE")语句的时候报了如下提醒信息：
    Warning: (1051, "Unknown table 'mysql.employee'")
  result = self._query(query)
    '''
    #使用预处理语句创建表,存在多行用三引号
    sql="""create table EMPLOYEE(
        id int(8) not null primary key auto_increment,
        first_name char(20) not null,
        last_name char(20) not null,
        age int,
        sex char(1),
        income float,
        create_time datetime
    )"""
    try:
        cursor.execute(sql)
        print('create table sucess!')
    #exception是所有错误类，也可以用指定错误类
    except Exception as e:
        print('create table failed,case:%s'%e)
    finally:
        #关闭数据库连接
        db.close()

def main():
    db_create()

if __name__=='__main__':
    main()
