import logging

def logger_atm(log_type):
    logger = logging.getLogger(log_type)
    fh = logging.FileHandler('logs/file.log')
    ch = logging.StreamHandler()

    formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s = %(message)s ')

    fh.setFormatter(formater)
    ch.setFormatter(formater)
    logger.setLevel(logging.DEBUG)#参数可
    return logger
