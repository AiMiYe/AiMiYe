import os
import sys
import time

sys.path.append(os.path.split(os.path.dirname(__file__))[0])
from loguru import logger as log
from selenium_notes.config import LOG


def get_logger():
    """
    初始化日志对象
    :return: 日志对象
    """
    # formatter = time.strftime('%Y%m%d%H%M%S', time.localtime())
    formatter = "debug"
    log.remove(handler_id=None)
    log.add(os.path.join(LOG, f"{formatter}.log"), backtrace=True, diagnose=True,
            level="INFO", rotation="01:00", encoding="UTF-8", compression="zip", retention="7 days")
    return log


logger = get_logger()
