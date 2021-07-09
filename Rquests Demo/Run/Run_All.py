import unittest
import datetime
from BeautifulReport import BeautifulReport
if __name__ == '__main__':
    discover = unittest.defaultTestLoader.discover("../Test_case", 'test*.py', None)
    filepath = "../report"
    now = datetime.datetime.now().strftime('%Y-%m-%d %H：%M：%S')
    filename = '测试报告 ' + str(now)
    BeautifulReport(discover).report(description='测试', filename=filename, log_path=filepath)