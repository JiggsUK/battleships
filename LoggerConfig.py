import logging

formatter = logging.Formatter('%(asctime)s --%(levelname)s-- %(name)s/%(funcName)s: %(message)s', '%d/%m/%Y %H:%M:%S')

root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)

def setup_logger_info(name, log_file, level=logging.INFO):
    """Function setup as many loggers as you want"""

    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

def setup_logger_debug(name, log_file, level=logging.DEBUG):
    """Function setup as many loggers as you want"""

    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    logger1 = logging.getLogger(name)
    logger1.setLevel(level)
    logger1.addHandler(handler)

    return logger1