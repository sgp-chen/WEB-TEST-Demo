import logging.config, logging
import unittest
from ddt import ddt, file_data
import os
from BeautifulReport import BeautifulReport
import time
from test_case.login import login_
from tools.demo import tools

CONF_LOG = "../log_config/config.ini"
logging.config.fileConfig(CONF_LOG)  # 采用配置文件


def save_img(self, test_method):
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace('\\', '/')
    img_path = root_dir + '/run/img'
    self.driver.get_screenshot_as_file('{}/{}.png'.format(img_path, test_method))


@ddt
class user_(login_):
    @file_data("../data/user_manager.yaml")
    def test_02(self, **kwargs):
        '''会员管理搜索测试'''
        self._testMethodDoc = "会员管理搜索测试"
        self.um.user_manager_search(kwargs['username'], kwargs['typename'], kwargs['phonenum'])
        name = self.driver.find_element_by_xpath("//td[text()='王茜']")
        self.assertEqual(kwargs["username"], name.text, msg="测试不通过")
        logging.info("会员搜索成功")

    @BeautifulReport.add_test_img("test_03")
    def test_03(self):
        '''会员管理重置按钮测试'''
        self.um.user_manager_reload()
        reload = self.driver.find_element_by_xpath('//input[@class="ant-input"]')
        self.assertEqual(reload.text, "", msg="测试不通过")
        logging.info("重置按钮重置成功")

    @BeautifulReport.add_test_img("test_04")
    def test_04(self):
        '''会员管理切换已离职标签'''
        self.um.user_manager_resign()
        resign = self.driver.find_element_by_xpath("//span[text()='温馨提示：1）员工复职前请优先保障该员工的必填信息完整。']")
        self.assertEqual(resign.text, "温馨提示：1）员工复职前请优先保障该员工的必填信息完整。", msg="测试不通过")
        logging.info("切换标签成功")

    def test_05(self):
        '''跳转添加会员'''
        self.um.add_user()
        self.assertIn("添加员工", self.driver.title, msg="测试通过")
        logging.info("成功跳转至:{}页面".format(self.driver.title))

    def test_06(self):
        '''添加新的成员'''
        b = tools(self.driver).ran_str()
        self.um.add_person(b)
        time.sleep(1)
        names = self.driver.find_element_by_xpath("//td[2]")
        self.assertEqual(b, names.text, msg="测试不通过")
        logging.info("添加员工成功")

    def test_07(self):
        '''跳转列表第一位会员并编辑'''
        try:
            self.um.edit_user()
            self.assertIn("编辑员工", self.driver.title, msg="测试不通过")
            logging.info("成功跳转至:{}页面".format(self.driver.title))
        except Exception as e:
            logging.error("错误：{}".format(e))

    def test_08(self):
        '''员工离职'''
        self.um.user_resign()
        self.um.click_close()
        self.um.click_ok()
        try:
            user = self.driver.find_element_by_xpath("//span[text()='更改成功']")
            self.assertEqual(user.text, "更改成功", msg="测试不通过")
            logging.info("员工离职成功")
        except:
            user = self.driver.find_element_by_xpath("//span[text()='该员工有未完成的业务']")
            self.assertEqual(user.text, "该员工有未完成的业务", msg="测试不通过")
            logging.info("员工有业务离职失败")

    @classmethod
    def tearDownClass(cls) -> None:
        time.sleep(1)
        cls.driver.quit()
        logging.info("成功关闭浏览器")


if __name__ == '__main__':
    unittest.main()
