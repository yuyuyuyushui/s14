import logging
import sys
# logging.warning("user [alex] attempted wrong password more than 3 times")
# logging.critical("server is down")
print(sys.path)
logging.basicConfig(filename='D:\s14\作业\example.log', level=logging.INFO)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')