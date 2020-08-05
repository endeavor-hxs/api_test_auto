import pytest


if __name__ == '__main__':
    pytest.main(['../test_case/test_case_01.py','--html=../test_report/report.html'])#生成html格式报告
    #前面一段是说，执行test-case下的test_case_01测试用例

    # pytest.main(['../test_case/','--junitxml=../test_report/report.xml'])#生成xml格式的报告
    #执行test_case下的所有用例

    # pytest.main(['../test_case/','--alluredir','../test_report/report_raw'])#生成allure格式的原生文件

   # "allure generate ./report_raw -o report/html --clean"
   # 需要在报告的电脑本地文件的当前路径下，使用cmd进入命令窗口
   # 输入上面的命令，其中中间是产生原生报告的路径， -o后面是产生新的可视化报告，且清除之前的报告

