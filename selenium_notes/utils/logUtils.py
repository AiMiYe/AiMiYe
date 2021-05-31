import os
import time
from loguru import logger as log
from selenium_notes.config import LOG



def get_logger():
    """
    初始化日志对象
    :return: 日志对象
    """
    log.remove(handler_id=None)
    log.add(os.path.join(LOG, f"{time.strftime('%Y%m%d%H%M%S', time.localtime())}.log"), backtrace=True, diagnose=True,
            level="INFO", rotation="21:40", encoding="UTF-8", compression="zip", retention="7 days")
    return log


logger = get_logger()

