'''
    生成日志器的配置
'''
import logging.config
from os import path


# 路径一定要在调用的地方进行填写，不然会报错。
def get_log(paths):
    log_path = paths
    log_file_path = path.join(path.dirname(path.abspath(__file__)), log_path)
    logging.config.fileConfig(log_file_path)
    return logging.getLogger()
