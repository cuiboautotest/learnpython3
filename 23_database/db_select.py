#coding
import pymysql

def db_select():
    #如果远程连接使用这种格式
    db=pymysql.connect(host="localhost", port=3306, user="root", password="123456", database="mysql")
    #使用cursor方法创建游标
    cursor=db.cursor()

    #创建sql语句
    sql="select * from employee where income>%d"%10000
    try:
        cursor.execute(sql)
        #获取所有记录列表,fetchone()获取单条记录，fetchall()获取所有
        results=cursor.fetchall()
        for row in results:
            fname=row[0]
            lname=row[1]
            age=row[2]
            sex=row[3]
            income=row[4]
            create_time=row[5]
            #输出结果
            print("first_name=%s,last_name=%s,age=%s,sex=%s,income=%d,create_time=%s"%(first_name,last_name,age,sex,income,create_time))
    except Exception as e:
        print('数据库插入失败，case：%s'%e)
        #如果插入操作，则进行回滚
        db.rollback()
    finally:
        db.close()
def main():
    db_select()

if __name__=='__main__':
    main()