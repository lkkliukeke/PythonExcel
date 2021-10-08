import xlwt


#第一步：创建表格，并写入内容
# #创建表格并导入内容
# def testwt():
#     #创建一个新的workbook（创建新的Excel表格）
#     workbook = xlwt.Workbook(encoding= 'ascii')
#     #创建新的sheet表格
#     worksheet = workbook.add_sheet("my new sheet")
#     #往表格中写内容
#     worksheet.write(0,0,"内容1")
#     worksheet.write(2,1,"内容2")
#     #保存表格
#     # workbook.save("test.xlsx")
#     workbook.save("F:/文档/练习文件夹/新建表格.xlsx")
# testwt()
# print('ok')




#第二步：设置字体格式
#创建表格并导入内容
def testwt():
    #创建一个新的workbook（创建新的Excel表格）
    workbook = xlwt.Workbook(encoding= 'ascii')
    #创建新的sheet表格
    worksheet = workbook.add_sheet("my new sheet")

    #初始化样式
    style = xlwt.XFStyle()
    #为样式创建字体
    font = xlwt.Font()
    font.name = 'Times New Roman'   #字体
    font.bold = True                #加粗
    font.underline = True           #下划线
    font.italic = True              #斜体
    #设置样式
    style.font = font

    #往表格中写内容
    worksheet.write(0,0,"内容1")
    worksheet.write(2,1,"内容2",style)
    #保存表格
    # workbook.save("test.xlsx")
    workbook.save("F:/文档/练习文件夹/新建表格.xlsx")
testwt()
print('ok')