# coding=utf-8
__author__ = "jewelry_zhu"
import logging

logfile = './log/log.txt'
ch = logging.StreamHandler()
class Log():
    def __init__(self):
        self.file = logfile
        self.logger1 = logging.getLogger('mylogger2')
        self.logger1.setLevel(logging.DEBUG)
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
        ch.setFormatter(formatter)
        self.logger1.addHandler(ch)

    def info(self, msg):
        self.logger1.info(msg)

    def warning(self, msg):
        self.logger1.warning(msg)

    def error(self, msg):
        self.logger1.error(msg)

    def debug(self, msg):
        self.logger1.debug(msg)

    def close(self):
        self.logger1.removeHandler(ch)
