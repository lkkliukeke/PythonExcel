import pandas as pd
from pandas import DataFrame

#使用pandas读写Excel
def testpandas():
    #读取Excel表格
    data = pd.read_excel(r"F:\文档\练习文件夹\练习表格.xls", sheet_name='Sheet1')
    print(data)

    #增加行数据，在第6行
    data.loc[5] = ['5','join','pandas']
    #增加列数据，给定默认值none
    data['new_col'] = None
    #保存数据
    DataFrame(data).to_excel('F:/文档/练习文件夹/新文件夹.xls',sheet_name='Sheet1',index=False,header=True)

if __name__ == '__main__':
    testpandas()