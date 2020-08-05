import xlrd
"""
验证登录，正常登录，密码错误，用户名不正确
读取Excel文件
先创建一个文件123.xlsx
"""
def get_excel_row(row):
    excel = xlrd.open_workbook('../test_data/123.xlsx')   #打开文件需要使用相对路径（。。/表示上一级）
    table = excel.sheets()[0]   #表示第一张表格
    # print(table.row_values(0))  #打印第一行数据
    # print(table.col_values(0))  #打印第一列的信息
    for i in range(1,table.nrows):  #遍历数据文件的n行
        print(table.cell_value(row,1),table.cell_value(row,2))