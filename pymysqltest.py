
import MySQLdb

#打开数据库
db = MySQLdb.connect("localhost","root","admin123","test")

#使用cursor()方法获取操作游标
cursor = db.cursor()

#使用execute方法执行SQL语句
cursor.execute("select version()")

#使用fetchone() 方法获取单条数据
data = cursor.fetchone()

print("Database version : %s " % data)

#关闭数据库
db.close()