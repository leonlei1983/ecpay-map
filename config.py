import os
import logging


BASE_PATH = os.path.dirname(os.path.realpath(__file__))
LOG_PATH = os.path.join(BASE_PATH, "log")
if not os.path.isdir(LOG_PATH):
    os.makedirs(LOG_PATH)

ECPAY_URL = "https://logistics-stage.ecpay.com.tw"
ECPAY_MERCHANTID = "2000132"
ECPAY_HASHKEY = "5294y06JbISpM5x9"
ECPAY_HASHIV = "v77hoKGq4kWxNNIS"


ECPAY_SERVER_REPLY = "https://127.0.0.1:5000/reply"

LOGGER_FORMAT = "%(levelname)s | %(asctime)s | %(filename)s:%(funcName)s:%(lineno)d | %(message)s"
LOGGER_FILE_PATH = os.path.join(LOG_PATH, "app.log")
LOGGER_LEVEL = logging.DEBUG

