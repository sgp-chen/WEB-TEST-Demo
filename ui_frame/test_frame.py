'''
    关键字驱动框架的程序主入口
'''
import allure
import sys,os
import pytest
from excel_driver import excel_read,excel_conf
import logging.config
from os import path


root_path = os.path.abspath(os.getcwd() + "\\.")
sys.path.append(root_path)
log_path = "./my_conf/log.ini"
log_file_path = path.join(path.dirname(path.abspath(__file__)), log_path)
logging.config.fileConfig(log_file_path)
logs = logging.getLogger("root")
@pytest.mark.parametrize('excel_path,sheet,log',[("./data/data.xlsx","Sheet2",logs)])
@allure.story("关键字+excel数据驱动")
@allure.title("测试用例")
def test_01(excel_path,sheet,log):
    '''测试用例'''
    excel_read.excel_runner(excel_path,sheet,log)
    case_assert=excel_conf.excel_sheet(excel_path,sheet)[2]
    for case in case_assert:
        assert case=="pass","测试不通过"

if __name__ == '__main__':
    pytest.main(["-s","-v",'--alluredir', './allure_report'])
    os.system('allure generate ./allure_report -o ./allure_report/report --clean')
    # 通过主入口调用excel的驱动读写，实现自动化测试
    # # 1. 生成日志器
    #
    # ## 2. excel驱动实现
    # ## excel_read.excel_runner(log)
    # # 2. 读取指定路径，获取所有的测试用例文件。
    # # case的list：用于接收所有的测试用例文件。
    # cases = []
    # # 读取指定路径下的所有文件
    # for path, dir, files in os.walk('./data/'):
    #     for file in files:
    #         # 获取文件的后缀名
    #         file_type = os.path.splitext(file)[1]
    #         if file_type == '.xlsx':
    #             excel_path = path + file
    #             cases.append(excel_path)
    #             print(excel_path)
    #         else:
    #             log.info('文件类型错误：{}'.format(file))
    #
    #     # 3. 调用excel_read进行关键字驱动自动化测试
    #     for case in cases:
    #         log.info('运行{}测试用例'.format(case))
    #         excel_read.excel_runner(case, log)
