# coding: utf-8
import sys
import os
sys.path.append(os.path.dirname(sys.path[0]))
# 将到上一层路径加入sys.path以便正常测试import
import time
from easycoins import OKCoin

"""
将logging设置为DEBUG，用于调试，生产环境可以设置为INFO甚至WARNING

logging是可以全局设置的类
"""
import logging
# 设置屏幕输出句柄
formatter = logging.Formatter(
    '[%(levelname)s] %(asctime)s - %(name)s - %(lineno)d - %(message)s'
)
logger = logging.getLogger("OKCoin")
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)
logger = logging.getLogger("OKCoinWS")
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)
logger = logging.getLogger("OKExWS")
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)

okcoin = OKCoin()

# okcoin.okcoin_ws.start()
okcoin.okex_ws.start()

# 设置api_key, secret_key并登录
from Unittest.account import get_api_key
# api_key_okcoin = get_api_key("api_key_okcoin.json")
# okcoin.okcoin_ws.set_api_key(api_key_okcoin["api_key"], api_key_okcoin["secret_key"])
# okcoin.okcoin_ws.login()
api_key_okex = get_api_key("api_key_okex.json")
okcoin.okex_ws.set_api_key(api_key_okex["api_key"], api_key_okex["secret_key"])
okcoin.okex_ws.login()

# okcoin.okex_ws.subscribe_ticker("btc", "this_week")

# okcoin.okex_ws.trade(
#     symbol="btc_usd",
#     contract_type="this_week",
#     price="2700",
#     volume="1",
#     order_type="1",
#     match_price="1",
#     lever_rate="10"
# )

help(okcoin)

while True:
    time.sleep(30)