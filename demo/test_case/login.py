import os
from page.Login_page import login_page
from selenium import webdriver
import unittest
from ddt import ddt, file_data
from tools.demo import Chorme_option
import logging, logging.config
from page.user_manager import user_manager
import time

CONF_LOG = "../log_config/config.ini"
logging.config.fileConfig(CONF_LOG)  # 采用配置文件



def save_img(self, test_method):
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace('\\', '/')
    img_path = root_dir + '/run/img'
    self.driver.get_screenshot_as_file('{}/{}.png'.format(img_path, test_method))
# 调用ddt数据驱动装饰器
@ddt
# 定义unittest类并继承TestCase
class login_(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        try:
            cls.driver = webdriver.Chrome(options=Chorme_option().option())
            logging.info("打开Chrome浏览器")
            cls.driver.implicitly_wait(2)
            cls.lg = login_page(cls.driver)
            cls.um=user_manager(cls.driver)
            logging.info("实例化浏览器对象成功")
        except Exception as e:
            logging.error("实例化浏览器对象失败：{}".format(e))

    @file_data("../data/demo.yaml")
    def test_01(self, **kwargs):
        '''saas登录测试'''
        self._testMethodDoc = "saas登录测试"
        self.lg.login(kwargs["user"], kwargs["password"])
        self.assertEqual(self.driver.title, "员工管理列表 - 线测环境总部", msg="测试不通过")
        logging.info("登录saas成功")

    @classmethod
    def tearDownClass(cls) -> None:
        time.sleep(1)
        cls.driver.quit()
        logging.info("成功关闭浏览器")

if __name__ == '__main__':
    unittest.main()
