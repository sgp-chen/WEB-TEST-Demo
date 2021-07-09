import unittest

from os import path
from ddt import ddt, data
from Excel_Config.Excel_config import Excel_Config
from my_config.log_config import get_log
import logging.config

@ddt
class test_case(unittest.TestCase):
    value = Excel_Config().excel_value("../data/新建 XLSX 工作表.xlsx")
    num = []
    for i in range(1, value + 1):
        num.append(i)

    @classmethod
    def setUpClass(cls) -> None:
        log_path = "../my_config/log.config"
        log_file_path = path.join(path.dirname(path.abspath(__file__)), log_path)
        logging.config.fileConfig(log_file_path)
        cls.log = logging.getLogger()
    @data(*tuple(num))
    def test_excel(self, num):
        self.log.info("正在执行第{}条用例".format(num))
        Excel_Config().Case_Run(num, self.log, "../data/新建 XLSX 工作表.xlsx")


if __name__ == '__main__':
    unittest.main()
