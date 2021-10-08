#导入模块
import xlrd

#打开Excel文件读取内容
data = xlrd.open_workbook(r"F:/文档/练习文件夹/练习表格.xls")
# #或者通过名称获取
# table = data.sheet_by_name()
#通过索引顺序获取
# table = data.sheets()[0]

#通过索引顺序获取
table = data.sheet_by_index(0)
#获取单个表格值  （2,1）表示获取第3行第2列的值
value = table.cell_value(2,1)
print('第三行第二列的值为',value)


#获取表格行数
nrows = table.nrows
print('表格一共有',nrows,'行')
# row = table.row()
# print('表格一共有',row,'列')
nrows_list = [str(table.cell_value(i,3)) for i in range(0,nrows)]
print('第四列的所有值为',nrows_list)




