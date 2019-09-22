import pymysql
import datetime
def db_update():
    db=pymysql.connect(host='localhost',user='root',password='123456',port=3306,database='mysql')
    print('数据库连接成功')
    cursor=db.cursor()
    sql="update EMPLOYEE set age = age+1 where sex='%s'"% 'M'
    try:
        cursor.execute(sql)
        db.commit()
        print("修改成功！")
    except Exception as e:
        print("修改失败！:case:%s"%e)
        db.rollback()
    finally:
        db.close()

def main():
    db_update()

if __name__=='__main__':
    main()