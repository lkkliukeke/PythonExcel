import MySQLdb
import mysql.connector

#打开数据库
db = MySQLdb.connect('localhost','root','admin123',"test")
crr = db.cursor()
sql = """insert into tests(name, age, sex) values ('张三3',17,'女')"""
# print(sql)
try:
    crr.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()

#创建一个游标对象
# cur = db.cursor()

#使用execute()方法执行sql，如果表存在则删除
# cur .execute("drop tests if exists name")

#添加
# sql = """insert into tests(name,age,sex) VALUES('张三2','12','男')"""
# print('success')
#添加表
# sql = """create table test2(
# name varchar (20),
# age varchar (20),
# sex varchar (10)
# )"""

#sql查询
# sql = """select * from test where name='张三'"""

# try:
#     print('1')
#     cur.execute(sql)
#     db.commit()
#     print('1')
# except:
#     db.rollback()

#使用预处理语句创建表
# sql = """CREATE TABLE TEST1 (
#          FIRST_NAME  CHAR(20) NOT NULL,
#          LAST_NAME  CHAR(20),
#          AGE INT,
#          SEX CHAR(1),
#          INCOME FLOAT )"""

# cur.execute(sql)
# print('2')
# db.close()