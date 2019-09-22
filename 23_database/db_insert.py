#coding=utf-8
import pymysql
from datetime import datetime

def db_insert():
    #如果远程连接使用这种格式
    db=pymysql.connect(host="localhost", port=3306, user="root", password="123456", database="mysql")
    #使用cursor方法创建游标
    cursor=db.cursor()
    #时间转换为字符串
    dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(dt)#可以打印时间看下格式
    #创建sql语句,格式"insert into XX values（）    "%（）
    #如果插入新数据，直接在格式化对象里修改
    sql="""INSERT INTO employee(id,first_name,last_name,age,sex,income,create_time) VALUES ('%d','%s','%s','%s','%s','%s','%s')""" %(2,'cui','bo',30,'M',10000,dt)
    print(sql)

    try:
        cursor.execute(sql)
        #提交到数据库去执行，只有执行了commit（）方法，数据库才会修改
        db.commit()
    except Exception as e:
        print('数据库插入失败，case：%s'%e)
        #如果插入操作，则进行回滚
        db.rollback()
    finally:
        db.close()
def main():
    db_insert()

if __name__=='__main__':
    main()


'''
数据库中所有插入、删除、更新需要用到事务的2个方法，执行db.commit()，回滚db.rollback()
'''