# encoding:utf-8

import logging

# 日志级别大小关系为：CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET

logging.error("this is error message")
logging.warning("this is warning message")
logging.info("this is info message")
logging.debug("this is debug message")

# logging.basicConfig(level=logging.DEBUG,
#                 format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                 datefmt='%a, %d %b %Y %H:%M:%S',
#                 filename='myapp.log',
#                 filemode='w'
#                 )

console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

logging.error("this is error message")
logging.warning("this is warning message")
logging.info("this is info message")
logging.debug("this is debug message")