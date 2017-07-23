# coding: utf-8
import sys
import os
sys.path.append(os.path.dirname(sys.path[0]))
# 将到上一层路径加入sys.path以便正常测试import
from EasyCoins import PoloniexWebSocket

"""
将logging设置为DEBUG，用于调试，生产环境可以设置为INFO甚至WARNING

logging是可以全局设置的类
"""
import logging
# 设置屏幕输出句柄
formatter = logging.Formatter(
    '[%(levelname)s] %(asctime)s - %(name)s - %(lineno)d - %(message)s'
)
logger = logging.getLogger("PoloniexWebSocket")
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)

poloniex_ws = PoloniexWebSocket()
poloniex_ws.start()