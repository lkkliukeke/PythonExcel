import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="admin123",
    database = 'runoob'
)
#创建一个游标对象
curr = mydb.cursor()
#创建数据库
# curr.execute("create database runoob")
#创建数据表
# curr.execute("create table site(name varchar(200),url varchar(200))")
#添加主键
# curr.execute("alter table site add column id int auto_increment primary key ")
#给表创建主键
# curr.execute("create table site(id int auto_increment primary key ,name varchar(200),url varchar(200))")
#给表插入数据
sql = "insert into site(name, url) values ('9999','www.999.com')"
curr.execute(sql)
mydb.commit()             #将sql语句提交到数据库内
print('成功')

#批量插入
# sql = "insert into site(name, url) values (%s,%s)"
# val = [
#     ('google','https"//www.google.com'),
#     ('baidu','https"//www.baidu.com'),
#     ('taobao','https"//www.taobao.com')
# ]
# curr.executemany(sql,val)
#mydb.commit()

#获取添加的id
# sql = "insert into site(name, url) values (%s,%s)"
# var = ('test','https://www.test.com')
# curr.execute(sql,var)
# mydb.commit()   #表格更新内容，必须使用该语句
# print('成功1,id为：',curr.lastrowid)

# #指定读取字段数据         fetchall()返回的是多个元组，即多条记录
# curr.execute("select name, url from site")
# sit = curr.fetchall()
# for x in sit:
#     print(x)

#读取一条数据           fetchone()返回的是单个元组，即一条记录
# curr.execute("select * from site")
# sit = curr.fetchone()
# print(sit)

#读取指定的数据
# curr.execute("select * from site where name = 'taobao'")
# sit = curr.fetchall()
# print(sit)

#使用通配符
# curr.execute("select * from site where name like '%ao%'")
# stre = curr.fetchall()
# print(stre)

#使用占位符
# sql = "select * from site where name =%s"
# na = ("baidu",)
# curr.execute(sql,na)
# ste = curr.fetchall()
# for m in ste:
#     print(m)

#查询结果排序 order by 升序asc  降序desc
# curr.execute("select * from site order by name")      #升序
# curr.execute("select * from site order by name desc")    #降序
# ste = curr.fetchall()
# print(ste)

#使用limit来指定
# curr.execute("select * from site limit 3")
# ste = curr.fetchall()
# print(ste)

#删除记录
# sql = "delete from site where name = '123'"
# curr.execute(sql)
# mydb.commit()
# print('删除成功')

#更新表
# sql = "UPDATE site set name = 'test123' where name='test'"
# curr.execute(sql)
# mydb.commit()
# print('chenggong')

#使用占位符更新表
# sql = "update site set name=%s where name=%s"
# val = ('test456','test123')
# curr.execute(sql,val)
# mydb.commit()
# print('成功')

#删除表
# sql = "drop table if exists site"
# curr.execute(sql)