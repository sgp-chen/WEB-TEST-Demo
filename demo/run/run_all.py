import unittest
import os, datetime
from BeautifulReport import BeautifulReport
from tools.smtp_post import email_

if __name__ == '__main__':
    discover = unittest.defaultTestLoader.discover("../test_case", 'test*.py', None)
    # localpath = os.path.dirname(os.path.dirname(__file__)).replace("\\", "/")
    filepath = "../report"
    now = datetime.datetime.now().strftime('%Y-%m-%d %H：%M：%S')
    filename = '测试报告 ' + str(now)
    BeautifulReport(discover).report(description='测试', filename=filename, log_path=filepath)
    email_().mail_()
